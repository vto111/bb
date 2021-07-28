    # "e": "24hrTicker",  # Event type
    # "E": 123456789,     # Event time
    # "s": "BNBBTC",      # Symbol
    # "p": "0.0015",      # Price change
    # "P": "250.00",      # Price change percent
    # "w": "0.0018",      # Weighted average price
    # "x": "0.0009",      # Previous day's close price
    # "c": "0.0025",      # Current day's close price
    # "Q": "10",          # Close trade's quantity
    # "b": "0.0024",      # Best bid price
    # "B": "10",          # Bid bid quantity
    # "a": "0.0026",      # Best ask price
    # "A": "100",         # Best ask quantity
    # "o": "0.0010",      # Open price
    # "h": "0.0025",      # High price
    # "l": "0.0010",      # Low price
    # "v": "10000",       # Total traded base asset volume
    # "q": "18",          # Total traded quote asset volume
    # "O": 0,             # Statistics open time
    # "C": 86400000,      # Statistics close time
    # "F": 0,             # First trade ID
    # "L": 18150,         # Last trade Id
    # "n": 18151          # Total number of trades

from authorization import Authorization
import asyncio
from binance import AsyncClient, BinanceSocketManager

class Websocket:

    def __init__(self, msg=None):
        self.msg = msg

    def process_message(self, msg):
        print(msg)

            # process message normally

    async def main(self):
        a = Authorization()
        api_key = str(a.api_key)
        api_secret = str(a.api_secret)
        client = await AsyncClient.create(api_key, api_secret)
        bm = BinanceSocketManager(client)
        try:
            # ts = bm.depth_socket('BNBBTC', depth=BinanceSocketManager.WEBSOCKET_DEPTH_5)
            ts = bm.aggtrade_socket('BNBBTC')
            async with ts as tscm:
                while True:
                    res = await tscm.recv()
                    self.process_message(res)
        except Exception as e:
                print("Exception: {0}".format(e))
                # print(res)

        await client.close_connection()

    def start(self):
        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.main())

Websocket().start()