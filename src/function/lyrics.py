# coding: utf-8
import re
from requests import get

ERROR_SONG = u'很抱歉，找不到这首歌曲'

human_headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
	'Accept-Encoding':'gzip,deflate,sdch'
}


class Lyrics(object):
	def __init__(self, song, singer=None):
		self.song = song
		if singer is None:
			self.singer = ''
		else:
			self.singer = singer

	def find(self):
		url = 'http://music.baidu.com/search/lrc?from=new_mp3&key=%s+%s' % (self.song, self.singer)
		html = get(url, headers=human_headers, ).text
		text = self.extract(html)
		return text

	def extract(self, page):
		text = re.search(r'<p id="lyricCont-0">([\S\s]*?)</p>', page)
		if text is None:
			return ERROR_SONG
		else:
			text = text.group(1)
			text = re.sub(r'[ <em>br/]', '', text)
			return text

def main():
	do = Lyrics('存在', '')
	print do.find()

if __name__ == '__main__':
	main()