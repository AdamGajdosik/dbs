#!/usr/bin/python3

import pymysql

class Database:
    def __init__(self,host,username,password,database_name):
        self.host = host
        self.password = password
        self.username = username
        self.db_name = database_name
    
    def connect(self):
        try:
            self.connection = pymysql.connect(self.host, self.username, self.password, self.db_name)
            return 1
        except:
            return 0
    
    def disconnect(self):
        try:
            self.connection.close()
            return 1
        except:
            return 0    

