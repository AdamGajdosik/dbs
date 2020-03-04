# dbs
najlepsi projekt z databaz

by Robo a Adam

meno: zLeM6tSMUW
heslo: 3LxEhUZn6C
host: remotemysql.com
port: 3306
linux terminal:
1. service mysql start
2. mysql -u zLeM6tSMUW -p -h remotemysql.com
3. Enter password: 3LxEhUZn6C


Tabulky:

users_list:
id(6) | name(20) | second_name(20) | password/hash(20) | email(30) | reg_day(8) | balance

horses:

tracks:

races:

logs:

bets:

money_transactions:


Database_controller.py navod:

    hnus = Database(host,meno,heslo,meno_databazy) - vytvori objekt databazy

    hnus.connect() - pripoji do databazy

    hnus.disconnect() - odpoji od databazy

    hnus.addUser(meno,priezvisko,heslo,email,den_registracie)

Config_parser.py navod:

    ConfigParser.getDatabaseAcces() - vrati dictionary s pristupovymi udajmi do DB