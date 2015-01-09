# coding: utf-8
from flask import render_template, Blueprint, request
from flask import make_response, redirect, url_for

bp = Blueprint('wechat', __name__)


@bp.route('/')
def wechat_auth():
	query = request.args
	return 'pretty'
