#-*- coding:utf-8 -*-
from src import web_app


from bae.core.wsgi import WSGIApplication
application = WSGIApplication(web_app)