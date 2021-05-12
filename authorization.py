from binance.client import Client

class Authorization:

    def __init__(self):
        self.key = 'VsOPwaX5WLqmQc9838POWs0Kb46DlZpDyDiM9YKXin1svjXZ5SN40BimuotO8VRA'
        self.secret = 'rCNQPaX6arDfMXVrGJ2JHALq7j1Xej4Y6ezosQkoEIgabkkxWUOAtTcyXlGf7Z31'

    def getClient(self):
        self.client = Client(self.key, self.secret)
        return self.client