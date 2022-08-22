from connect_to_metatrader5 import connect_to_metatrader5

def symbols_total():
    connect_to_metatrader5()
    symbols_total = mt5.symbols_total()
    print(symbols_total)