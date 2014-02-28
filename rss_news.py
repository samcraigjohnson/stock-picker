import feedparser
import urllib
from os import listdir
from bs4 import BeautifulSoup

feed_dir = "./feeds/"
text_dir = "./feeds_text/"

#read list of feeds
def read_feeds(filename):
	feeds = open(filename, 'r')
	feeds = feeds.read().split('\n')
	return feeds


#get all feeds given feed filename
def write_feeds(filename):
	feeds = read_feeds(filename)
	count = 0
	for feed in feeds:
		parsed = feedparser.parse(feed)
		entries = parsed.entries
		print '## ' + feed + ' ##'
		for entry in entries:
			feed_write = open(feed_dir+'story_'+str(count), 'w')
			content = urllib.urlopen(entry['link']).read()
			feed_write.write(content)
			count += 1

#translate the feeds into just the news stories
def translate_html():
	for f in listdir(feed_dir):
		doc_html = open(feed_dir+f, 'r').read()
		write_doc = open(text_dir+f+'.txt', 'w')
		soup = BeautifulSoup(doc_html)
		article_text = soup.find("div", id="articleText")
		write_doc.write(article_text.get_text().encode('utf-8'))