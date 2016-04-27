# coding:utf-8
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def base_sendmail(to, subject, text):
    HOST = "smtp.exmail.qq.com"
    SUBJECT = subject
    TO = to

    FROM = "warning@geetest.com"
    Text = text

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = SUBJECT
    msgRoot['From'] = "极验110"
    msgRoot['To'] = string.join(TO, ',')
    msgText = MIMEText(Text.replace('\n', '<br>'),
                       'html', 'utf-8')
    msgRoot.attach(msgText)
    server = smtplib.SMTP(HOST)
    server.login("warning@geetest.com", "gt2012wuhan")
    server.sendmail(FROM, TO, msgRoot.as_string())
    server.close()
    print "over"


def send_email(email, name, level, text="rt"):
    subject = "%s异常,\"%s\"级警报"%(name, level)
    base_sendmail(email, subject, text)


if __name__ == "__main__":
    email_list = [
        "282872104@qq.com",
    ]
    base_sendmail(email_list, "")
