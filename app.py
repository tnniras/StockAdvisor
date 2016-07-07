#!/usr/bin/python

from yahoo_finance import Share

# List of stocks
stocks = [ "AMZN", "IBM", "YHOO"]

for stock in stocks:
    symbol = Share(stock)
    print "%s : %s " % (stock, symbol.get_price())

#print yahoo.get_price()
#print yahoo.get_trade_datetime()

# COMMENT
print 'Hello, world!'
