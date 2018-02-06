#coding:utf-8
#Created by weimi on 2018/2/3.


from tornado.ioloop import IOLoop

from src.application import Dev4db

app = Dev4db()
app.listen(8888)
IOLoop.current().start()