#!/usr/bin/python
#===================================================================================
# Author : Tushar Niras, Amol Morbale
# Email : tnniras@gmail.com
# Information : this class is defined to make CRUD operations easy.
#===================================================================================

#import yahoo_finance
#from yahoo_finance import Share
from MySQL import MySQL
import re

sql = MySQL()

# sql.order_by function should be called before the sql.select() function.
# this will select all the feilds from `users` table.
# you can specify whichever feilds you want to return. like : sql.select("users")
sql.where("email", "tushar@gmail.com")
sql.order_by("email", "desc")
result = sql.select("users", "id, email")
for email in result:
    print email["id"]

sql.close()






