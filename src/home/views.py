# coding: utf-8
import hashlib
from flask import render_template, request, Blueprint
from flask import url_for, redirect, make_response

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
	return 'Hello World'

@bp.route('wechat/', methods=['GET', 'POST'])
def wechat_auth():
	token = 'prettystory'
	query = request.args
	signature = query['signature']
	timestamp = query['timestamp']
	nonce = query['nonce']
	echostr = query['echostr']
	data = [token, timestamp, nonce]
	data.sort()
	data = ''.join(data)
	hashcode = hashlib.sha1(data).hexdigest()
	if hashcode == signature:
		return echostr

@bp.route('test/')
def test():
	token = 'prettystory'
	signature = 'bf76fdf980abcb11325fe347df84ca9d6bcd67d5'
	echostr = '3178196012987580285'
	timestamp = '1420689213'
	nonce = '697622616'
	data = [token, timestamp, nonce]
	data.sort()
	data = ''.join(data)
	hashcode = hashlib.sha1(data).hexdigest()
	if hashcode == signature:
		return hashcode
	else:
		return 'false'