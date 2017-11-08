import csv

def artikels_toevoegen():
    'Voegt de artikelen toe aan een csv bestand'
    with open('producten.csv', 'w', newline='') as artikel:
        fieldnames = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
        writer = csv.DictWriter(artikel, delimiter=';', fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Artikelnummer': 121, 'Artikelcode': 'ABC123', 'Naam': 'Highlight pen','Voorraad': 231, 'Prijs': 0.56})
        writer.writerow({'Artikelnummer': 123, 'Artikelcode': 'PQR678', 'Naam': 'Nietmachine', 'Voorraad': 587, 'Prijs': 9.99})
        writer.writerow({'Artikelnummer': 128, 'Artikelcode': 'ZYX163', 'Naam': 'Bureaulamp', 'Voorraad': 34, 'Prijs': 19.95})
        writer.writerow({'Artikelnummer': 137, 'Artikelcode': 'MLK709', 'Naam': 'Monitorstandaard', 'Voorraad': 66, 'Prijs': 32.50})
        writer.writerow({'Artikelnummer': 271, 'Artikelcode': 'TR665', 'Naam': 'Ipad hoes', 'Voorraad': 155, 'Prijs': 19.01})

artikels_toevoegen()

with open('producten.csv', 'r') as product:
    reader = csv.DictReader(product, delimiter=';')

    productList = []
    prijsList = []
    voorraadList= []

    for row in reader:

        prijsList += [float(row['Prijs'])]
        productList += [row]
        voorraadList += [int(row['Voorraad'])]

    hoogste_prijs = max(prijsList)
    min_voorraad = min(voorraadList)
    totale_voorraad = sum(voorraadList)

    for art in productList:
        if hoogste_prijs == float(art['Prijs']):
            print('Het duurste artikel is {} en die kost {} Euro'.format(art['Naam'], art['Prijs']))

        if min_voorraad == int(art['Voorraad']):
            print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(art['Voorraad'], art['Artikelnummer']))

    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totale_voorraad))
