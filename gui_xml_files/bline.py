# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bline_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
from gui import *

class Bline(Ui_Bline):
    def setupUi(self, Bline):
        super().setupUi(Bline)
        self.register_button.clicked.connect(self.registerScreen)
        self.register_confirm.clicked.connect(self.registerSubmit)

    def welcomeScreen(self):
        self.stackedWidget.setCurrentIndex(0)

    def mainMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def registerScreen(self):
        self.stackedWidget.setCurrentIndex(2)

    def registerSubmit(self):

        name = self.reg_name.toPlainText()
        second_name = self.reg_second_name.toPlainText()
        email = self.reg_email.toPlainText()
        password = self.reg_password.toPlainText()
        password_repeat = self.reg_password_repeat.toPlainText()
        username = self.reg_username.toPlainText()

        self.stackedWidget.setCurrentIndex(1)




def main():
    app = QtWidgets.QApplication(sys.argv)
    Bline_win = QtWidgets.QMainWindow()
    ui = Bline()
    ui.setupUi(Bline_win)
    Bline_win.show()
    ui.welcomeScreen()
    time.sleep(2)
    ui.mainMenu()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    

