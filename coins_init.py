import requests

url = 'https://ftx.com/api/markets'
r = requests.get(url)
result = r.json()['result']



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


ton = coin(baseCurrency=result[570]['baseCurrency'], quoteCurrency=result[570]['quoteCurrency'], price=result[570]['price'], change1h=round(result[570]['change1h'], 3)*100, change24h=round(result[570]['change24h'], 3)*100)
print(ton.baseCurrency, ton.quoteCurrency, ton.price, ton.change1h, ton.change24h)

btc = coin(baseCurrency=result[150]['baseCurrency'], quoteCurrency=result[150]['quoteCurrency'], price=result[150]['price'], change1h=round(result[150]['change1h'], 3)*100, change24h=round(result[150]['change24h'], 3)*100)
print(btc.baseCurrency, btc.quoteCurrency, btc.price, btc.change1h, btc.change24h)

eth = coin(baseCurrency=result[260]['baseCurrency'], quoteCurrency=result[260]['quoteCurrency'], price=result[260]['price'], change1h=round(result[260]['change1h'], 3)*100, change24h=round(result[260]['change24h'], 3)*100)
print(eth.baseCurrency, eth.quoteCurrency, eth.price, eth.change1h, eth.change24h)

pos=0
#for answer in result:
    #pos += 1
    #print(answer['name'])
    #if answer['name'] == "TORN/USD":
        #print(pos-1)
       # break
