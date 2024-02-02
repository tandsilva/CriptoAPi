# from binance.client import Client
# import config

# TradeSymbol = 'GALAUSDT'
# TimeInterval = Client.KLINE_INTERVAL_1MINUTE
# closes =[]




# if __name__== "main":
#     client = Client(config.API_KEY,config.API_SECRETI)

#     klines = client.get_historical_klines(TradeSymbol,TimeInterval,"1 day ago UTC")

# print(klines)
    # print("Get only close values")
    # for candles in range(LEN(klines)-1):
    #     closes.append(float(klines[candles][4]))
    #     socket ="wss://stream.binance.com:9443/ws/"+TradeSymbol.lower()+"@Kline"+TimeInterval

from binance.client import Client
import config

TradeSymbol = 'GALAUSDT'
TimeInterval = Client.KLINE_INTERVAL_1MINUTE
closes = []

if __name__ == "__main__":
    client = Client(config.API_KEY, config.API_SECRETI)

    klines = client.get_historical_klines(TradeSymbol, TimeInterval, "1 day ago UTC")

    print(klines)
