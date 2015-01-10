# coding: utf-8
import re
import time
import hashlib
from src.function import Lyrics
from src.settings import TOKEN, MSG_TEXT_TPL, ERROR_TEXT, RULE
from lxml import etree
from flask import render_template, Blueprint, request
from flask import make_response, redirect, url_for

bp = Blueprint('wechat', __name__)


@bp.route('/', methods=['GET'])
def wechat_access_verify():
	echostr = request.args.get('echostr', '')
	if verification(request):
		return echostr
	return 'something wrong'

@bp.route('/', methods=['POST'])
def wechat_msg():
	data = request.data
	msg = parse_msg(data)
	text = msg['Content'].encode('utf-8').replace('：', ':')
	reply = re.search(RULE, text)
	if reply.group(1):
		response = get_lyrics(msg)
		return response
	return reply_text(msg, ERROR_TEXT)


def verification(request):
	token = TOKEN
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

def parse_msg(data):
	root = etree.fromstring(data)
	args = {}
	for child in root:
		args[child.tag] = child.text
	return args

def reply_text(msg, content):
	text = MSG_TEXT_TPL % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content)
	return text


def get_lyrics(msg):
	text = msg['Content'].encode('utf-8').replace('：', ':')
	song = re.search(r'[:](.*?) |[:](.*?)$', text)
	if song.group(1) is None:
		song = song.group(2)
	else:
		song = song.group(1)
	singer = re.search(r' (.*?)$', text)
	if singer is None:
		singer = ''
	else:
		singer = singer.group(1)
	lyrics = Lyrics(song, singer).find()
	return reply_text(msg, lyrics)