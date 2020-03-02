#!/usr/bin/python3

class ConfigParser:
    def __init__(self):

        self.conf_file = "config.conf"

        try:
            open_conf = open(self.conf_file,"r")
            open_conf.close()
        except:
            print("[-] Error! Missing config file")
            exit()


    def getDatabaseAcces(self):
        
        line = ""
        return_dict = {}
        open_conf = open(self.conf_file,"r")

        while line != "#database_acces\n" and line !="END\n":
            line = open_conf.readline()

        return_dict["user"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["password"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["database_name"]=open_conf.readline().strip("\n").split("=")[1]
        return_dict["host"]=open_conf.readline().strip("\n").split("=")[1]
        
        return return_dict
