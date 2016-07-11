#!/usr/bin/python
import pymysql

# select (table, parameter)
# insert (table, data)
# update (table, id, data)
# delete (table, id)

class MySQL:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sherlock',
                             charset='utf8mb4')

        #sql = "SELECT * FROM `users` WHERE `email`=%s"

        self.cursor = self.connection.cursor()
        #cursor.execute(sql, ('tapan@yaholo.com',))
        #result = cursor.fetchone()
    
    
    def select(self, table, *feilds):
        flds = ""
        if not feilds:
            flds = '*'
        else:
            for f in feilds:
                if not flds:
                    flds = f
                else:
                    flds += ",`%s`" % f
        sql = "SELECT %s FROM `%s`" % (flds, table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result    
    
    def close(self):
        self.connection.close()

        

    