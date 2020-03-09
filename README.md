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



   
    
    
# Scenáre
## Login

 -  Verzia: v1.0
 -  Scenár: 1
 -  Milestone: [Registrácia a prihlásenie používateľa](https://github.com/AdamGajdosik/dbs/milestone/1)
 -  Issues
      -  [Registrácia](/../../issues/1)

Pouzívateľ sa vie do systému zaregistrovať pomocou emailu a hesla. Po verifikovaní emailu sa pomocou emailu a hesla dokáže do aplikácie prihlásiť

## Import dát

 -  Verzia: v1.0
 -  Scenár: 2
 -  Milestone: tba
 -  Issues
      -  tba

Všetky dáta pre fungovanie systému prevzaté z api BetFair. Obsahujú kone, závody, krajiny. 

## Pridávanie dát

 -  Verzia: v1.0
 -  Scenár: 3
 -  Milestone: tba
 -  Issues
      -  tba

Možnosť pridávania rôznych dát cez formulár.

## Správa stávok

 -  Verzia: v1.0
 -  Scenár: 4
 -  Milestone: tba
 -  Issues
      -  tba
      
Užívateľ si vie podať stávku na zápas, pozrieť štatistiky minulých zápasov, vyfiltrovať si zápasy podľa parametrov.

## Dashboard

 -  Verzia: v1.0
 -  Scenár: 5
 -  Milestone: tba
 -  Issues
      -  tba
      
 Užívateľ si vie v GUI pozrieť jeho email, last login, terajšiu stávku, históriu stávok
