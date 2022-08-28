import MetaTrader5 as mt5
from loguru import logger

def mt5_init():
    if not mt5.initialize():
        print("initialize failed, error code =", mt5.last_error())
        quit()
logger.info("Connection Successful!") 