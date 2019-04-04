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
    
    def __init__(self,host,send_user,to_user,pwd,total,suceccs,fail):
        self.host=host
        self.send_user=send_user
        self.to_user=to_user
        self.pwd=pwd
        self.total=total
        self.fail=fail
        self.suceccs=suceccs
    
    def send_mail(self):
        #上传附件的处理
        msg = MIMEMultipart()
        text=MIMEText(self.maintext())#设置正文
        
        msg["Subject"]="接口自动化测试报告"#设置标题
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
    def maintext(self):
        #suceccs=suceccs+0.0
        SuccessRate=int((float(self.suceccs)/self.total)*100)
        print SuccessRate
        FailRate=int((float(self.fail)/self.total)*100)
        print type(FailRate)
        print FailRate
        str=("当前接口自动化测试完成，总共完成用例"+"".join(bytes(self.total))+
             "条，成功"+"".join(bytes(self.suceccs))+"条，失败"+
             "".join(bytes(self.fail))+"条，成功率："+"".join(bytes(SuccessRate))+
             "%,失败率："+"".join(bytes(FailRate))+"%，查看详情请阅读附件。")
        #     +"条，功"
        #bytes(self.suceccs)+"条，失败"+bytes(self.fail)+"条，成功率为："
        #+bytes(SuccessRate)+"%,失成败率为：")
        #+FailRate+"%"
        #+bytes(SuccessRate)+"%,失成败率为："+bytes(FailRate)
        #s=bytes(self.total)
        #str=str1+s
        
        
        
        return str

'''
if __name__=="__main__":
    to_list=['651525091@qq.com']
    test=SendEmail("smtp.qq.com","1119864992@qq.com",to_list[0],"clefcofolgvcgied",5,3,2)
    test.send_mail()
'''