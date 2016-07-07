#!/usr/bin/python

from yahoo_finance import Share

yahoo = Share('AMZN')
print yahoo.get_price()
print yahoo.get_trade_datetime()

# COMMENT