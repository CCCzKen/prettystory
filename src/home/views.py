# coding: utf-8
import hashlib
from flask import render_template, request, Blueprint
from flask import url_for, redirect, make_response

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
	return 'Hello World'

@bp.route('wechat/')
def wechat_auth():
	token = 'prettystory'
	query = request.args
	signature = query.get('signature')
	timestamp = query.get('timestamp')
	nonce = query.get('nonce')
	echostr = query.get('echostr')
	data = [token, timestamp, nonce]
	data.sort()
	data = ''.join(data)
	hashcode = hashlib.sha1(data).hexdigest()
	if hashcode == signature:
		return echostr