# coding:utf-8

class Member(object):
    fields = ["_id", "tel", "email", "wechat"]
    filter_fields = ["tel", "email", "wechat"]

    default = {
        "tel": "",
        "email": "",
        "wechat": ""
    }

    def __init__(self, _id, **kwargs):
        self._id = _id
        self.body = kwargs['body']

    def get(self):
        member = {}
        member['_id'] = self._id
        for i in self.filter_fields:
            member[i] = self._filter(i)
        return member

    def _filter(self, name):
        return self.body.get(name, self.default.get(name))
