# coding:utf-8
import json

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    pagination_class = None

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.db = self.settings['db']
        self.redis = self.settings['redis']

    def write_response(self, data="", status=1, **kwargs):
        response = {'data': data}
        response.update(kwargs)
        response.update({'status': status})

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(response))
        self.finish()
