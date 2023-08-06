from setuptools import find_packages, setup

name = 'lando_core'
requires_list = open(f'{name}/requirements.txt', 'r', encoding='utf8').readlines()
requires_list = [i.strip() for i in requires_list]

setup(
    name=name,  # 包名同工程名，这样导入包的时候更有对应性
    version='0.0.2',
    author="lando",
    author_email='lando@gmail.com',
    description="A small example package",
    python_requires="==3.10.*",
    packages=find_packages(exclude=[".tests", ".tests.", "tests.", "tests"]),
    package_data={"": ["*"]},  # 数据文件全部打包
    include_package_data=True,  # 自动包含受版本控制(svn/git)的数据文件
    zip_safe=False,
    # data_files=['img_classifier/config/conf.yaml',
    #             'img_classifier/models/flag.pt',
    #             'img_classifier/people_model/face.lib',
    #             'img_classifier/porn_model/porn_classifier_model.onnx'
    #             ]

    # 设置依赖包
    install_requires=requires_list
)
