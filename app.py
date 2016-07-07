#!/usr/bin/python

import yahoo_finance
from yahoo_finance import Share

# List of stocks
stocks = [ "AMZN", "IBM", "RELIANCE"]



#def get_stock_price(stocks):
 #   for stock in stocks:
 #       symbol = Share(stock)
 #       print "%s : %s " % (stock, symbol.get_price())

#get_stock_price(stocks)

tt = Share("BHEL.NS")
#print yahoo_finance.__dict__
print(tt.get_price())