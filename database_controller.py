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

    def executeCommand(self,command):
        self.connection.ping(reconnect=True)
        self.cursor.execute(command)
        self.connection.commit()
        records = self.cursor.fetchall()
        
        print(records)
        print("[+] Done!")

        if len(records) != 0:
            return records
        else:
            return 0

    def addUser(self,name,secondName,password,email,reg_day):
        values = "values ( '" + name + "','" + secondName + "','" + password + "','" + email + "','" + reg_day + "' )"
        command = "INSERT INTO users_list(name,second_name,password,email,reg_day) " + values
        #cemm = "insert into users_list(name,secondName,password,email,reg_day) VALUES('Adam','Gajdosik','hehahe','mail','12121212');"
        self.executeCommand(command)

    def listUsers(self):
        command = "SELECT * FROM users_list"
        self.executeCommand(command)

    def test(self):
        command = "INSERT INTO test VALUES('test')"
        self.executeCommand(command)
    
    def listTest(self):
        command = "SELECT * FROM test"
        return self.executeCommand(command)


    




