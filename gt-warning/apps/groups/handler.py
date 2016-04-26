# coding:utf-8
import json

import tornado.gen

from apps.basehandler import BaseHandler
from models.group import Group
from tools import return_500


class GroupHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            groups = yield self.db.Group.find().sort("_id", -1).to_list(length=100)
            self.write_response(groups, status=1)
        except Exception as e:
            print e
            return_500(self)
            self.write_response("", status=0)

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            # data = {_id:dev, members: [1,2,3]}
            data = json.loads(self.request.body)  # 将json文件变成字典
            g = Group(_id=data["_id"], body=data)
            group = g.get()
            # group = {_id:dev, create_time:xxx-xxx-xxx, level:3, memebers:[1,2,3]}
            yield self.db.Group.insert(group)
            self.write_response("")
        except Exception as e:
            print e
            self.write_response("", status=0)


class AddNewMemberHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            g = Group(_id=data["_id"], body=data)
            member = g.get()
            yield self.db.Group.save(member)
            self.write_response("", status=1)
        except Exception as e:
            print e
            self.write_response("", status=0)

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            groups = yield self.db.Group.find().sort("_id", -1).to_list(length=100)
            self.write_response(groups, status=1)
        except Exception as e:
            print e
            return_500(self)
            self.write_response("", status=0)
