import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime
import platform
import subprocess


news = []
def get_news(): #scrape news from coindesk
	URL = f"https://www.coindesk.com/price/{name}"
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	
	for div in soup.findAll('div', class_="card-text-block"):
		for h2 in div.findAll('h2', class_="heading"):
			for i in range(1):
				a = h2.find('a')
				for index in range(1):
					b = a.find('a')
					news_val = a.get_text()
					news.append(news_val)
	
def get_coin(name, arg2=None):
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

	# 24 low/high value
	low_high = []
	for span in soup.findAll('span', class_="highLowValue___GfyK7"):
		val = span.get_text()
		low_high.append(val)

	# circulating supply, volume, market cap
	supply = []
	for div in soup.findAll('div', class_="statsValue___2iaoZ"):
		val = div.get_text()
		supply.append(val)

	# 24h price change, market dominance
	price_change = []
	for table in soup.findAll('table'):
		for td in table.findAll('td'):
			for span in td.findAll('span'):
				val = span.get_text()
				price_change.append(val)

	print('''
/***
 *     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
 *    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
 *    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║     ███████║█████╗  ██║     █████╔╝ 
 *    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
 *    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
 *     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
 *
 *		v1.3 
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
	# optional args
	arg_price = ['-p', '--price']
	arg_change = ['-c', '--price-change']
	arg_volume = ['-tv', '--volume']
	arg_low_high = ['-lh', '--low-high']
	arg_dominance = ['-d', '--dominance']
	arg_supply = ['-s', '--supply']
	arg_market_cap = ['-mc', '--market-cap']
	arg_news = ['-n', '--news']
	# display all
	if arg2 == "-a" or arg2 == None:
		for index, (val1, val2, val3, val4) in \
		enumerate(zip(coin, abbrv, price, rank)):
				print(f"[*] Coin: {val1}\n[*] Abbrv: {val2}\n[*] Current price: {val3}\n[*] Rank: {val4}")

		print("[24h] Low: " + low_high[0] + "  ------------------  [24h] High: " + low_high[1])
		print("[24h] Trading volume: " + supply[2])
		print("[24h] Price change: " + price_change[0])
		print("[*] Market dominance: " + price_change[6])
		print("[*] Circulating supply: " + supply[4])
		print("[*] Market cap: "+ supply[0])
		get_news()
		if len(news) == 0:
			print(f'[!] News not found. Please check https://coinmarketcap.com/currencies/{name}/')
		else:
			print("[*] Latest news: "+ news[0] + f"\n[*] Source: https://www.coindesk.com/price/{name}")
	# display current price
	elif arg2 in arg_price:
		print("[*] Current price: " + price[0])
	# display price change
	elif arg2 in arg_change:
		print("[24h] Price change: " + price_change[0])
	# display trading volume
	elif arg2 in arg_volume:
		print("[24h] Trading volume: " + supply[2])
	# display 24h low/high
	elif arg2 in arg_low_high:
		print("[24h] Low: " + low_high[0] + "  ------------------  [24h] High: " + low_high[1])
	# display market dominance
	elif arg2 in arg_dominance:
		print("[*] Market dominance: " + price_change[6])
	# display supply
	elif arg2 in arg_supply:
		print("[*] Circulating supply: " + supply[4])
	# display market cap
	elif arg2 in arg_market_cap:
		get_news()
		print("[*] Market cap: "+ supply[0])
	elif arg2 in arg_news:
		get_news()
		print("[*] Latest news: "+ news[0] + f"\n[*] Source: https://www.coindesk.com/price/{name}")

if __name__ == "__main__":
	try:
		name = sys.argv[1]
		request = requests.get(f'https://coinmarketcap.com/currencies/{name}')
		if request.status_code == 200: # check if url exists
			if platform.system() == "Windows":
				subprocess.call('cls', shell=True)
			else:
				subprocess.call('clear', shell=True)

			# handle optional arguments
			try:
				arg2 = sys.argv[2]
			except IndexError:
				arg2 = None
				
			if arg2 == None:
				get_coin(name)
			else:
				get_coin(name, arg2)
	
		else:
			print('[!] Coin not found.')
			raise IndexError
	except IndexError: # put a short documentation here
		print('''
CryptoCheck v1.3 (https://github.com/prodseanb/cryptocheck)
	Keep track of the latest cryptocurrency data with CryptoCheck.
Usage:	python3 cryptocheck.py [coin-name]
	Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
Output:
	python3 cryptocheck.py [coin-name] [optional-arg]
	Maximum of 2 parameters: currency name and display option
	-a: Display all the results (optional, defaults to None when not used)
	-p / --price: Display the current price
	-c / --price-change: Display the 24h price change
	-tv / --volume: Display the 24h trading volume
	-lh / --low-high: Display the 24h low/high
	-d / --dominance: Display the market dominance
	-s / --supply: Display the circulating supply
	-mc / --market-cap: Display the market cap
	-n / --news: Display the latest news
Examples:
	Try executing these examples.	
	python3 cryptocheck.py dogecoin -a
	python3 cryptocheck.py bitcoin --news
	python3 cryptocheck.py cardano -mc
			''')
	except UnboundLocalError:
		print(f"[!] No news found. Please check https://coinmarketcap.com/currencies/{name}/") 
#v1.3 -- 24h price change, market dominance, optional args