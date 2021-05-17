from binance.client import Client
from authorization import Authorization

class Coins:

    def __init__(self):
        autorization = Authorization()

        self.client = autorization.getClient()
        info = self.client.get_all_tickers()
        self.ar = []
        for coin in info:
            self.ar.append(coin["symbol"])

    def getCoins(self):
        return self.ar