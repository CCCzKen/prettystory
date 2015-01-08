# coding: utf-8
import hashlib
import time
from flask import render_template, request, Blueprint
from flask import url_for, redirect, make_response

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
	return 'Hello World'

@bp.route('wechat/', methods=['GET', 'POST'])
def wechat_auth():
	# return str(time.time())
	if request.method == 'GET':
		token = 'prettystory'
		data = request.args
		signature = data.get('signature')
		timestamp = data.get('timestamp')
		nonce = data.get('nonce')
		echostr = data.get('echostr')
		print timestamp, nonce, token
		args = [token, timestamp, nonce]
		args.sort()
		args = ''.join(args)
		hashcode = hashlib.sha1(args).hexdigest()
		if hashcode == signature:
			return echostr
		else:
			return 'false'