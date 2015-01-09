# coding: utf-8
import os

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

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = ROOT_FOLDER + '/templates/'
STATIC_FOLDER = ROOT_FOLDER + '/static/'