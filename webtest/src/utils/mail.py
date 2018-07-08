import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror,error
from utils.log import logger


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """
        初始化email
        :param title 邮件标题，必填
        :param message: 邮件正文，非必填
        :param path: 附件路径，可传入list或str，非必填
        :param server
        :param sender
        :param password
        :param receiver
        """
        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file,'rb').read(),'plain','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]',att_file)
        att["Content-Disposition"] = 'attachment;filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list）或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror and error) as e:
            logger.exception('Send mail failed, cant\'t connect to server,check you network and smtp server')
        else:
            try:
                smtp_server.login(self.sender,self.password) # 登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('username or password wrong %s',e)
            else:
                smtp_server.sendmail(self.sender,self.receiver.split(';'),self.msg.as_string())
            finally:
                smtp_server.quit()
                logger.info('send mail"{0}" success! receiver:{1}.if not receive mail,please check your trash box'
                            ' and check receiver address'.format(self.title,self.receiver))

        


    