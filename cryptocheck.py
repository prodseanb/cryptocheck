import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime


def get_market_cap(): #fix this function
	URL = f"https://www.coindesk.com/price/{name}"
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	market = []
	for a in soup.findAll('div', class_="coin-info-list price-list"):
		for d in a.findAll('div', class_="coin-info-block"):
			for e in d.findAll('div', class_="data-definition"):
				for f in e.findAll('div', class_="price-medium"):
					val = f.get_text()
					market.append(val)
					market_cap = market[0]
					market_cap_val = market_cap
					#print(market_cap_val)
					#issue#1 -- list print twice

def get_coin(name):
	URL = f"https://coinmarketcap.com/currencies/{name}"
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	#scrape coin name 
	coin = []
	print(f'[*] Selected coin: {name}')
	# sc-1q9q90x-0 iYFMbU h1___3QSYG -- h2 class
	for h2 in soup.findAll('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG"):
		small = h2.find('small') # unwanted small tag
		small.extract()
		coin_name = h2.get_text()
		coin.append(coin_name)
		#print(coin)

	#scrape abbrv
	abbrv = []
	for h1 in soup.findAll('h1', class_="priceHeading___2GB9O"):
		for small in h1.findAll('small'):
			abbrv_val = small.get_text()
			abbrv.append(abbrv_val)

	#scrape price
	price = []
	for p in soup.findAll('div', class_="priceValue___11gHJ"):
		price_val = p.get_text()
		price.append(price_val)
		#print(price)

	#scrape market cap
	#get_market_cap() -- fix issue#1

	#scrape rank
	rank = []
	for rank in soup.findAll('div', class_="namePill___3p_Ii namePillPrimary___2-GWA"):
		rank_val = rank.get_text()
		rank.append(rank_val)

	print('''
/***
 *     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
 *    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
 *    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║     ███████║█████╗  ██║     █████╔╝ 
 *    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
 *    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
 *     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
 *                                                                                               
 */
		''')
	#check date and time
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	print(f"[*] Date and time: {dt_string}")
	#Output
	for index, (val1, val2, val3, val4) in \
	enumerate(zip(coin, abbrv, price, rank)):
			print(f"[*] Coin: {val1}\n[*] Abbrv: {val2}\n[*] Current Price: {val3}\n[*] Rank: {val4}")
if __name__ == "__main__":
	try:
		name = sys.argv[1]
		get_coin(name)
	except IndexError: # put a short documentation here
		print("fail")
	