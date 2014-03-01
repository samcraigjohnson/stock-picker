import rss_news as RSS
import stock_list as STOCKS
import file_sentiment as SENT
import hist_data as HIST

from Tkinter import *
import operator

feed_loc = "./setup/rss_feeds.txt"

#RSS.write_feeds(feed_loc)
RSS.translate_html()
#SENT.get_sentences()
#HIST.get_close_change(stock)
#HIST.get_adj_change(stock)
#word_vals = SENT.value_words()

#sorted_words = sorted(word_vals.iteritems(), key=lambda data: data[1][0])

#for word in sorted_words:
	#print word


#Draw Clusters
'''
master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

w.create_line(0, 0, 200, 100)

mainloop()'''