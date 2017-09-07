meerderjarig = input('Geef je leeftijd: ')
paspoort = input('Nederlands paspoort: ')

if meerderjarig >= '18' and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas, je mag niet stemmen!')
