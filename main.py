#!/usr/bin/python3

from database_controller import *
from config_parser import *


class Application:

    # pripojenie do DB, vytvorenie objektu DB
    def __init__(self):

        self.logged = 0
        self.user_id = None
        
        db_acces = ConfigParser.getDatabaseAcces()
        self.database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
        self.database.connect()
        print("[+] Connected to database!")

    # registracia noveho uzivatela
    def register(self,name,secondName,password,passwordSecond,email,loginName):

        if password == passwordSecond:
            self.database.addUser(name,secondName,password,email,loginName)
            return 1
        else:
            return 0

    # prihlasenie uzivatela
    def login(self,name,password):
        user_id = self.database.getUserIdFromLogin(name,password)
        if user_id != None:
            self.database.createLoginLogEntry(user_id)
            self.logged = 1
            self.user_id = user_id
            return 1
        return 0

    # vrati vsetky informacie o uzivatelovi
    def getInfo(self):
        out = self.database.getUserInfoFromId(self.user_id)
        return out

    # vrati stav uctu
    def getBalance(self):
        return self.database.getUserBalance(self.user_id)
        
    # nabije peniaze na ucet
    def addMoney(self,amount):

        self.database.addMoneyToUser(self.user_id,amount)
    
            




