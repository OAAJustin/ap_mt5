import MetaTrader5 as mt5
from loguru import logger

def symbols_get():
    symbols = mt5.symbols_get()
    logger.info(symbols)