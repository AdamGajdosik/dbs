#!/usr/bin/python3

from database_controller import *
from config_parser import *


class Application:
    def __init__(self):

        self.logged = 0
        self.user_id = None

        db_acces = ConfigParser.getDatabaseAcces()
        self.database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
        self.database.connect()
        self.database.listUsers()
        self.database.listHorses()
        print("[+] Connected to database!")

    def register(self,name,secondName,password,passwordSecond,email):
        if password == passwordSecond:
            self.database.addUser(name,secondName,password,email,"11223344")
            return 1
        else:
            return 0

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

            




