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
### Status: Beta
Need more features. Current commit only returns the price and rank. Going to be working on scraping more specific data.
```
[*] Selected coin: cardano
[*] Date and time: 13/06/2021 02:19:30
[*] Coin: Cardano
[*] Current Price: $1.44
[*] Rank: Rank #5
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
