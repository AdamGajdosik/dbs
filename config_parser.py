#!/usr/bin/python3

conf_file = "config.conf"

class ConfigParser:
    def __init__(self):
        try:
            open_conf = open(conf_file,"r")
            open_conf.close()
        except:
            print("[-] Error! Missing config file")
            exit()

    @staticmethod
    def getDatabaseAcces():
        
        line = ""
        return_dict = {}
        try:
            open_conf = open(conf_file,"r")
        except:
            print("[-] Missing config file")
            exit()

        while line != "#database_acces\n" and line !="END\n":
            line = open_conf.readline()

        return_dict["user"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["password"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["database_name"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["host"]=open_conf.readline().strip("\n").split("=")[1]
        
        return return_dict
