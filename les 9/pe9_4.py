import csv

def createcvs():

    with open('producten.csv', 'w', newline='') as f:

        fieldnames = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']

        writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)

        writer.writeheader()

        writer = csv.writer(f, delimiter=';')

        writer.writerow(('121', 'ACB123', 'Highlight Pen', '231', '0.56'))
        writer.writerow(('123', 'PQR678', 'Nietmachine', '587', '9.99'))
        writer.writerow(('128', 'ZXY163', 'Bureaulamp', '34', '19.95'))
        writer.writerow(('137', 'MLK709', 'Monitorstandaard', '66', '32.50'))
        writer.writerow(('271', 'TRS665', 'Ipad Hoes', '155', '19.01'))

#createcvs()

def opencsv():

    maxPriceList = []

    counter = 0

    with open('producten.csv', newline='') as f:

        reader = csv.reader(f, delimiter=';')

        for row in reader:

            price = row[4]

            if counter > 0:

                maxPriceList.append(price)

            counter = counter + 1

        maxPrice = max(map(float, maxPriceList))

        print(maxPriceList)
        print(maxPrice)

opencsv()
