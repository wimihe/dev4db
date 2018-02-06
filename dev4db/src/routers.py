#coding:utf-8
#Created by weimi on 2018/2/6.


from tornado.web import url

from src.handlers import test


urls = [
    url(r"/", test.TestHandler, name='test'),
]
