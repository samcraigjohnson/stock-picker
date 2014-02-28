import urllib
import stock_list

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
dest = "./old_data/"
file_nasdaq = "./setup/nas_stocks.txt"

#get csv of all prices of given symbol
def get_old_data(symb):
	url = base_url + symb
	file_name = dest + symb + '.csv'
	try:
		urllib.urlretrieve(url, file_name)

	except urllib.ContentTooShortError as e:
		outfile = open(file_name, "w")
		outfile.write(e.content)
		outfile.close()

#get every csv from yahoo of nasdaq
def get_all_data():
	stocks = stock_list.create_stock_list(file_nasdaq)
	for stock in stocks:
		get_old_data(stock['symbol'])
