#coding:utf-8
#Created by weimi on 2018/2/6.

import json

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def db(self):
        return self.application.db
    
    def write(self, chunk):
        if isinstance(chunk, (list, tuple)):
            chunk = {
                'total': len(chunk),
                'data': chunk
            }
        super(BaseHandler, self).write(json.dumps(chunk))