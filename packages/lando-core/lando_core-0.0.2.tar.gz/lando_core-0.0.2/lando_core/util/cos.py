import io
import os
import re
from urllib.parse import unquote, urlparse, quote

from qcloud_cos import CosConfig, CosS3Client
from sts.sts import Scope, Sts


class CosService:
    def __init__(self, bucket_name, bucket_id, region, secret_id, secret_key, cos_server):
        self.bucket_name = bucket_name
        self.bucket_id = bucket_id
        self.region = region
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.cos_server = cos_server
        self.config = CosConfig(Region=self.region, SecretId=self.secret_id,
                                SecretKey=self.secret_key, Token=None)
        self.client = CosS3Client(self.config)
        self.bucket = f'{self.bucket_name}-{self.bucket_id}'

    async def get_temp_credential(self, path_prefix, header_prefixs):
        allow_actions = [
            # Obtain signature link
            'name/cos:GetObject',
            # total Upload
            'name/cos:PutObject',
            'name/cos:PostObject',
            # Batch upload
            'name/cos:InitiateMultipartUpload',
            'name/cos:ListMultipartUploads',
            'name/cos:ListParts',
            'name/cos:UploadPart',
            'name/cos:CompleteMultipartUpload',
            # Cancel block upload operation
            "name/cos:AbortMultipartUpload"
        ]
        scopes = list()
        for header_prefix in header_prefixs:
            temp_scopes = [Scope(action=action, bucket=f'{self.bucket_name}-{self.bucket_id}',
                                 region=self.region, resource_prefix=path_prefix)
                           for action in allow_actions]
            temp_scopes.append(
                Scope(action="name/cos:HeadObject", bucket=f'{self.bucket_name}-{self.bucket_id}',
                      region=self.region, resource_prefix=header_prefix))  # 查询对象元数据
            scopes.extend(temp_scopes)
        config = {
            'url': 'https://sts.tencentcloudapi.com/',
            # 域名，非必须，默认为 sts.tencentcloudapi.com
            'domain': 'sts.tencentcloudapi.com',
            # 临时密钥有效时长，单位是秒
            'duration_seconds': 24 * 60 * 60,
            'secret_id': self.secret_id,
            # 固定密钥
            'secret_key': self.secret_key,
            # 换成你的 bucket
            'bucket': f'{self.bucket_name}-{self.bucket_id}',
            # 换成 bucket 所在地区
            'region': self.region,
            # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
            # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
            'allow_prefix': '*',  # path_prefix,
            # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
            'policy': Sts.get_policy(scopes)
        }
        try:
            sts = Sts(config)
            result = sts.get_credential()
            if isinstance(result, dict):
                result.update({
                    'bucket': f'{self.bucket_name}-{self.bucket_id}',
                    'region': self.region,
                })
            return result
        except Exception as e:
            print(e)

    def upload_binary(self, buffer, key):
        pass


class CosFile(CosService):
    def __init__(self, bucket_name, bucket_id, region, secret_id, secret_key, cos_server):
        super().__init__(bucket_name, bucket_id, region, secret_id, secret_key, cos_server)

    def map_server_local(self, url):
        """ Map COS server path to local path
        The server path has two versions - CDN and location specific version"""
        return unquote(urlparse(url).path).lstrip('/')

    def map_local_server(self, local_path, bucket_name=None):
        """ Map COS Server path to local path """
        # url = client.get_object_url(
        #     Bucket=BUCKET,
        #     Key=local_path
        # )
        if bucket_name is not None:
            return f'https://{bucket_name}-{self.bucket_id}.cos.{self.region}.myqcloud.com/' + quote(local_path, safe=":/.")
        return self.cos_server + '/' + quote(local_path, safe=":/.")

    def expanded_ext(self, filename):
        """ Extensions with language specifier, or type specifier """
        exts = re.findall(r'((\.[A-Za-z0-9]{1,5})?\.[A-Za-z0-9]{1,6}$)', filename)
        if exts:
            return exts[0][0]
        return ''

    def ext(self, filename):
        """ Extensions with language specifier, or type specifier """
        exts = re.findall(r'(\.[A-Za-z0-9]{1,6}$)', filename)
        if exts:
            return exts[0]
        return ''

    def cos_file_path(self, local_path):
        if isinstance(local_path, dict):  # Check if local_path is already a dictionary
            return local_path

        str_local_path = local_path

        if str_local_path.startswith("http"):
            str_local_path = self.map_server_local(str_local_path)
        local_path = str_local_path.lstrip('/')
        dirname, basename = os.path.split(local_path)
        title = os.path.splitext(basename)[0]
        expanded_ext = self.expanded_ext(local_path).lstrip('.')
        title_without_expanded_ext = basename[:basename.find(expanded_ext) - 1]
        ext = self.ext(local_path).lstrip('.')
        url = self.map_local_server(local_path)

        return {
            'local_path': local_path,
            'dirname': dirname,
            'basename': basename,
            'title': title,
            'expanded_ext': expanded_ext,
            'title_without_expanded_ext': title_without_expanded_ext,
            'ext': ext,
            'url': url,
            'is_dir': basename == ''
        }

    async def upload_binary(self, buffer, key):
        """
        Upload binary content to COS file

        :param buffer: bytes
        :param key: COS file key, starting with root dir name and without leading "/"
        :return: COS URL
        """
        cfp = self.cos_file_path(key)
        self.client.upload_file_from_buffer(
            Bucket=self.bucket, Key=cfp['local_path'], Body=io.BytesIO(buffer)
        )
        return cfp['url']

