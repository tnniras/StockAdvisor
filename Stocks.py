#!/usr/bin/python

from pymongo import MongoClient
client = MongoClient()
db = client.sherlock_database

stocks = [

    {
        "resource": {
            "classname": "Quote",
            "fields": {
                "name": "ZICOM ELECTRONIC S INR10",
                "price": "47.299999",
                "symbol": "ZICOM.NS",
                "ts": "1467971998",
                "type": "equity",
                "utctime": "2016-07-08T09:59:58+0000",
                "volume": "55415"
            }
        }
    },
    {
        "resource": {
            "classname": "Quote",
            "fields": {
                "name": "BHARAT HEAVY ELECTRICALS LTD.",
                "price": "137.850006",
                "symbol": "BHEL.BO",
                "ts": "1467973718",
                "type": "equity",
                "utctime": "2016-07-08T10:28:38+0000",
                "volume": "723332"
            }
        }
    }

]



URL="http://finance.yahoo.com/webservice/v1/symbols/"
FORMAT="/quote?format=json&view=detail"

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
    def get_price(self):
        print "%s%s%s" % (URL, self.symbol, FORMAT)

stock = Stock("AMZN")

stock.get_price()
        