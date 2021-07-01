import sys
import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime
import platform
import subprocess
import csv
import banner as banner

news = []
coin = []  # scrape coin name
abbrv = []  # scrape abbrv
price = []  # scrape price
rank = []
low_high = []
supply = []  # circulating supply, volume, market cap
price_change = []


def get_news():  # scrape news from coindesk
    URL = f"https://www.coindesk.com/price/{sys.argv[1]}"
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


def main(*arguments):
    URL = f"https://coinmarketcap.com/currencies/{sys.argv[1]}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')

    print(f'[*] Selected coin: {sys.argv[1]}')
    # sc-1q9q90x-0 iYFMbU h1___3QSYG -- h2 class
    for h2 in soup.findAll('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG"):
        small = h2.find('small')  # unwanted small tag
        small.extract()
        coin_name = h2.get_text()
        coin.append(coin_name)
        # print(coin)

    for h1 in soup.findAll('h1', class_="priceHeading___2GB9O"):
        for small in h1.findAll('small'):
            abbrv_val = small.get_text()
            abbrv.append(abbrv_val)

    for p in soup.findAll('div', class_="priceValue___11gHJ"):
        price_val = p.get_text()
        price.append(price_val)
        # print(price)

    for rank in soup.findAll('div', class_="namePill___3p_Ii namePillPrimary___2-GWA"):
        rank_val = rank.get_text()
        rank.append(rank_val)

    for span in soup.findAll('span', class_="highLowValue___GfyK7"):
        val = span.get_text()
        low_high.append(val)

    for div in soup.findAll('div', class_="statsValue___2iaoZ"):
        val = div.get_text()
        supply.append(val)

    for table in soup.findAll('table'):
        for td in table.findAll('td'):
            for span in td.findAll('span'):
                val = span.get_text()
                price_change.append(val)

    banner.head()
    # check date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"[*] Date and time: {dt_string}")

    # Output
    # optional args
    '''
    all_args = ['-p', '--price', '-a', '-c', '--price-change',
    '-T', '--volume', '-K', '--low-high', '-d', '--dominance',
    '-s', '--supply', '-M', '--market-cap', '-n', '--news']
    '''

    if len(sys.argv) == 2 or '-a' in sys.argv[1:]:
        for index, (val1, val2, val3, val4) in \
                enumerate(zip(coin, abbrv, price, rank)):

            print(
                f"[*] Coin: {val1}\n[*] Abbrv: {val2}\n[*] Current price: {val3}\n[*] Rank: {val4}")

        print("[24h] Low: " + low_high[0] +
              "  ------------------  [24h] High: " + low_high[1])
        print("[24h] Trading volume: " + supply[2])
        print("[24h] Price change: " + price_change[0])
        print("[*] Market dominance: " + price_change[6])
        print("[*] Circulating supply: " + supply[4])
        print("[*] Market cap: " + supply[0])
        get_news()
        if len(news) == 0:
            print(
                f'[!] News not found. Please check https://coinmarketcap.com/currencies/{sys.argv[1]}/')
        else:
            print("[*] Latest news: " + news[0] +
                  f"\n[*] Source: https://www.coindesk.com/price/{sys.argv[1]}")
    if '-p' in sys.argv[1:] or '--price' in sys.argv:
        print("[*] Current price: " + price[0])
    if '-c' in sys.argv[1:] or '--price-change' in sys.argv[1:]:
        print("[24h] Price change: " + price_change[0])
    if '-T' in sys.argv[1:] or '--volume' in sys.argv[1:]:
        print("[24h] Trading volume: " + supply[2])
    if '-K' in sys.argv[1:] or '--low-high' in sys.argv[1:]:
        print("[24h] Low: " + low_high[0] +
              "  ------------------  [24h] High: " + low_high[1])
    if '-d' in sys.argv[1:] or '--dominance' in sys.argv[1:]:
        print("[*] Market dominance: " + price_change[6])
    if '-s' in sys.argv[1:] or '--supply' in sys.argv[1:]:
        print("[*] Circulating supply: " + supply[4])
    if '-M' in sys.argv[1:] or '--market-cap' in sys.argv[1:]:
        get_news()
        print("[*] Market cap: " + supply[0])
    if '-n' in sys.argv[1:] or '--news' in sys.argv[1:]:
        get_news()
        print("[*] Latest news: " + news[0] +
              f"\n[*] Source: https://www.coindesk.com/price/{sys.argv[1]}")


if __name__ == "__main__":

    try:
        args = sys.argv
        request = requests.get(
            f'https://coinmarketcap.com/currencies/{sys.argv[1]}')
        if request.status_code == 200:  # check if url exists
            if platform.system() == "Windows":
                subprocess.call('cls', shell=True)
            else:
                subprocess.call('clear', shell=True)
            main(args)
        else:
            print('[!] Coin not found.')
            banner.usage()
    except IndexError:
        banner.usage()
    except UnboundLocalError:
        print(
            f"[!] No news found. Please check https://coinmarketcap.com/currencies/{sys.argv[1]}/")
