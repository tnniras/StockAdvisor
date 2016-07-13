#!/usr/bin/python
import pymysql

# select (table, parameter)
# insert (table, data)
# update (table, id, data)
# delete (table, id)

class MySQL:
    def __init__(self):
        self.sort_by = ""
        self.order = ""
        # initiate database connection.
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sherlock',
                             charset='utf8mb4')
        
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
    # this function is for selecting any feild on any table.(feilds veriable is optinal)     
    def select(self, table, *feilds):
        flds = "" #differnt name for feilds veriable.
        if not feilds:
            flds = '*'
        else:
            for f in feilds:
                if not flds:
                    flds = f
                else:
                    flds += ",`%s`" % f
        sql = "SELECT %s FROM `%s` " % (flds, table)
        if self.sort_by:
            sql = sql +"order by "+ str(self.sort_by) +" "+ str(self.order)
        print sql
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result    
    
    # This function is for data sorting for Mysql but optinal
    # example : SELECT * FROM `users`  order by id asc
    def order_by(self, *args):
        if len(args) >= 2:
            self.sort_by = args[0]
            self.order = args[1]
        elif len(args) == 1:
            self.sort_by = args[0]
    
    # this function is for closing Mysql connection
    def close(self):
        self.connection.close()

########### END OF MySQL CLASS #############


