# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bline_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


'''
widget index:
0 - welcome
1 - menu
2 - registration
3 - login

'''

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
from main import *
from gui_xml_files.gui import *

class Bline(Ui_Bline):
    def __init__(self, logic):
        self.logic = logic

    def setupUi(self, Bline):
        super().setupUi(Bline)

        # welcome screen
        self.register_button.clicked.connect(self.registerScreen)
        self.login_button.clicked.connect(self.loginScreen)

        # registration screen
        self.register_confirm.clicked.connect(self.registerSubmit)

        # login screen
        self.login_submit.clicked.connect(self.loginSubmit)

    def welcomeScreen(self):
        self.stackedWidget.setCurrentIndex(0)

    def mainMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def registerScreen(self):
        self.stackedWidget.setCurrentIndex(2)

    def registerSubmit(self):

        name = self.reg_name.toPlainText()
        secondName = self.reg_second_name.toPlainText()
        email = self.reg_email.toPlainText()
        password = self.reg_password.toPlainText()
        passwordRepeat = self.reg_password_repeat.toPlainText()
        username = self.reg_username.toPlainText()

        out = self.logic.register(name,secondName,password,passwordRepeat,email,username)


        self.stackedWidget.setCurrentIndex(1)

    def loginScreen(self):
        self.stackedWidget.setCurrentIndex(3)

    def loginSubmit(self):
        
        username = self.login_username.toPlainText()
        password = self.login_password.toPlainText()

        out = self.logic.login(username,password)
        print(out)



def main():
    logic = Application()
    app = QtWidgets.QApplication(sys.argv)
    Bline_win = QtWidgets.QMainWindow()
    ui = Bline(logic)
    ui.setupUi(Bline_win)
    Bline_win.show()
    ui.welcomeScreen()
    time.sleep(2)
    ui.mainMenu()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    

