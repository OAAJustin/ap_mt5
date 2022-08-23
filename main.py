from mt5_connect import mt5_connect
import MetaTrader5 as mt5

# connect to the server
mt5_connect()

# Get all Symbols
symbols = mt5.symbols_total()

# Print the symbols
print(symbols)