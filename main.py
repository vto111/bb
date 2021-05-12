import sys
sys.path.append('../')

from macd import Macd
from sql import Sql
from coins import Coins
from spread import Spread

# coin = "BNBBTC"
# getmacd = Macd(coin)
# macd = getmacd.action()
# spread = Spread(coin)
# spredPerc = str(spread.get_order_book())
# print(macd)
# if float(macd) > 0:
#     print(float(macd))
# else:
#     print(type(float(macd)))


# Sql([coin, 'macd', macd, 'spreadPerc', spredPerc])


coins = Coins()
arCoins = coins.getCoins()
for coin in arCoins:
    getmacd = Macd(coin)
    macd = getmacd.action()
    spread = Spread(coin)
    spredPerc = str(spread.get_order_book())
    if float(macd) > 0 and float(spredPerc) > 0.6:
        print("MACD > 0 " + coin)
        Sql([coin, 'macd', macd, 'spreadPerc', spredPerc])



# print(spredPerc)
# print(spread.get_order_book())
# print(spread.get_recent_trades())c