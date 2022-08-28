import MetaTrader5 as mt5
from loguru import logger as log 

def symbol_info(symbol):
    symbol_info = mt5.symbol_info(symbol)._asdict()
    for prop in symbol_info:
        print("{}={}".format(prop,symbol_info[prop]))
    