# dbs
najlepsi projekt z databaz

by Robo a Adam

Tabulky:
[tu](https://github.com/AdamGajdosik/dbs/files/4375838/finalihope.zip)

Dokumentácia:
[tu](https://github.com/AdamGajdosik/dbs/wiki)


Database_controller.py navod:

    hnus = Database(host,meno,heslo,meno_databazy) - vytvori objekt databazy

    hnus.connect() - pripoji do databazy

    hnus.disconnect() - odpoji od databazy

    hnus.addUser(meno,priezvisko,heslo,email,den_registracie,prihlasovacie_meno)

    hnus.listUsers() - vrati zoznam uzivatelov

Config_parser.py navod:

    ConfigParser.getDatabaseAcces() - vrati dictionary s pristupovymi udajmi do DB


