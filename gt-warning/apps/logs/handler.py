# coding:utf-8
import tornado.gen

from apps.basehandler import BaseHandler
from tools import return_500


class LogsHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        page = self.get_argument("page", 1)
        page = int(page)
        number = 10
        start = number * (page-1)
        try:
            logs = yield self.db.HistoryLog.find(skip=start).sort("_id", -1).to_list(length=number)
            for log in logs:
                try:
                    log["time"] = log["time"].strftime("%Y-%m-%d %H:%M:%S")
                except:
                    log["time"] = "0000-00-00 00:00:00"
            self.write_response(logs, status=1)
        except Exception as e:
            print e
            return_500(self)


class LogLengthHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            logs = yield self.db.HistoryLog.find().sort("_id", -1).to_list(length=100)
            for log in logs:
                try:
                    log["time"] = log["time"].strftime("%Y-%m-%d %H:%M:%S")
                except:
                    log["time"] = "0000-00-00 00:00:00"
            self.write_response(logs, status=1)
        except Exception as e:
            print e
            return_500(self)
            self.write_response("", status=0)

