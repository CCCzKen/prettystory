# coding: utf-8
from flask import render_template, request, Blueprint
from flask import url_for, redirect

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
	return 'Hello World'