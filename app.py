#!/usr/bin/python

#import yahoo_finance
#from yahoo_finance import Share
from MySQL import MySQL

sql = MySQL()

# sql.order_by function should be called before the sql.select() function.
sql.order_by("email")

# this will select all the feilds from `users` table.
# you can specify feilds to return. like : sql.select("users")
result = sql.select("users")

for email in result:
    print email["email"]
sql.close()


