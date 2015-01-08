# coding: utf-8
import time
import hashlib
from lxml import etree
from flask import render_template, request, Blueprint
from flask import url_for, redirect, make_response

bp = Blueprint('home', __name__)

xml_text = """
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
"""

@bp.route('', methods=['GET', 'POST'])
def wechat_auto():
	if request.method == 'POST':	
		xml = etree.fromstring(request.stream.read())
		content = xml.find('Content').text
		fromUser = xml.find('FromUserName').text
		toUser = xml.find('ToUserName').text
		msg = u'我现在还在开发中，还没有什么功能，您刚才说的是：' + content
		response = make_response(xml_text % (toUser, fromUser, str(int(time.time())), msg))
		response.content_type='application/xml'
		return response
	return make_response(u'请用微信发送信息')

@bp.route('wechat/', methods=['GET', 'POST'])
def wechat_insert():
	if request.method == 'GET':
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

@bp.route('reply/', methods=['GET', 'POST'])
def reply():
	if request.method == 'POST':
		xml = etree.fromstring(request.stream.read())
		content = xml.find('Content').text
		fromUser = xml.find('FromUserName').text
		toUser = xml.find('ToUserName').text
		msg = u'我现在还在开发中，还没有什么功能，您刚才说的是：' + content
		response = make_response(xml_text % (toUser, fromUser, str(int(time.time())), msg))
		response.content_type='application/xml'
		return response
	return '无消息返回'