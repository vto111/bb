from authorization import Authorization


class Spread:

    def __init__(self, coin):
        self.coin = coin
        autorization = Authorization()
        self.client = autorization.getClient()

    def get_order_book(self):
        try:

            orders = self.client.get_order_book(symbol=self.coin)
            lastBid = float(orders['bids'][0][0])  # last buy price (bid)
            lastAsk = float(orders['asks'][0][0])  # last sell price (ask)
            spread = (lastAsk/lastBid - 1) * 100.0
            return spread

        except Exception as e:
            print('ob: %s' % (e))
            return 0


    def get_recent_trades(self):
        return self.client.get_recent_trades(symbol=self.coin)


