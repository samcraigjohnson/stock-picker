import nltk.data
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords

import time
import stock_list as SL
import hist_data as HIST
from os import listdir


text_dir = "./feeds_text/"
punc = [',', '*', '(', ')', '!', '@', '#', '$', '%', '^', '&', ':']
remove_words = ["corporation", "corp.", "inc.", "incorporated", "systems", "international", "ltd.", "ltd", "limited"]
stocks = SL.create_stock_list()


def get_sentences():
	sent_dectect = nltk.data.load('tokenizers/punkt/english.pickle')
	all_sents = []
	for f in listdir(text_dir):
		text = open(text_dir+f, 'r').read()
		sent_list = sent_dectect.tokenize(text.strip())
		all_sents.extend(sent_list)
	return all_sents

def get_stock_info():
	sents = get_sentences()
	found_stocks = []
	stock_data = {}

	for sent in sents:
		words = PunktWordTokenizer().tokenize(sent)
		filt_words = [w for w in words if not (w.lower() in stopwords.words('english') or w in punc)]
		found = stock_in_senctence(filt_words)

		#for every stock found append list of words
		if len(found) > 0:
			for s in found:
				if not s in stock_data:
					stock_data[s] = []
				stock_data[s].extend(filt_words)


	return stock_data

#returns a list of stocks found in the sentance
def stock_in_senctence(filt_words):
	stocks_found = []
	
	for s in stocks:
		symb = s['symbol']
		name = s['name']
		name = name.split()
		if symb in filt_words and not symb in stocks_found:
			stocks_found.append(symb)
		else:
			count_name = len(name)
			for n in name:
				if n.lower() in remove_words or n in filt_words:
					count_name -= 1

			if count_name == 0 and not symb in stocks_found:
				stocks_found.append(symb)


	return stocks_found


#returns a dictonary of words where word : (frequency, change)
def value_words():
	data = get_stock_info()
	word_dict = {} #eventually will be pickled and added to
	for s in data:
		p_change = HIST.get_adj_change(s)
		words = data[s]
		for word in words:
			word = word.lower()
			if not word in word_dict:
				word_dict[word] = [0,0]

			word_dict[word][0] += 1
			word_dict[word][1] += p_change

	return word_dict