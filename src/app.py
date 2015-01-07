# coding: utf-8
import logging
import settings
from ._flask import Flask

def init_logger(app):
	if app.debug:
		return

	handler = logging.StreamHandler()
	handler.setLevel(logging.ERROR)
	app.logger.addHandler(handler)

def register_routes(app):
	import home
	app.register_blueprint(home.bp, url_prefix='/')


def create_app(config=None):
	app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)
	app.config.from_object(settings)
	app.static_folder = app.config.get('STATIC_FOLDER')
	init_logger(app)
	register_routes(app)
	return app