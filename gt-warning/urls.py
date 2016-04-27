# coding:utf-8
import os

import tornado.web

from apps.index import MainHandler
from config import BASE_DIR,STATIC_DIR
from tools import logger

def app_url():
    apps_url = []
    directory = os.path.join(BASE_DIR, 'apps')
    try:
        for filename in os.listdir(directory):
            try:
                full_path = os.path.join(directory, filename)
                if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, 'urls.py')):
                    apps_url += getattr(
                        __import__(os.path.join('apps', filename, 'urls').replace('/', '.'), fromlist=['url']), 'url')
            except Exception as e:
                print e, ":url", filename
                logger.error(full_path)
                logger.error(e)
    except Exception as e:
        print e, ":url error"
        logger.error(e)
    return apps_url


url = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": STATIC_DIR}),
    (r"/media/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(BASE_DIR, "media")}),
    (r"/node_modules/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(STATIC_DIR, "node_modules")}),
    (r"/bower/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(STATIC_DIR, "bower_components")}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(STATIC_DIR, "js")}),
]

url += [
    (r"/", MainHandler),
    (r"/channels", MainHandler),
    (r"/groups", MainHandler),
    (r"/members", MainHandler),
    (r"/logs", MainHandler),
    # (r"(.+)", MainHandler),
]

url += app_url()