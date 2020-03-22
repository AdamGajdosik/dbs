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
        out = self.database.connect()
        if out == 0:
            print("[-] Not connected to DB")
            exit()
        print("[+] Connected to database!")

    # registracia noveho uzivatela
    def register(self,name,secondName,password,passwordSecond,email,loginName):

        if password == passwordSecond:
            self.database.addUser(name,secondName,password,email,loginName)
            print("[+] Succes!")
            return 1
        else:
            print("[-] Error")
            return 0

    # prihlasenie uzivatela
    def login(self,name,password):
        user_id = self.database.getUserIdFromLogin(name,password)
        if user_id != None:
            self.database.createLoginLogEntry(user_id)
            self.logged = 1
            self.user_id = user_id
            print("[+] Logged in!")
            return 1
        return 0

    # vrati vsetky informacie o uzivatelovi
    def getInfo(self):
        out = self.database.getUserInfoFromId(self.user_id)
        return out

    # ziska meno z id
    def getOtherUsername(self, user_id):
        return self.database.getUsernameFromId(user_id)

    # vrati stav uctu
    def getBalance(self):
        return self.database.getUserBalance(self.user_id)

    # nabije peniaze na ucet
    def addMoney(self,amount):
        self.database.addMoneyToUser(self.user_id,amount)

    # odcita sumu penazi z uctu
    def removeMoney(self, amount):
        self.database.removeMoneyFromUser(self.user_id)
    
    # posle peniaze na iny ucet
    def sendMoneyToUser(self,receiver,amount,password):
        
        #print(self.getBalance())
        receiver_id = self.database.getUserIdFromUsername(receiver)
        if receiver_id == None:
            print("[-] User dont exists")
            return 0

        user_password = self.database.getUserInfoFromId(self.user_id)[0][3]
        if user_password != password:
            print("[-] Wrong password")
            return 2

        if self.getBalance() < amount:
            print("[-] Not enough money")
            return 3
        
        self.database.addMoneyToUser(receiver_id,amount)
        self.database.removeMoneyFromUser(self.user_id,amount)
        self.database.addTransactionLog(self.user_id,receiver_id,amount)
        print("[+] Done!")
        return 1

    # odhlasenie   
    def logOut(self):
        self.user_id = None
        self.logged = 0
        print("[+] Loged out")

    # ziska pocet transakcii
    def transactionCount(self):
        return self.database.getTransactionCount(self.user_id)

    # vrati zaznamy transakcii
    def transactionsList(self):
        return self.database.getTransactionsList(self.user_id, 0, 0)

    # z db ziska vsetky kone co sa zucastnili preteku
    def getHorsesFromRaceId(self, race_id):
        return self.database.getHorsesFromRaceId(race_id)

    # zobrazi 10 zaznamov od indexu
    def getSomeRacesFromIndex(self, index, count):
        return self.database.getRacesByIndex(index, count)
    

    def dataImport(self, id, name, sortPriority, status, venue, country, timezone):
        #print("meno", name)
        #print("som tu")
        #same = self.database.testForSameTracks(venue)
        if venue in addMany:
            print("uz tam je")
            return
        else:
            #print("adding")
            #self.database.addHorse(id, name, sortPriority, status)
            self.database.addTrack(venue,country,timezone)

    def newImport(self, listToSend):
        self.database.executeMany(listToSend)


    def getRaceId(self):
        return self.database.getLastRaceId()

    def getTrackId(self):
        return self.database.getLastTrackId()

    def testForSameHorse(self, name):
        return self.database.testForSameHorse(name)

    def testForSameTrack(self, name):
        return self.database.testForSameTrack(name)

    def getSameTrackId(self, name):
        return self.database.getTrackId(name)

    
            





    