import sys
sys.path.append('../')

from indicators import Indicators
from sql import Sql
from coins import Coins
from params import Params


onoff = 2

if onoff == 1:
    coin = "BCCBTC" #"EURUSDT"
    indicators = Indicators(coin)
    macd = indicators.macd()
    rsi = indicators.rsi()
    spredPerc = indicators.spreadPerc()
    volume = indicators.volume()
    rank = indicators.rank()
    print(coin + ' macd ' +  macd + ' spreadPerc ' + spredPerc + ' rsi ' + rsi + ' volume ' + volume + ' rank ' + rank)

    colParamsValue = {'coin':coin, 'macd':macd, 'spreadPerc':spredPerc, 'rsi':rsi, 'volume':volume, 'rank':rank}
    Sql().action(colParamsValue)

if onoff == 2:
    try:
        coins = Coins()
        arCoins = coins.getCoins()
        for coin in arCoins:
            indicators = Indicators(coin)
            macd = indicators.macd()
            rsi = indicators.rsi()
            spredPerc = indicators.spreadPerc()
            volume = indicators.volume()
            rank = indicators.rank()

            if float(macd) > 0 and float(spredPerc) > 0.6 and float(rsi) > 0:
                print("MACD > 0 " + coin)
                colParamsValue = {'coin': coin, 'macd': macd, 'spreadPerc': spredPerc, 'rsi': rsi, 'volume': volume,
                                  'rank': rank}
                Sql().action(colParamsValue)
    except Exception as e:
        print("Exception: {0}".format(e))

