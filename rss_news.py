import feedparser


def read_feeds(filename):
	feeds = open(filename, 'r')
	feeds = feeds.read().split('\n')
	return feeds


def list_titles(filename):
	feeds = read_feeds(filename)

	for feed in feeds:
		parsed = feedparser.parse(feed)
		entries = parsed.entries
		print '## ' + feed + ' ##'
		for entry in entries:
			print entry.title

if __name__ == '__main__':
	list_titles('rss_feeds.txt')