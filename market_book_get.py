import MetaTrader5 as mt5
from loguru import logger as log
import time

def market_book_get(symbol,interval):
    market_book_add = mt5.market_book_add(symbol)
    if market_book_add:
        for i in range(10):
            items = mt5.market_book_get(symbol)
            log.info(items)
            if items:
                for item in items:
                    log.info(item._asdict())
            time.sleep(interval) 