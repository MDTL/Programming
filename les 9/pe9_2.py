import datetime
import csv


bestand = 'inloggers.csv'

while True:

    naam = input("Wat is je achternaam? ")

    if naam == 'einde':

        break

    else:

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        time = datetime.datetime.today()
        timeNow = time.strftime("%a %d %b %Y at %H:%M:%S")

        list = []

        list.append(timeNow)
        list.append(voorl)
        list.append(naam)
        list.append(gbdatum)
        list.append(email)

        csv.register_dialect('myDialect', delimiter = ';', quoting=csv.QUOTE_NONE)

        f = open('inloggers.csv', 'a', newline='\n')

        with f:

            writer= csv.writer(f, dialect='myDialect')

            writer.writerow(list)

        print()
