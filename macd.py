from authorization import Authorization
import numpy as np
import talib as tb

class Macd:

    def __init__(self, criptopara):
        autorization = Authorization()
        self.client = autorization.getClient()
        self.symbol = str(criptopara)
        self.quantity = float(0.55)
        self.buyPrice = float(0.002)
        self.arr = list()

    def get_history(self):
        klines = self.client.get_historical_klines(self.symbol, self.client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        for value in klines:
            self.arr.append(value[1])

        return self.arr

    def getema(self):

        prices = np.asarray(self.get_history(), dtype=float)
        EMA12 = tb.EMA(prices, timeperiod=12)
        EMA26 = tb.EMA(prices, timeperiod=26)

        return round(EMA12[-1], 10) - round(EMA26[-1], 10)

    def action(self):
        pass
        try:
            macd = np.format_float_positional(self.getema())
            return macd
        except Exception:
            return "0"
        # macd = np.format_float_positional(self.getema())
        # return macd
