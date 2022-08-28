import MetaTrader5 as mt5 
from loguru import logger as log
import time


def get_top_symbols(value, increment_in_sec):
    symbols = mt5.symbols_get()
    count = 0
    for s in symbols:
        count +=1
        print("{}. {}".format(count,s.name))
        time.sleep(increment_in_sec)
        if count == value: break
    print()