def head():
    	print('''
/***
 *     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
 *    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
 *    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║     ███████║█████╗  ██║     █████╔╝ 
 *    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
 *    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
 *     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
 *
 *		v1.4 
 *		@Author: prodseanb
 *		@GitHub: https://github.com/prodseanb
 *                                                                                              
 */
		''')

def usage():
    		print('''
CryptoCheck v1.4 (https://github.com/prodseanb/cryptocheck)
	Keep track of the latest cryptocurrency data with CryptoCheck.
Usage:	python3 run.py [coin-name] [*args]
	Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
Output:
	python3 run.py [coin-name] [*args]
	Maximum of 2 parameters: currency name and display option
	-a: Display all the results (optional, defaults to None when not used)
	-p / --price: Display the current price
	-c / --price-change: Display the 24h price change
	-T / --volume: Display the 24h trading volume
	-K / --low-high: Display the 24h low/high
	-d / --dominance: Display the market dominance
	-s / --supply: Display the circulating supply
	-M / --market-cap: Display the market cap
	-n / --news: Display the latest news
Examples:
	Try executing these examples.	
	python3 run.py dogecoin -a
	python3 run.py bitcoin --news -p
	python3 run.py cardano -M
			''')