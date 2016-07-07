#!/usr/bin/python

from yahoo_finance import Share

# List of stocks
stocks = [ "AMZN", "IBM", "YHOO"]

for stock in stocks:
    symbol = Share(stock)
    print "%s : %s " % (stock, symbol.get_price())

# COMMENT
print 'Hello, world!'
