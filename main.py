#!/usr/bin/python3

from database_controller import *
from config_parser import *

parser = ConfigParser()
db_acces = parser.getDatabaseAcces()

database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
print(database.connect())
print(database.disconnect())

name = "Adam"
second = "Gajdosik"
password = "heslo"
email = "heh"
reg_day = "12011999"

database.addUser(name,second,password,email,reg_day)