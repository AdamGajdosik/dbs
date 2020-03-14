#!/usr/bin/python3

import pymysql
from datetime import date
from datetime import datetime

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
    def executeCommand(self, command):
        self.connection.ping(reconnect=True)
        self.cursor.execute(command)
        self.connection.commit()
        records = self.cursor.fetchall()
        
        #print(records)
        #print("query done")

        if len(records) != 0:
            return records
        else:
            return 0

    # registracia uzivatela
    def addUser(self, name, secondName, password, email, loginName):

        # upravenie datumu na string ddmmrrrr
        today_date = str(date.today()).split("-")
        reg_day = today_date[2] + today_date[1] + today_date[0]

        values = "values ( '" + name + "','" + secondName + "','" + password + "','" + email + "','" + reg_day + "','" + "0" + "','" + loginName + "')"
        command = "INSERT INTO users_list(name,second_name,password,email,reg_day,balance,login_username) " + values
        
        self.executeCommand(command)

    # vrati vsetkych uzivatelov
    def listUsers(self):
        command = "SELECT name,second_name,email FROM users_list"
        self.executeCommand(command)

    # prihlasovanie pomocou mena a hesla
    def getUserIdFromLogin(self, name, password):

        command = "SELECT id FROM users_list WHERE name='" + name + "' AND password='" + password + "'"
        out = self.executeCommand(command)
        if type(out) == int:
            return None
        return out[0][0]

    # ziska id z mena
    def getUserIdFromUsername(self, name):

        command = "SELECT id FROM users_list WHERE login_username='" + name + "'"
        out = self.executeCommand(command)

        # ak nenajde uzivatela vrati int nie tuple
        if type(out) == int:
            return None

        return out[0][0]

    # vrati vsetky informacie z tabulky users_list
    def getUserInfoFromId(self, id):

        command = "SELECT * FROM users_list WHERE id='" + str(id) + "'"
        out = self.executeCommand(command)
        return out
    
    # vytvori zazam o prihlaseni uzivatela
    def createLoginLogEntry(self, user_id):

        if self.getUserInfoFromId(user_id) == 0:
            return

        # upravenie casu na string hhmmss
        now = str(datetime.now().time()).split(":")
        now[2] = now[2].split(".")[0]
        time = now[0] + now[1] + now[2]
        
        # upravenie datumu na string ddmmrrrr
        today_date = str(date.today()).split("-")
        date_now = today_date[2] + today_date[1] + today_date[0]

        values = "('" + str(user_id) + "','" + str(date_now) + "','" + str(time) + "')"
        command = "INSERT INTO login_log(user_id,date,time) VALUES" + values
        self.executeCommand(command)
    
    # ziska akutalny stav uctu
    def getUserBalance(self, user_id):

        command = "SELECT balance FROM users_list WHERE id='" + str(user_id) + "'"
        out = self.executeCommand(command)

        return out[0][0]

    # prida uzivatelovi peniaze na ucet
    def addMoneyToUser(self, user_id, amount):
        
        current_balance = self.getUserBalance(user_id)
        balance = current_balance + int(amount)

        command = "UPDATE users_list SET balance=" + str(balance) + " WHERE id=" + str(user_id)
        #print(command)
        self.executeCommand(command)

    # odoberie uzivatelovi urcenu sumu penazi
    def removeMoneyFromUser(self, user_id, amount):

        current_balance = self.getUserBalance(user_id)
        balance = current_balance - int(amount)

        command = "UPDATE users_list SET balance=" + str(balance) + " WHERE id=" + str(user_id)
        self.executeCommand(command)

    # prida zaznam o tranzakcii do logu
    def addTransactionLog(self, sender_id, receiver_id, amount):

        today_date = str(date.today()).split("-")
        day = today_date[2] + today_date[1] + today_date[0]

        values = "('" + str(sender_id) + "','" + str(receiver_id) + "'," + str(amount) + "," + str(day) + ")"
        
        print(command)
        self.executeCommand(command)

    def executeMany(self, listToSend):
        self.connection.ping(reconnect=True)
        #print(listToSend)
        for x in listToSend:
            #print(x)
            self.cursor.execute(x)
            if (x[12:17] == "race_"):
                self.connection.commit()
        self.connection.commit()
        records = self.cursor.fetchall()
        
       #print(records)
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

    def addHorse(self, id, name, sortPriority, status):
        command = ("INSERT INTO horses(id,name,sorting_priority,status) values(%d,'%s',%d,'%s')"%(id, name, sortPriority, status))
        #print(command)
        self.executeCommand(command)

    def listHorses(self):
        command = "SELECT * from horses"
        self.executeCommand(command)

    def testForSame(self, name):
        command = "SELECT EXISTS(SELECT * from horses where name=" + "'" + name + "'" + ");"
        return self.executeCommand(command)[0][0]

    def addTrack(self, venue, country, timezone):
        command = ("INSERT INTO tracks(name,country,timezone) values('%s','%s','%s')"%(venue,country,timezone))
        self.executeCommand(command)

    def addManyTrack(self, data):
        print("som tu")
        command = "INSERT INTO tracks(name,country,timezone) values('%s','%s','%s')"
        self.executeMany(command, data)


    def testForSameTrack(self, name):
        command = "SELECT EXISTS(SELECT * from tracks where name=" + "'" + name + "'" + ");"
        return self.executeCommand(command)[0][0]

    def addRace(self, id, name, eventId, timezone, numberOfWinners, complete, runners):
        return

    def getLastRaceId(self):
        command = "select count(*) from races;"
        return self.executeCommand(command)[0][0]

    def getLastTrackId(self):
        command = "select count(*) from tracks;"
        return self.executeCommand(command)[0][0]

    def testForSameHorse(self, name):
        command = "SELECT EXISTS(SELECT * from horses where name=" + "'" + name + "'" + ");"
        return self.executeCommand(command)[0][0]

    def getTrackId(self, name):
        command = "select id from tracks where name=" + "'" + name + "'" + ""
        return self.executeCommand(command)



 
