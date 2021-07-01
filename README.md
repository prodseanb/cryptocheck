# cryptocheck
[![Generic badge](https://img.shields.io/badge/fork-🔱-<COLOR>.svg)](https://github.com/prodseanb/cryptocheck/fork)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/prodseanb/cryptocheck/blob/master/LICENSE)
[![Generic badge](https://img.shields.io/badge/follow-LinkedIn-<COLOR>.svg)](https://www.linkedin.com/in/sean-bachiller-40b63417b/)
[![Generic badge](https://img.shields.io/badge/follow-Twitter-<COLOR>.svg)](https://twitter.com/prodseanb)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://github.com/prodseanb/cryptocheck/blob/master/cryptocheck.py)
<br />
```
/***
 *     ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
 *    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
 *    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██║     ███████║█████╗  ██║     █████╔╝ 
 *    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
 *    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
 *     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
 *
 *    v1.4      
 *    @Author: prodseanb
 *    @GitHub: https://github.com/prodseanb
 */
```
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) <br />
Keep track of the latest cryptocurrency data with CryptoCheck.
### Usage
```bash
python3 run.py [coin-name] [*args]
```
`argv[1]` must refer to the coin name, converts this argument into a part of the URL to be parsed by [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).
```bash
URL = f"https://coinmarketcap.com/currencies/{sys.argv[1]}"
```
Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
```
CryptoCheck v1.4 (https://github.com/prodseanb/cryptocheck)
    Keep track of the latest cryptocurrency data with CryptoCheck.
Usage:  python3 run.py [coin-name] [*args]
    Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
Output:
    python3 cryptocheck.py [coin-name] [optional-arg]
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
```
### v1.0
- Coin price
- Rank
### v1.1
Planning to add more features. v1.1 commit:
- Market cap
- Latest news  
- Documentation
### v1.2
- 24h low/high
- 24h trading volume
- Circulating supply
### v1.3
- 24h price change
- Market dominance
- Optional arguments
### v1.4
- Utilize multiple arguments e.g. `python3 run.py bitcoin -M -p -K`
```
[*] Date and time: 14/06/2021 16:18:10
[*] Coin: Ethereum
[*] Abbrv: (ETH)
[*] Current price: $2,545.63
[*] Rank: Rank #2
[24h] Low: $2,469.39  ------------------  [24h] High: $2,606.43
[24h] Trading volume: $28,941,341,401
[24h] Price change: $60.43
[*] Market dominance: 18.27%
[*] Circulating supply: 116,290,438.81 ETH
[*] Market cap: $296,032,541,530
[*] Latest news: Bitcoin and Ether Price Indicators Support Near-Term ‘Relief Rally’ 
[*] Source: https://www.coindesk.com/price/ethereum
```
### Run on Docker
Make sure you have Docker installed. `docker -v` to check. 
```bash
sudo docker pull prodseanb/cryptocheck
sudo docker run -t -i prodseanb/cryptocheck [coin-name] [*args]
```
### License
[MIT License](https://github.com/prodseanb/cryptocheck/blob/master/LICENSE)

Copyright (c) 2021 Sean Bachiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
