import requests
from decimal import *


class coin:
    def __init__(self, price, change1h, change24h):
        self._price = price
        self._change1h = change1h
        self._change24h = change24h

    @property
    def price(self):
        return self._price

    @property
    def change1h(self):
        return str(self._change1h) + "%"

    @property
    def change24h(self):
        return str(self._change24h) + "%"


# getting data about ton
def get_ton():
    url = 'https://ftx.com/api/markets'
    r = requests.get(url)
    result = r.json()['result']
    id = 0
    for i in result:
        id += 1
        if i['name'] == "TONCOIN/USD":
            break
    getcontext().prec = 3
    change_1h = Decimal(result[id - 1]['change1h']) * 100
    change_24h = Decimal(result[id - 1]['change24h']) * 100
    ton = coin(
               price=result[id - 1]['price'], change1h=change_1h,
               change24h=change_24h)
    return ton







