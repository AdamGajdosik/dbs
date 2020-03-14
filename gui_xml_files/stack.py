# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stack.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(819, 600)
        self.centralwidget = QtWidgets.QWidget(test)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetStack = Q3WidgetStack(self.centralwidget)
        self.widgetStack.setGeometry(QtCore.QRect(0, 0, 811, 601))
        self.widgetStack.setObjectName("widgetStack")
        self.welcome = QtWidgets.QWidget(self.widgetStack)
        self.welcome.setGeometry(QtCore.QRect(0, 0, 811, 601))
        self.welcome.setObjectName("welcome")
        self.label_3 = QtWidgets.QLabel(self.welcome)
        self.label_3.setGeometry(QtCore.QRect(370, 220, 64, 19))
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QWidget(self.widgetStack)
        self.login.setObjectName("login")
        self.label_2 = QtWidgets.QLabel(self.login)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 151, 71))
        self.label_2.setObjectName("label_2")
        self.register_2 = QtWidgets.QWidget(self.widgetStack)
        self.register_2.setGeometry(QtCore.QRect(0, 0, 811, 601))
        self.register_2.setObjectName("register_2")
        self.label = QtWidgets.QLabel(self.register_2)
        self.label.setGeometry(QtCore.QRect(310, 10, 171, 41))
        self.label.setObjectName("label")
        test.setCentralWidget(self.centralwidget)

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "MainWindow"))
        self.label_3.setText(_translate("test", "vitaj"))
        self.label_2.setText(_translate("test", "Prihlasenie"))
        self.label.setText(_translate("test", "Registracia"))
from q3widgetstack import Q3WidgetStack


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = QtWidgets.QMainWindow()
    ui = Ui_test()
    ui.setupUi(test)
    test.show()
    sys.exit(app.exec_())
