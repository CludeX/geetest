#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from time import time

import requests

CorpID = "wx65054867f1dc5947"
Secret = "3HSF-3UWh_HQLQp5LGcrveDrPnNHQ2fdeKCn0xzNe573rFXiR39Te3jD8AWKb5IP"


class WeixinError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Weixin(object):
    def __init__(self):
        self.access_token = None
        self.expire = 0

    def get_access_token(self):
        if time() < self.expire:
            return self.access_token

        access_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (CorpID, Secret)
        r = requests.get(access_url)
        try:
            access_token = r.json()["access_token"]
            expires_in = r.json()["expires_in"]
        except KeyError:
            raise WeixinError("can't get access token: %s" % str(r.json()))
        self.access_token = access_token
        self.expire = time() + expires_in - 5
        return access_token

    def send_msg(self, text, users, parts=None):
        msg_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % \
                  (self.get_access_token(),)
        if isinstance(users, list):
            users = "|".join(users)
        if isinstance(parts, list):
            parts = "|".join(parts)
        elif parts is None:
            parts = ""
        # print text, type(text)
        if isinstance(text, unicode):
            text = text.encode("utf8")
        msg = {
            "touser": users,
            "toparty": parts,
            "totag": "",
            "msgtype": "text",
            "agentid": 6,
            "text": {
                "content": text
            },
            "safe": "0"
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        rawdata = json.dumps(msg, ensure_ascii=False)
        # print json.dumps(msg)
        r = requests.post(msg_url, data=rawdata, headers=headers)
        errcode = r.json()["errcode"]
        if errcode != 0:
            raise WeixinError("can't send message: %s." % str(r.json()))


if __name__ == '__main__':
    w = Weixin()
    w.send_msg(u"你是", ["xieqiang", "yangyu", "wangpeifeng"])
    # w.send_msg(u"你是", ["yangyu"])
