# coding: utf-8
import re
from requests import get

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
		return html

	def extract(self):
		page = self.find()
		text = re.search(r'<p id="lyricCont-0">([\S\s]*?)</p>', page).group(1)
		return text

	def filter(self):
		text = self.extract()
		text = re.sub(r'[ <em>br/]', '', text)
		return text

	def verify(self, text):
		pass



def main():
	do = Lyrics('听说爱情回来过', '张敬轩')
	print do.filter()

if __name__ == '__main__':
	main()