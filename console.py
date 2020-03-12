#!/usr/bin/python3

from main import *

def register(app):
    name = input("[?] Name: ")
    secondName = input("[?] Second name: ")
    email = input("[?] Email: ")
    loginName = input("[?] Login name: ")
    password = input("[?] Password: ")
    passwordSecond = input("[?] Repeat: ")
    out = app.register(name,secondName,password,passwordSecond,email,loginName)
    if out == 1:
        print("[+] Succes!")
    elif out == 0:
        print("[-] Passwords do not match")

def login(app):
    name = input("[?] Login name: ")
    password = input("[?] Password: ")
    out = app.login(name,password)
    if out == 1:
        print("[+] Succesfuly logged in!")
        return 1
    else:
        print("[-] Wrong username or password")
        return 0

def sendMoney(app):
        receiver = input("[?] Receiver: ")
        amount = input("[?] How much: ")
        password = input("[?] Password: ")
        out = app.sendMoneyToUser(receiver,int(amount),password)
        if out == 0:
            print("[-] User not found :O")
        elif out == 1:
            print("[+] Money sent :D")
        elif out == 2:
            print("[-] Wrong password :/")
        elif out == 3:
            print("[-] Not enough money :(")

def loginMenu(app):

    while True:
        print("1, login\n2, register\n0, exit")
        comm = input(">> ")
        if comm == "2":
            register(app)
        elif comm == "1":
            if login(app):
                break
        elif comm == "0":
            exit(1)

def loggedMenu(app):
    while True:
        print("1, show my info\n2, check balance\n3, add money to account\n4, send money to someone\n0, exit")
        comm = input(">> ")

        if comm == "1":
            info = app.getInfo()
            print(info)

        elif comm == "2":
            balance = app.getBalance()
            print("[!] Current balance is: " + str(balance))
        
        elif comm == "3":
            amount = input("[?] How much: ")
            app.addMoney(amount)

        elif comm == "4":
            sendMoney(app)

        elif comm == "0":
            exit(1)

def main():
    app = Application()
    print("Hello, what now?")
    loginMenu(app)
    loggedMenu(app)




if __name__ == "__main__":
    main()