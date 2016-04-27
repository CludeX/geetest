# coding:utf-8
import threading
import time

import tornado.ioloop
import tornado.web

from config import DEBUG, STATIC_DIR, APP_HOST, APP_ADDR
from tools import gee_database, gee_redis, listen_mongo
from urls import url
from watch_redis import get_redis_event

db = gee_database()
r = gee_redis()
l_mongo = listen_mongo()

settings = {
    "static_path": STATIC_DIR,
    # "template_path" : os.path.join(STATIC_DIR, "templates"),
    "template_path": STATIC_DIR,
    "gzip": True,
    "redis": gee_redis()
}


class myThread(threading.Thread):
    def __init__(self, r, m):
        threading.Thread.__init__(self)
        self.redis = r
        self.mongo = m

    def run(self):
        print "Starting "
        get_redis_event(self.redis, self.mongo)
        print "Exiting "


def lister_redis():
    newThread = myThread(r, l_mongo)
    newThread.start()


def make_app():
    app = tornado.web.Application(
        url, db=db, debug=DEBUG, **settings)
    return app


if __name__ == "__main__":
    print "host:%s;addr:%s" % (APP_HOST, APP_ADDR)
    lister_redis()
    app = make_app()
    app.listen(APP_ADDR, address=APP_HOST)
    tornado.ioloop.IOLoop.current().start()
