from authorization import Authorization
import numpy as np
import talib as tb

class Indicators:

    def __init__(self, criptopara):
        try:
            autorization = Authorization()
            self.client = autorization.getClient()
        except Exception as e:
            print("Exception autorization: {0}".format(e))

        self.symbol = str(criptopara)

        try:
            orders = self.client.get_order_book(symbol=self.symbol)
            # print(orders)
            self.lastBid = float(orders['bids'][0][0])
            self.lastAsk = float(orders['asks'][0][0])
        except Exception as e:
            print("Exception init: {0}".format(e))

    def spreadPerc(self):
        try:
            res =  str((self.lastAsk / self.lastBid - 1) * 100.0)
            return res
        except Exception as e:
            print("Exception spreadPerc: {0}".format(e))
            return "0"


    def get_history(self):

        try:
            arrHistory = list()
            klines = self.client.get_historical_klines(self.symbol, self.client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
            for value in klines:
                arrHistory.append(value[1])

            return arrHistory

        except Exception as e:
            print("Exception get_history: {0}".format(e))
            return "0"

    def macd(self):
        try:
            prices = np.asarray(self.get_history(), dtype=float)
            EMA12 = tb.EMA(prices, timeperiod=12)
            EMA26 = tb.EMA(prices, timeperiod=26)

            return np.format_float_positional(round(EMA12[-1], 10) - round(EMA26[-1], 10))
        except Exception as e:
            print("Exception macd: {0}".format(e))
            return "0"

    def rsi(self):
        try:
            rsi = tb.RSI(np.asarray(self.get_history(), dtype=float))
            return np.format_float_positional(round(rsi[-1], 10))
        except Exception as e:
            print("Exception rsi: {0}".format(e))
            return "0"

    def volume(self):
        try:
            volume = self.client.get_klines(symbol=self.symbol, interval=self.client.KLINE_INTERVAL_30MINUTE)
            return str(volume[-1][5])
        except Exception as e:
            print("Exception: {0}".format(e))
            return "0"

    def rank(self):
        try:

            vol24 = self.client.get_ticker()
            for coin_vol24 in vol24:
                if coin_vol24['symbol'] == self.symbol:
                    return str((self.lastAsk - self.lastBid) / self.lastBid * float(coin_vol24['quoteVolume']))

        except Exception as e:
            print("Exception volume: {0}".format(e))
            return "0"
