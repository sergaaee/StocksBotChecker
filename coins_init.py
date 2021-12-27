import requests


class coin:
    def __init__(self, baseCurrency, quoteCurrency, price, change1h, change24h):
        self._baseCurrency = baseCurrency
        self._quoteCurrency = quoteCurrency
        self._price = price
        self._change1h = change1h
        self._change24h = change24h

    @property
    def baseCurrency(self):
        return self._baseCurrency

    @property
    def quoteCurrency(self):
        return self._quoteCurrency

    @property
    def price(self):
        return self._price

    @property
    def change1h(self):
        return str(self._change1h) + "%"

    @property
    def change24h(self):
        return str(self._change24h) + "%"


url = 'https://ftx.com/api/markets'
r = requests.get(url)
result = r.json()['result']


def get_btc():
    url = 'https://ftx.com/api/markets'
    r = requests.get(url)
    result = r.json()['result']
    btc = coin(baseCurrency=result[150]['baseCurrency'], quoteCurrency=result[150]['quoteCurrency'],
               price=result[150]['price'], change1h=round(result[150]['change1h'], 4) * 100,
               change24h=round(result[150]['change24h'], 4) * 100)
    return btc

def get_eth():
    url = 'https://ftx.com/api/markets'
    r = requests.get(url)
    result = r.json()['result']
    eth = coin(baseCurrency=result[260]['baseCurrency'], quoteCurrency=result[260]['quoteCurrency'],
               price=result[260]['price'], change1h=round(result[260]['change1h'], 4) * 100,
               change24h=round(result[260]['change24h'], ) * 100)
    return eth

def get_ton():
    url = 'https://ftx.com/api/markets'
    r = requests.get(url)
    result = r.json()['result']
    ton = coin(baseCurrency=result[570]['baseCurrency'], quoteCurrency=result[570]['quoteCurrency'],
               price=result[570]['price'], change1h=round(result[570]['change1h'], 4) * 100,
               change24h=round(result[570]['change24h'], 4) * 100)
    return ton


# pos=0
# for answer in result:
# pos += 1
# print(answer['name'])
# if answer['name'] == "TORN/USD":
# print(pos-1)
# break
