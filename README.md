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
 *    v1.2      
 *    @Author: prodseanb
 *    @GitHub: https://github.com/prodseanb
 */
```
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) <br />
Keep track of the latest cryptocurrency data with CryptoCheck.
### Usage
```bash
python3 cryptocheck.py [coin-name]
```
`argv[1]` must refer to the coin name, converts this argument into a part of the URL to be parsed by [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).
```bash
URL = f"https://coinmarketcap.com/currencies/{name}"
```
Appends [coin-name] argument to URL. Make sure multiple-word coins are separated by a "-" hyphen.
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
```
[*] Date and time: 13/06/2021 23:16:01
[*] Coin: Dogecoin
[*] Abbrv: (DOGE)
[*] Current Price: $0.3236
[*] Rank: Rank #6
[24h] Low: $0.3079  ------------------  [24h] High: $0.33
[24h] Trading volume: $1,547,795,850
[*] Circulating supply: 130.01B DOGE
[*] Market Cap: $42.08B
[*] Latest news: No DOGE Allowed? Thai SEC Bans Meme, Fan and Exchange Tokens as Well as NFTs 
[*] Source: https://www.coindesk.com/price/dogecoin
```
### Don't forget to install the requirements...
```bash
pip3 -r install requirements.txt
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
