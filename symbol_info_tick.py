import MetaTrader5 as mt5
from loguru import logger as log
from datetime import datetime

def symbol_info_tick(symbol):
    last_tick = mt5.symbol_info_tick(symbol)._asdict()
    for prop in last_tick:
        print("{} = {}".format(prop, last_tick[prop]))
        if last_tick[prop] == last_tick["time"]:
            print("Symbol Name: " , symbol)
            print("{} = {}".format(prop,datetime.fromtimestamp(last_tick["time"])))
        