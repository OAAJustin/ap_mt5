import MetaTrader5 as mt5
from loguru import logger
from symbols_total import symbols_total
 





if __name__ == '__main__':
    mt5.initialize()
    symbols_total = symbols_total()
