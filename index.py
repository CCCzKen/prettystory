#-*- coding:utf-8 -*-
import flask
def app(environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/html')]
	start_response(status, headers)
	return 'Hello world'

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
