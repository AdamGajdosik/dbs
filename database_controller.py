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