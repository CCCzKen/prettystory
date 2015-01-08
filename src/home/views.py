# coding: utf-8
import time
import hashlib
from lxml import etree
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
	signature = query.get('signature', '')
	timestamp = query.get('timestamp', '')
	nonce = query.get('nonce', '')
	echostr = query.get('echostr', '')
	data = [token, timestamp, nonce]
	data.sort()
	data = ''.join(data)
	hashcode = hashlib.sha1(data).hexdigest()
	if hashcode == signature:
		return make_response(echostr)
	return 'false'

@bp.route('reply/', methods=['POST'])
def reply():
	str_xml = request.form()
	xml = etree.fromstring(str_xml)
	content = xml.find('Content').text
	msgType = xml.find('MsgType').text
	fromUser = xml.find('FromUserName').text
	toUser = xml.find('ToUserName').text
	return render_template(
		'reply_text.xml',
		toUser=toUser,
		fromUser=fromUser,
		createTime=time.time(),
		content=u'我现在还在开发中，还没有什么功能，您刚才说的是：' + content,
	)
# @bp.route('reply/')
# def reply():
# 	toUser = 'ken'
# 	fromUser = 'kang'
# 	content = u'你好'
# 	return render_template(
# 		'reply_text.xml',
# 		toUser=toUser,
# 		fromUser=fromUser,
# 		createTime=time.time(),
# 		content=content,
# 	)
