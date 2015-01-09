# coding: utf-8
import os
import re

DEBUG = True
TESTING = True

TOKEN = 'prettystory'

MSG_TEXT_TPL = """<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>"""

ERROR_TEXT = u'公众号处于研发阶段，不能自动回复您的消息，请等待开发者回复。'
ERROR_SONG = u'很抱歉，没有这首歌曲'

RULE = r'歌词'

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = ROOT_FOLDER + '/templates/'
STATIC_FOLDER = ROOT_FOLDER + '/static/'