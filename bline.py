#!/usr/bin/python3


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bline_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


'''
main widget index:
0 - welcome
1 - menu
2 - registration
3 - registration result
4 - login
5 - logged user

'''

'''
logged user widget
0 - home screen
1 - My profile
2 - money
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
from main import *
from gui_xml_files.gui import *
from timeParser import *

class Bline(Ui_Bline):
    def __init__(self, logic):
        self.logic = logic

    def setupUi(self, Bline):
        super().setupUi(Bline)

        #
        # Tlacidla rozdelene podla obrazovky
        #

        # menu screen
        self.register_button.clicked.connect(self.registerScreen)
        self.login_button.clicked.connect(self.loginScreen)

        # registration screen
        self.register_confirm.clicked.connect(self.registerSubmit)

        # login screen
        self.login_submit.clicked.connect(self.loginSubmit)

        # logged user screen
        #menu
        self.logged_user_logout_button.clicked.connect(self.logOut)
        self.logged_user_profile_button.clicked.connect(self.userProfileInfo)
        self.logged_user_money_button.clicked.connect(self.userMoneyManagement)
        self.logged_user_home_button.clicked.connect(self.userHomeScreen)
        #money management
        self.logged_user_money_confirm_button.clicked.connect(self.sendMoney)

    #
    # Menenie obrazovky
    #

    # nastavi uvitaciu obrazovku
    def welcomeScreen(self):
        self.stackedWidget.setCurrentIndex(0)

    # ide do hlavneho menu
    def mainMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    # ide do registrace uzivatela
    def registerScreen(self):
        self.stackedWidget.setCurrentIndex(2)

    # ide na prihlasenie uzivatela
    def loginScreen(self):
        self.stackedWidget.setCurrentIndex(4)

    # obrazovka prihlaseneho uzivatela
    def loggedUserScreen(self):
        self.stackedWidget.setCurrentIndex(5)

    #
    # Funkcie
    #

    # odosle registraciu
    def registerSubmit(self):
        name = self.reg_name.toPlainText()
        secondName = self.reg_second_name.toPlainText()
        email = self.reg_email.toPlainText()
        password = self.reg_password.toPlainText()
        passwordRepeat = self.reg_password_repeat.toPlainText()
        username = self.reg_username.toPlainText()

        out = self.logic.register(name,secondName,password,passwordRepeat,email,username)

        self.mainMenu()

    # odosle prihlasovacie udaje
    def loginSubmit(self):
        
        username = self.login_username.toPlainText()
        password = self.login_password.toPlainText()

        out = self.logic.login(username,password)
        if out == 1:
            print(self.logic.user_id)
            self.loggedUserScreen()

    # odhlasovanie vsetkych uzivatelov
    def logOut(self):

        self.logic.logOut()
        self.mainMenu()

    # domovska obrazovka prihlaseneho uzivatela
    def userHomeScreen(self):
        self.logged_user_menu.setCurrentIndex(0)

    # prepne okno v menu a ukaze info o uzivatelovi    
    def userProfileInfo(self):
        self.logged_user_menu.setCurrentIndex(1)
        info = self.logic.getInfo()
        info = info[0]
        date = info[5]
        reg_date = TimeParser.toDate(date)
        
        string = info[1] + "\n" + info[2] + "\n" + info[4] + "\n" + info[7] + "\n" + reg_date
        self.output_test.setText(string)

    # sprava financii prihlaseneho uzivatela
    def userMoneyManagement(self):
        self.logged_user_menu.setCurrentIndex(2)
        
    # posle peniaze adresatovi
    def sendMoney(self):
        receiver = self.logged_user_receiver_text.toPlainText()
        amount = self.logged_user_amount_text.toPlainText()
        password = self.logged_user_password_text.toPlainText()

        try:
            amount = int(amount)
        except:
            return
        
        out = self.logic.sendMoneyToUser(receiver,amount,password)





def main():
    logic = Application()
    app = QtWidgets.QApplication(sys.argv)
    Bline_win = QtWidgets.QMainWindow()
    ui = Bline(logic)
    ui.setupUi(Bline_win)
    Bline_win.show()

    
    ui.mainMenu()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    

