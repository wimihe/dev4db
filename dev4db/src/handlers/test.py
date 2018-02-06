#coding:utf-8
#Created by weimi on 2018/2/6.


from src import BaseHandler

class TestHandler(BaseHandler):

    async def get(self):
        result = await self.db().database_names()
        self.write(result)