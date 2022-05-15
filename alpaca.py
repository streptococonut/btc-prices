from alpaca_trade_api import REST, TimeFrame
import pandas as pd
import openpyxl
from datetime import datetime
api = REST('PKW1ZK9YZN9BF93UPGGM', 'FDA4EzHD2TaMfIHG62ieBq9ZwHuo5i0Ngcsly8jD', 'https://data.alpaca.markets/v1beta1/crypto')
now = datetime.now()
now = now.strftime("%Y-%m-%d")

data = api.get_crypto_bars("BTCUSD", TimeFrame.Hour, "2022-01-01", now).df
data_edited = [i.replace(tzinfo=None) for i in data.index]
data.index = data_edited
data.to_excel('btc_prices.xlsx')
