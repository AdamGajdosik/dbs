#!/usr/bin/python3

from database_controller import *
from config_parser import *
from datetime import date
<<<<<<< HEAD
=======

>>>>>>> master

class Application:
    def __init__(self):

        self.logged = 0
        self.user_id = None
<<<<<<< HEAD
        
=======
        print(date.today())
>>>>>>> master
        db_acces = ConfigParser.getDatabaseAcces()
        self.database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
        self.database.connect()
        print("[+] Connected to database!")

    def register(self,name,secondName,password,passwordSecond,email,loginName):

        today_date = str(date.today()).split("-")
        reg_day = today_date[2] + today_date[1] + today_date[0]

        if password == passwordSecond:
            self.database.addUser(name,secondName,password,email,reg_day,loginName)
            return 1
        else:
            return 0

    def login(self,name,password):
        user_id = self.database.getUserIdFromLogin(name,password)
        if user_id != None:
            self.logged = 1
            self.user_id = user_id
            return 1
        return 0

    def getInfo(self):
        out = self.database.getUserInfoFromId(self.user_id)
        return out
        

    
            




