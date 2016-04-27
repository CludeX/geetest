# coding:utf-8
import json

import tornado.gen

from apps.basehandler import BaseHandler
from models.channel import Channel
from tools import return_500, get_traceback


class ChannelHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):                                           #get方法
        try:
            channels = yield self.db.Channel.find().sort("_id", -1).to_list(length=100)
            self.write_response(channels, status=1)
        except Exception as e:
            print e
            return_500(self)
            self.write_response("", status=0)

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)     #将json格式文件变成字典
            c = Channel(data['_id'], body=data)
            channel = c.get()
            yield self.db.Channel.insert(channel)
            self.write_response("")
        except Exception as e:
            print e
            self.write_response("", status=0, error="channel 添加失败")
            get_traceback()


class SettingChannelHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            channel = yield self.db.Channel.find_one({"_id": data["_id"]})
            if channel:
                c = Channel(_id=channel['_id'], body=data)
                channel = c.get()
            yield self.db.Channel.save(channel)
        except:
            self.write_response("", status=0)
            get_traceback()





