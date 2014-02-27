import urllib
import stock_list

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
dest = "./old_data/"
file_nasdaq = "nas_stocks.txt"

def get_old_data(symb):
	url = base_url + symb
	file_name = dest + symb + '.csv'
	try:
		urllib.urlretrieve(url, file_name)

	except urllib.ContentTooShortError as e:
		outfile = open(file_name, "w")
		outfile.write(e.content)
		outfile.close()

def get_all_data():
	stocks = stock_list.create_stock_list(file_nasdaq)
	for stock in stocks:
		get_old_data(stock['symbol'])

if __name__ == '__main__':
	get_all_data()