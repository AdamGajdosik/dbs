#!/usr/bin/python3

from main import *

def register(app):
    name = input("Name: ")
    secondName = input("Second name: ")
    email = input("Email: ")
    password = input("Password: ")
    passwordSecond = input("Repeat: ")
    out = app.register(name,secondName,password,passwordSecond,email)
    if out == 1:
        print("[+] Succes!")



def main():
    app = Application()
    print("Hello, what now?")
    while True:
        print("1, login\n2, register\n0, exit")

        comm = input(">> ")

        if comm == "2":
            register(app)

        elif comm == "0":
            exit(1)




if __name__ == "__main__":
    main()