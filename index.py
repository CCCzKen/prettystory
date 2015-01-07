#-*- coding:utf-8 -*-
from src import web_app
import flask
def app(environ, start_response):
	return 'Hello world'

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
