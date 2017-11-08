stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk Centraal', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = ""
eindstation = ""

def inlezen_beginstation():
    'vraagt om een beginstation en slaat deze op'

    while True:

        invoer = input('Wat is je beginstation? :')

        if invoer in stations:

            global beginstation

            beginstation = invoer

            return  beginstation

            break

        else:

            continue

def inlezen_eindstation():
    'Vraagt om een eindstation en en slaat deze op'

    while True:

        invoer = input('Wat is je eindstation? :')

        if invoer in stations:

            global eindstation

            eindstation = invoer

            if stations.index(eindstation) > stations.index(beginstation):

                return eindstation

                break

            else:

                print('Deze trein komt niet in ' + eindstation)

                continue

            break

        else:

            continue

def omroepen_reis():
    'haalt het begin en eindstation op, berekent de station nummers en de tussenstations en laat deze zien'

    beginstationindex = stations.index(beginstation) + 1
    eindstationindex = stations.index(eindstation) + 1

    stationsafstand = eindstationindex - beginstationindex

    ritprijs = stationsafstand * 5

    tussenstationslist = []

    for x in range(beginstationindex, eindstationindex - 1):
        tussenstationslist.append('-' + stations[x])

    tussenstations = '\n'.join(tussenstationslist)


    print()

    print('Het beginstation ' + str(beginstation) + ' heeft rangnummer ' + str(beginstationindex) + ' in het traject.')
    print('Het eindstation ' + str(eindstation) + ' heeft rangnummer ' + str(eindstationindex) + ' in het traject.')

    print()

    print('De afstand bedraagt ' + str(stationsafstand) + ' station(s).')

    print()

    print('De prijs van het kaartje is ' + str(ritprijs) + ' euro')

    print()

    print('Jij stapt in de trein in: ' + str(beginstation))
    print(str(tussenstations))
    print('Jij stapt uit in: ' + str(eindstation))

inlezen_beginstation()

inlezen_eindstation()

omroepen_reis()
