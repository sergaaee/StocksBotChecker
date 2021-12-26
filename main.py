import requests

url = 'https://ftx.com/api/markets'
r = requests.get(url)
result = r.json()['result']


print(result[0]['name'])

class coin:
    def __init__(self, coin_name, coin_quote, price, change1h, change24h):
        self._coin_name = coin_name
        self._coin_quote = coin_quote
        self._price = price
        self._change1h = change1h
        self._change24h = change24h

    @property
    def coin_name(self):
        return self._coin_name

    @property
    def coin_quote(self):
        return self._coin_quote()

    @property
    def price(self):
        return self._price

    @property
    def change1h(self):
        return self._change1h

    @property
    def change24h(self):
        return self._change24h

ton = coin(coin_name='', coin_quote='', price='', change1h='', change24h='')



#for answer in result:
    #if answer['name'] == "TONCOIN/USD":
        #print(answer)
        #break
