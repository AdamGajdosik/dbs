#!/usr/bin/python3

import pymysql

class Database:

    # inicializacia prihlasovacich udajov
    def __init__(self,host,username,password,database_name):
        self.host = host
        self.password = password
        self.username = username
        self.db_name = database_name
    
    # pripojenie do DB
    def connect(self):
        try:
            self.connection = pymysql.connect(self.host, self.username, self.password, self.db_name)
            self.cursor = self.connection.cursor()
            return 1
        except:
            return 0
    
    # dopojenie od DB
    def disconnect(self):
        try:
            self.connection.close()
            return 1
        except:
            return 0

    # vykonanie query
    def executeCommand(self,command):
        self.connection.ping(reconnect=True)
        self.cursor.execute(command)
        self.connection.commit()
        records = self.cursor.fetchall()
        
        #print(records)
        print("query done")

        if len(records) != 0:
            return records
        else:
            return 0

    # registracia uzivatela
    def addUser(self,name,secondName,password,email,reg_day,loginName):

        values = "values ( '" + name + "','" + secondName + "','" + password + "','" + email + "','" + reg_day + "','" + loginName + "')"
        command = "INSERT INTO users_list(name,second_name,password,email,reg_day,login_username) " + values
        
        self.executeCommand(command)

    # prihlasovanie pomocou mena a hesla
    def getUserIdFromLogin(self,name,password):

        command = "SELECT id FROM users_list WHERE name='" + name + "' AND password='" + password + "'"
        out = self.executeCommand(command)
        if type(out) == int:
            return None
        return out[0][0]

    def listUsers(self):
        command = "SELECT * FROM users_list"
        self.executeCommand(command)

    def getUserInfoFromId(self,id):

        command = "SELECT * FROM users_list WHERE id='" + str(id) + "'"
        out = self.executeCommand(command)
        return out



    




