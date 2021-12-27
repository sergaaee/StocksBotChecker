import requests




# getting data about ton
def get_ton():
    url = 'https://ftx.com/api/markets'
    r = requests.get(url)
    result = r.json()['result']
    ton = coin(
               price=result[570]['price'], change1h=round(result[570]['change1h'], 4) * 100,
               change24h=round(result[570]['change24h'], 4) * 100)
    return ton




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
