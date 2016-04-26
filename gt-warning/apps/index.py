# coding:utf-8
import tornado.gen
import tornado.web

from tools import return_500
from apps.basehandler import BaseHandler
from config import STATIC_DIR
import tornadoredis

class MainHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            self.render('index.html')
        except Exception as e:
            print e
            return_500(self)
