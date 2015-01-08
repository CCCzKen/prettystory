# coding: utf-8
import time
import hashlib
from lxml import etree
from flask import render_template, request, Blueprint
from flask import url_for, redirect, make_response

bp = Blueprint('home', __name__)

xml_text = 
'''
<?xml version="1.0" encoding="UTF-8"?>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
'''

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
	xml = etree.fromstring(request.data)
	content = xml.find('Content').text
	fromUser = xml.find('FromUserName').text
	toUser = xml.find('ToUserName').text
	msg = u'我现在还在开发中，还没有什么功能，您刚才说的是：' + content
	response = make_response(xml_text % (toUser, FromUserName, str(int(time.time())), msg))
	return response


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
