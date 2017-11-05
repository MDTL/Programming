import xmltodict

with open('stationslijsten.xml') as f:

    doc = xmltodict.parse(f.read())

    print('Alle stations Codes en Types:')

    for station in doc['Stations']['Station']:

        print(station['Code'])
        print(station['Type'])

        print()

    print('Alle Stations Codes en Synoniemen:')

    for station in doc['Stations']['Station']:

        print(station['Code'])

        if station['Synoniemen'] is not None:

            synoniemenlength = len(station['Synoniemen']['Synoniem'])

            x = 0

            while x < synoniemenlength:

                print(station['Synoniemen']['Synoniem'][x])

                x = x + 1

            print()

        else:

            print('')

    print('Alle stations Codes en Lange Namen:')

    for station in doc['Stations']['Station']:

        print(station['Code'])

        print(station['Namen']['Lang'])

        print()
