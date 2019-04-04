#coding:utf-8
'''
Created on 2019��3��29��

@author: Administrator
'''
import smtplib
from email.mime.text import MIMEText
from email.Header import Header
import datetime

from email.mime.multipart import MIMEMultipart

from email.mime.application import MIMEApplication
from email.utils import formatdate


class SendEmail:
    
    def __init__(self,host,send_user,to_user,pwd):
        self.host=host
        self.send_user=send_user
        self.to_user=to_user
        self.pwd=pwd
    
    def send_mail(self):
        #上传附件的处理
        msg = MIMEMultipart()
        text=MIMEText("yes，这是一条测试")#设置正文
        
        msg["Subject"]="这是第一条测试短息"#设置标题
        msg["From"]=self.send_user#设置发送者
        msg["to"]=self.to_user#设置接受者
        msg["Date"]=formatdate(localtime=True)
        msg.attach(text)
        
        #---这是附件部分---
        #xlsx类型附件
        part = MIMEApplication(open(r"C:/Users/Administrator/Desktop/3333.xls",'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=r"C:/Users/Administrator/Desktop/3333.xls")
        msg.attach(part)
        
        server=smtplib.SMTP_SSL()
        server.connect(self.host,465)
        server.login(self.send_user,self.pwd)#登陆服务器
        server.sendmail(self.send_user,self.to_user, msg.as_string())#发送邮件
        server.close()


if __name__=="__main__":
    to_list=['651525091@qq.com']
    test=SendEmail("smtp.qq.com","1119864992@qq.com",to_list[0],"clefcofolgvcgied")
    test.send_mail()
    
    
        
        
    
