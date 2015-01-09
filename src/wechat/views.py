# coding: utf-8
import hashlib
from src import settings
from flask import render_template, Blueprint, request
from flask import make_response, redirect, url_for

bp = Blueprint('wechat', __name__)


@bp.route('/', methods=['GET'])
def wechat_access_verify():
	echostr = request.args.get('echostr', '')
	if verification(request):
		return echostr
	return 'something wrong'


def verification(request):
	token = settings.TOKEN
	signature = request.args.get('signature', '')
	timestamp = request.args.get('timestamp', '')
	nonce = request.args.get('nonce', '')
	data = [token, timestamp, nonce]
	data.sort()
	data = ''.join(data)
	hashcode = hashlib.sha1(data).hexdigest()
	if hashcode == signature:
		return True
	return False
