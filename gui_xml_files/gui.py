# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bline_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bline(object):
    def setupUi(self, Bline):
        Bline.setObjectName("Bline")
        Bline.resize(803, 526)
        self.centralwidget = QtWidgets.QWidget(Bline)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -20, 801, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome = QtWidgets.QWidget()
        self.welcome.setObjectName("welcome")
        self.bline_png = QtWidgets.QLabel(self.welcome)
        self.bline_png.setGeometry(QtCore.QRect(-40, 20, 841, 541))
        self.bline_png.setText("")
        self.bline_png.setPixmap(QtGui.QPixmap("bline.png"))
        self.bline_png.setObjectName("bline_png")
        self.stackedWidget.addWidget(self.welcome)
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.bline_png_2 = QtWidgets.QLabel(self.login)
        self.bline_png_2.setGeometry(QtCore.QRect(-40, 20, 841, 541))
        self.bline_png_2.setText("")
        self.bline_png_2.setPixmap(QtGui.QPixmap("bline.png"))
        self.bline_png_2.setObjectName("bline_png_2")
        self.login_button = QtWidgets.QPushButton(self.login)
        self.login_button.setGeometry(QtCore.QRect(360, 460, 94, 27))
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.login)
        self.register_button.setGeometry(QtCore.QRect(360, 500, 94, 27))
        self.register_button.setObjectName("register_button")
        self.stackedWidget.addWidget(self.login)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.reg_name = QtWidgets.QTextEdit(self.page_3)
        self.reg_name.setGeometry(QtCore.QRect(240, 120, 331, 31))
        self.reg_name.setObjectName("reg_name")
        self.reg_second_name = QtWidgets.QTextEdit(self.page_3)
        self.reg_second_name.setGeometry(QtCore.QRect(240, 160, 331, 31))
        self.reg_second_name.setObjectName("reg_second_name")
        self.reg_email = QtWidgets.QTextEdit(self.page_3)
        self.reg_email.setGeometry(QtCore.QRect(240, 200, 331, 31))
        self.reg_email.setObjectName("reg_email")
        self.reg_password = QtWidgets.QTextEdit(self.page_3)
        self.reg_password.setGeometry(QtCore.QRect(240, 240, 331, 31))
        self.reg_password.setObjectName("reg_password")
        self.reg_password_repeat = QtWidgets.QTextEdit(self.page_3)
        self.reg_password_repeat.setGeometry(QtCore.QRect(240, 280, 331, 31))
        self.reg_password_repeat.setObjectName("reg_password_repeat")
        self.reg_username = QtWidgets.QTextEdit(self.page_3)
        self.reg_username.setGeometry(QtCore.QRect(240, 320, 331, 31))
        self.reg_username.setObjectName("reg_username")
        self.register_confirm = QtWidgets.QPushButton(self.page_3)
        self.register_confirm.setGeometry(QtCore.QRect(360, 370, 94, 27))
        self.register_confirm.setObjectName("register_confirm")
        self.stackedWidget.addWidget(self.page_3)
        Bline.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bline)
        QtCore.QMetaObject.connectSlotsByName(Bline)

    def retranslateUi(self, Bline):
        _translate = QtCore.QCoreApplication.translate
        Bline.setWindowTitle(_translate("Bline", "MainWindow"))
        self.login_button.setText(_translate("Bline", "Login"))
        self.register_button.setText(_translate("Bline", "Register"))
        self.register_confirm.setText(_translate("Bline", "register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bline = QtWidgets.QMainWindow()
    ui = Ui_Bline()
    ui.setupUi(Bline)
    Bline.show()
    sys.exit(app.exec_())
