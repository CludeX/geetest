# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from models.logs import HistoryLog


def logMessage(event, channel, db):
    e = channel["event"]["level1"]
    message = {
        "operation": e["operation"],
        "groups": e["groups"],
        "active": "false"
    }
    members = {
            "name": "wjy",
            "email": "475477375@qq.com"
        }
    log = db.Log.find({"time": event["time"],
                       "level": event["level"], "active": "true"})
    write_log = dict(event, **message)
    print write_log
    if not log:
            write_log["active"] = "true"
            for m in members["email"]:
                send_email(m)
    write(write_log, db)


def send_email(m):
    sender = 'from@runoob.com'
    receiver = [m]
    message = MIMEText('异常报警...', 'plain', 'utf-8')
    message['From'] = Header('极验验证', 'utf-8')
    message['To'] = Header('测试', 'utf-8')
    subject = "极验监测"
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"


def write(write_log, db):
    try:
        l = HistoryLog(_id=write_log["id"], body=write_log)
        log = l.get()
        db.Log.insert(log)
        print "日志写入成功"
    except Exception as e:
        print e

