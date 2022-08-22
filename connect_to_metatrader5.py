import MetaTrader5 as mt5

def connect_to_metatrader5():
    if not mt5.initialize():
        print("initialize failed, error code =", mt5.last_error())
        quit()