#-*- coding:utf-8 -*-
from src import web_app
def app(environ, start_response):
	return web_app

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
