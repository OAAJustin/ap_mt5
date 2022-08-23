from mt5_connect import mt5_connect
import MetaTrader5 as mt5
from loguru import logger

connect = mt5_connect()

symbols = mt5.symbols_total()
print("There are ",symbols, "symbols!")
