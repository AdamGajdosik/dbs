#!/usr/bin/python3

from database_controller import *
from config_parser import *


class Application:
    def __init__(self):

        db_acces = ConfigParser.getDatabaseAcces()
        self.database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
        self.database.connect()
        print("[+] Connected to database!")


    def exit_app(self):
        print("Exitting...")

