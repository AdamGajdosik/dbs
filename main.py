#!/usr/bin/python3

from database_controller import *
from config_parser import *

#parser = ConfigParser()


def main():
    db_acces = ConfigParser.getDatabaseAcces()
    database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
    print(database.connect())
    print(database.disconnect())



if __name__ == "__main__":
    main()