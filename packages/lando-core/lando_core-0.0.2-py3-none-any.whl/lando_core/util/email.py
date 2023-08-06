import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import random
import re
from tenacity import wait_random_exponential, stop_after_attempt, retry


class EmailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    @retry(wait=wait_random_exponential(min=1, max=3), stop=stop_after_attempt(3))
    async def send_email(self, header, subject, body, email):
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = Header(header, 'utf-8')
        message.attach(MIMEText(body))

        # 使用SMTP连接发送邮件
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, email, message.as_string())
                print('Email sent successfully!')
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def check_email(email):
        # 定义电子邮件地址的正则表达式
        pattern = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

        # 使用正则表达式验证电子邮件地址
        if re.match(pattern, email):
            return True
        else:
            return False
