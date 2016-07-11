#!/usr/bin/python

#import yahoo_finance
#from yahoo_finance import Share
from MySQL import MySQL

sql = MySQL()
result = sql.select("users", "email")
for email in result:
    print email[0]
sql.close()


