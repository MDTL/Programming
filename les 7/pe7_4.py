def ticker(filename):
    'haalt de gegevens uit het bestand op en zet deze in een dictionary'

    with open(filename, "r") as f:

        data = f.readlines()

        list = []

        dict = {}

        for x in data:

            listS = x.split(':')

            list.append(listS)

        for x in list:

            stripx = str(x[1]).strip('\n')

            dict.update({x[0] : stripx})

        return dict

def getTickers():
    'gebruikt de dictionary op de gegevens te laten zien.'

    dict = ticker('tickers.txt')

    getcompanyname = input('Enter company name: ')

    if getcompanyname in dict:

        tickername = dict[getcompanyname]

        print('Ticker symbol: ' + tickername)

    print()

    gettickername = input('Enter ticker symbol: ')

    for key, val in dict.items():

        if val == gettickername:

            print('Company name: ' + key)

getTickers()





