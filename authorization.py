from binance.client import Client

class Authorization:

    def __init__(self):
        self.key = ''
        self.secret = ''

    def getClient(self):
        self.client = Client(self.key, self.secret)
        return self.client