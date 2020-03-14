# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_scene.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first_window(object):
    def setupUi(self, first_window):
        first_window.setObjectName("first_window")
        first_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(first_window)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_labe = QtWidgets.QLabel(self.centralwidget)
        self.welcome_labe.setGeometry(QtCore.QRect(370, 140, 64, 19))
        self.welcome_labe.setObjectName("welcome_labe")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(340, 350, 94, 27))
        self.button.setObjectName("button")
        first_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(first_window)
        QtCore.QMetaObject.connectSlotsByName(first_window)

    def retranslateUi(self, first_window):
        _translate = QtCore.QCoreApplication.translate
        first_window.setWindowTitle(_translate("first_window", "MainWindow"))
        self.welcome_labe.setText(_translate("first_window", "ahoj"))
        self.button.setText(_translate("first_window", "push me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    first_window = QtWidgets.QMainWindow()
    ui = Ui_first_window()
    ui.setupUi(first_window)
    first_window.show()
    sys.exit(app.exec_())
