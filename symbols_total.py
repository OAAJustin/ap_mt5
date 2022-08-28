import MetaTrader5 as mt5
from loguru import logger as log

def symbols_total():
    symbols_total = mt5.symbols_total()
    log.info(symbols_total)
    
