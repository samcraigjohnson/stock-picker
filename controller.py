import rss_news as RSS
import stock_list as STOCKS
import file_sentiment as SENT
feed_loc = "./setup/rss_feeds.txt"


#RSS.write_feeds(feed_loc)
#RSS.translate_html()
#SENT.get_sentences()
SENT.identify_symbols()