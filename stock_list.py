from ftplib import FTP

#read stocks from nasdaq ftp
def read_stocks(save_name):
	ftp_server = "ftp.nasdaqtrader.com"
	ftp = FTP(ftp_server)
	ftp.login()
	ftp.cwd('SymbolDirectory')
	ftp.retrbinary('RETR nasdaqlisted.txt', open(save_name, 'wb').write)
	ftp.quit()

#create list of company dictionaries
#[{symbol: '', name: ''}, {}, ..]
def create_stock_list(filename):
	#read files
	f = open(filename, 'r')
	text = f.read()
	lines = text.split('\n')
	del lines[0]
	del lines[-1]
	del lines[-1]

	#add to list
	stock_list = []
	for line in lines:
		entry = {}
		data = line.split('|')
		
		entry['symbol'] = data[0]
		name = data[1]
		name = name.split('-')
		if len(name) > 1:
			entry['name'] = name[0]

		stock_list.append(entry)

	return stock_list



if __name__ == "__main__":
	pass
	#read_stocks(file_nasdaq)
	#stocks = create_stock_list(file_nasdaq)
	#print stocks