import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

		
def get_other(): #scrape news, market cap, other data from coindesk
	URL = f"https://www.coindesk.com/price/{name}"
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	news = []
	for div in soup.findAll('div', class_="card-text-block"):
		for h2 in div.findAll('h2', class_="heading"):
			for i in range(1):
				a = h2.find('a')
				for index in range(1):
					b = a.find('a')
					news_val = a.get_text()
					news.append(news_val)

	market = []
	for a in soup.findAll('div', class_="coin-info-list price-list"):
		for d in a.findAll('div', class_="coin-info-block"):
			for e in d.findAll('div', class_="data-definition"):
				for f in e.findAll('div', class_="price-medium"):
					val = f.get_text()
					market.append(val)
					market_cap = market[0]

	print("[*] Market Cap: "+ market_cap)
	print("[*] Latest news: "+ news[0] + f"\n[*] Source: https://www.coindesk.com/price/{name}")
	

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
 *		v1.1 
 *		@Author: prodseanb
 *		@GitHub: https://github.com/prodseanb
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
	get_other()

if __name__ == "__main__":
	try:
		name = sys.argv[1]
		request = requests.get(f'https://coinmarketcap.com/currencies/{name}')
		if request.status_code == 200: # check if url exists
			get_coin(name)
		else:
			print('[!] Coin not found.')
			raise IndexError
	except IndexError: # put a short documentation here
		print('''
CryptoCheck v1.1 (https://github.com/prodseanb/cryptocheck)
	Keep track of the latest cryptocurrency data with CryptoCheck.
Usage:	python3 cryptocheck.py [coin-name]
	Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
Examples:
		
	python3 cryptocheck.py shiba-inu
	python3 cryptocheck.py bitcoin
	python3 cryptocheck.py cardano
			''')
	except UnboundLocalError:
		print(f"[!] No news found. Please check https://coinmarketcap.com/currencies/{name}/") 

#Add more options/argv capabilities
#scrape 24h volume
#scrape circulating supply