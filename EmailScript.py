#!/user/bin/env python3
# 可以使用不同的
import smtplib
from email.mime.text import MIMEText

#if you use the config.py ,your can add this content in it. as for me ,I often write a config.py to store my configrations.
#config content like this
#EmailAdress ={
#        'fromAdd' : "XXX@qq.com",  # 你的邮箱   发件地址
#        # to_ = input('Please input Recipient:')  # 收件地址
#        'toAdd' : "xxxxx@qq.com",
#        # subject = input('Please input title:')  # 邮件标题
#
#        'pwd' : "xxxxxx",  # 授权码  nkijfhnodibbiifb  smtp tmap
##
#        #报告的主题分级
#        'serverName':'测试用爬虫服务器',
#
#        'ordernaryReport':serverName+"-"+"服务器爬虫日常数据汇报" , #这个是用来发送平时的每日数据汇报的情况的
#       'ordernaryDeadlyReport': serverName+"-"+"服务器爬虫崩溃检修报告" ,#这个用于日常的服务器中爬虫死亡了提供崩溃信息还有数据汇报总结
#}


EmailAdress = {

class EMail(object):
    def __init__(self):
        self.fromAdd = EmailAdress['Sender']  # 你的邮箱   发件地址
        # to_ = input('Please input Recipient:')  # 收件地址
        self.toAdd = EmailAdress['toWho']
        # subject = input('Please input title:')  # 邮件标题
        # self.subject = "服务器 新闻爬虫运行终端报告"

        self.pwd = EmailAdress['pwd']  # 授权码  nkijfhnodibbiifb  smtp tmap
        self.ordernaryReport = EmailAdress['ordernaryReport']  #日常报告的主题
        self.ordernaryDeadlyReport = EmailAdress['ordernaryDeadlyReport']   #死亡的时候就要这个主题


    def SendEmail(self,subjectLevel,text):  #选择使用不同的时候发送不同的主题
        if subjectLevel==1: 
            subject = self.ordernaryReport
        elif subjectLevel==2:
            subject = self.ordernaryDeadlyReport

        # print(text)
        msg = MIMEText(text)
        msg["Subject"] = subject
        msg["From"] = self.fromAdd
        msg["To"] = self.toAdd
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)     #you can change your email provider here 
            s.login(self.fromAdd, self.pwd)
            s.sendmail(self.fromAdd, self.toAdd, msg.as_string())
            s.quit()
            print("Success!")
        except smtplib.SMTPException:
            print('Falied!')


if __name__ == '__main__':
    # text = input('Please input Content:')  # 邮件内容
    text = "😍成功了拉，以后自动检测后就可以定时的向手机汇报程序中断了的消息拉"
    email = EMail()

    email.SendEmail(1, text)
