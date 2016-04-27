# coding:utf-8
import tornado.gen

from apps.basehandler import BaseHandler
from models.member import Member
from tools import return_500

import json

class ManageHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            members = yield self.db.Member.find().sort("_id", -1).to_list(length=100)
            self.write_response(members, status=1)
        except Exception as e:
            print e
            return_500(self)
            self.write_response("", status=0)

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            m = Member(_id=data["_id"], body=data)
            member = m.get()
            yield self.db.Member.insert(member)
            self.write_response("", status=1)
        except:
            self.write_response("", status=0)

class ChangeManageHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            m = Member(_id=data["_id"], body=data)
            member = m.get()
            yield self.db.Member.save(member)
            self.write_response("", status=1)
        except:
            self.write_response("", status=0)
