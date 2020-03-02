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
            self.cursor = self.connection.cursor()
            return 1
        except:
            return 0
    
    def disconnect(self):
        try:
            self.connection.close()
            return 1
        except:
            return 0

    def execute_command(self,command):
        self.connection.ping(reconnect=True)
        self.cursor.execute(command)
        self.connection.commit()
        printf("[+] Done!")

    def addUser(self,name,second_name,password,email,reg_day):
        values = "values ( '" + name + "','" + second_name + "','" + password + "','" + email + "','" + reg_day + "' )"
        command = "INSERT INTO users_list(name,second_name,password,email,reg_day) " + values
        cemm = "insert into users_list(name,second_name,password,email,reg_day) VALUES('Adam','Gajdosik','hehahe','mail','12121212');"
        print(command)
        self.execute_command(command)

    




