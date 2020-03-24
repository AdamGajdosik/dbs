#!/usr/bin/python3

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
        self.mainScreenIndex = 0
        self.checkRaceId = None
        self.news_races = self.logic.getSomeRacesFromIndex(0,5)

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
        self.register_screen_back_button.clicked.connect(self.mainMenu)

        # login screen
        self.login_submit.clicked.connect(self.loginSubmit)
        self.login_screen_back_button.clicked.connect(self.mainMenu)

        # logged user screen
        #menu
        self.logged_user_logout_button.clicked.connect(self.logOut)
        self.logged_user_profile_button.clicked.connect(self.userProfileInfoScreen)
        self.logged_user_money_button.clicked.connect(self.userMoneyManagementScreen)
        self.logged_user_home_button.clicked.connect(self.userHomeScreen)
        #money management   
        self.logged_user_money_confirm_button.clicked.connect(self.sendMoney)
        #home screen
        self.news_button_1.clicked.connect(lambda: self.raceDetailScreen(self.news_races[0][0]))
        self.news_button_2.clicked.connect(lambda: self.raceDetailScreen(self.news_races[1][0]))
        self.news_button_3.clicked.connect(lambda: self.raceDetailScreen(self.news_races[2][0]))
        self.news_button_4.clicked.connect(lambda: self.raceDetailScreen(self.news_races[3][0]))
        self.news_button_5.clicked.connect(lambda: self.raceDetailScreen(self.news_races[4][0]))

        # race detail
        self.race_detail_back_button.clicked.connect(self.goToPreviousScreen)

    #
    # Menenie obrazovky
    #

    # nastavi uvitaciu obrazovku
    def welcomeScreen(self):
        self.stackedWidget.setCurrentIndex(0)
        self.mainScreenIndex = 0
        

    # ide do hlavneho menu
    def mainMenu(self):
        self.stackedWidget.setCurrentIndex(1)
        self.mainScreenIndex = 1
        self.register_screen_info_label.setText("")
    
    # ide do registrace uzivatela
    def registerScreen(self):
        self.stackedWidget.setCurrentIndex(2)
        self.mainScreenIndex = 2
        self.reg_name.setText("")
        self.reg_email.setText("")
        self.reg_password.setText("")
        self.reg_password_repeat.setText("")
        self.reg_second_name.setText("")
        self.reg_username.setText("")

    # ide na prihlasenie uzivatela
    def loginScreen(self):
        self.stackedWidget.setCurrentIndex(4)
        self.mainScreenIndex = 4
        self.login_username.setText("")
        self.login_password.setText("")

    # obrazovka prihlaseneho uzivatela
    def loggedUserScreen(self):
        self.stackedWidget.setCurrentIndex(5)
        self.mainScreenIndex = 5

    # detail preteku
    def raceDetailScreen(self, race_id):
        self.stackedWidget.setCurrentIndex(6)
        self.race_details_info_text.setText("")
        self.race_details_horses_text.setText("")
        info = self.logic.getWholeRaceInfoFromId(race_id)
        horses = self.logic.getHorsesFromRaceId(race_id)
        self.race_details_info_text.append(info[3] + "\n")
        self.race_details_info_text.append("time: " + info[5] + "\n")
        self.race_details_info_text.append("status: " + info[6] + "\n")
        self.race_details_info_text.append("track: " + info[8])
        for horse in horses:
            self.race_details_horses_text.append(horse[1])
            


    # naspat
    def goToPreviousScreen(self):
        self.stackedWidget.setCurrentIndex(self.mainScreenIndex)
        

    #
    # Funkcie
    #

    # odosle registraciu
    def registerSubmit(self):
        name = self.reg_name.text()
        secondName = self.reg_second_name.text()
        email = self.reg_email.text()
        password = self.reg_password.text()
        passwordRepeat = self.reg_password_repeat.text()
        username = self.reg_username.text()

        out = self.logic.register(name,secondName,password,passwordRepeat,email,username)
        if out == 1:
            self.main_screen_info_label.setText("Succesfuly registred!")
            self.mainMenu()

        elif out == 0:
            self.register_screen_info_label.setText("Passwords do not match")
        elif out == 2:
            self.register_screen_info_label.setText("Username allready used")
        elif out == 3:
            self.register_screen_info_label.setText("Email allready used")
        

    # odosle prihlasovacie udaje
    def loginSubmit(self):
        
        username = self.login_username.text()
        password = self.login_password.text()

        out = self.logic.login(username,password)
        if out == 1:
            print(self.logic.user_id)
            self.loggedUserScreen()
            self.userHomeScreen()

    # odhlasovanie vsetkych uzivatelov
    def logOut(self):

        self.logic.logOut()
        self.mainMenu() 
        self.main_screen_info_label.setText("")

    # posle peniaze adresatovi
    def sendMoney(self):
        receiver = self.logged_user_receiver_text.text()
        amount = self.logged_user_amount_text.text()
        password = self.logged_user_password_text.text()

        try:
            amount = int(amount)
        except:
            return
        
        out = self.logic.sendMoneyToUser(receiver,amount,password)
        self.userMoneyManagementScreen()

    def test(self):
        print("ahoj")
        

    #
    # Uzivatelove obrazovky
    #

    # domovska obrazovka prihlaseneho uzivatela
    def userHomeScreen(self):
        self.logged_user_menu.setCurrentIndex(0)
        
        self.news_button_1.setText(self.news_races[0][3] + " " + self.news_races[0][6])
        self.news_button_2.setText(self.news_races[1][3] + " " + self.news_races[1][6])
        self.news_button_3.setText(self.news_races[2][3] + " " + self.news_races[2][6])
        self.news_button_4.setText(self.news_races[3][3] + " " + self.news_races[3][6])
        self.news_button_5.setText(self.news_races[4][3] + " " + self.news_races[4][6])

    # prepne okno v menu a ukaze info o uzivatelovi    
    def userProfileInfoScreen(self):
        self.logged_user_menu.setCurrentIndex(1)
        info = self.logic.getInfo()
        info = info[0]
        date = info[5]
        reg_date = TimeParser.toDate(date)
        
        string = info[1] + "\n" + info[2] + "\n" + info[4] + "\n" + info[7] + "\n" + reg_date
        self.output_test.setText(string)

    # sprava financii prihlaseneho uzivatela
    # do jedneho stlpca pri transakciach sa zmesti najviac 19 riadkov
    def userMoneyManagementScreen(self):
        self.logged_user_menu.setCurrentIndex(2)
        self.logged_user_balance_text.setText(str(self.logic.getBalance()))
        
        transactionList = self.logic.transactionsList()
        self.logged_user_amount_text.setText("")
        self.logged_user_password_text.setText("")
        self.logged_user_receiver_text.setText("")
        self.logged_user_transactions_type_text.setText("")
        self.logged_user_transactions_amount_text.setText("")
        self.logged_user_transactions_user_text.setText("")
        self.logged_user_transactions_date_text.setText("")
        
        for transaction in transactionList:

            if transaction[1] == self.logic.user_id:
                self.logged_user_transactions_type_text.append("sent")
                self.logged_user_transactions_user_text.append(self.logic.getOtherUsername(transaction[2]))
                
            else:
                self.logged_user_transactions_type_text.append("received")
                self.logged_user_transactions_user_text.append(self.logic.getOtherUsername(transaction[1]))

            self.logged_user_transactions_amount_text.append(str(transaction[3]))
            self.logged_user_transactions_date_text.append(TimeParser.toDate(transaction[4]))

        self.logic.transactionCount()
        



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

