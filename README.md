# dbs
najlepsi projekt z databaz

by Robo a Adam



Tabulky:

users_list:
id(6) | name(20) | second_name(20) | password/hash(20) | email(30) | reg_day(8) | balance

horses:
id(6) | name(20) | sortPriority() | status() | adjustementFactor?()

tracks:
id() | country() | venue() | timezone() 

races:
id() | eventTypeId() | eventName() | numberOfWinners() | complete() | runners()

logs:
id() | fromUser() | severity() | time()

bets:
id() | fromUser() | matchId() | amount() | time() | currency()

money_transactions:
id() | type() | amount() | time() | sender_id() | receiver_id()

Database_controller.py navod:

    hnus = Database(host,meno,heslo,meno_databazy) - vytvori objekt databazy

    hnus.connect() - pripoji do databazy

    hnus.disconnect() - odpoji od databazy

    hnus.addUser(meno,priezvisko,heslo,email,den_registracie)

    hnus.listUsers() - vrati zoznam uzivatelov

Config_parser.py navod:

    ConfigParser.getDatabaseAcces() - vrati dictionary s pristupovymi udajmi do DB


