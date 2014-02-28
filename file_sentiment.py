import nltk.data
import stock_list as SL
from os import listdir
text_dir = "./feeds_text/"

def get_sentences():
	sent_dectect = nltk.data.load('tokenizers/punkt/english.pickle')
	all_sents = []
	for f in listdir(text_dir):
		text = open(text_dir+f, 'r').read()
		sent_list = sent_dectect.tokenize(text.strip())
		all_sents.extend(sent_list)
	return all_sents

def identify_symbols():
	sents = get_sentences()
	stocks = SL.create_symbol_list()
	for sent in sents:
		words = sent.split()
		for word in words:
			word = word.strip('()\n')
			if word in stocks:
				print "found stock: ", word