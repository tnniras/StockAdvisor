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
    def select(self, table, feilds="*", *args, **kwargs):
        
        sql = "SELECT %s FROM `%s` " % (feilds, table)
        if self.sort_by:
            sql = sql +"order by "+ str(self.sort_by) +" "+ str(self.order)
        print sql
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result    
    def where(self, *args):
        args = list(args)
        #args = dict(args)
        operator=["=", ">=", "<=", "!="]
        
        args = str.split()
        #str = re.sub(r'[^\w]', '', str)
        try:
            where = "%s %s" % (str[0], str[1])
        except:
            where = "%s =" % str[0]
            #print(str[1])

        print(where)
    
    # This function is for data sorting for Mysql; but optinal.
    # example : SELECT * FROM `users`  order by id asc
    def order_by(self, sort_by="", order="", *args, **kwargs):
        self.sort_by = sort_by
        self.order = order
    
    # this function is for closing Mysql connection
    def close(self):
        self.connection.close()

########### END OF MySQL CLASS #############


