stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = ""
eindstation = ""

def inlezen_beginstation():

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

    beginstationindex = stations.index(beginstation) + 1
    eindstationindex = stations.index(eindstation) + 1

    stationsafstand = eindstationindex - beginstationindex

    ritprijs = stationsafstand * 5

    tussenstationsindex = range(beginstationindex + 1, eindstationindex - 1)

    tussenstationslist = []

    for x in tussenstationsindex:
        tussenstationslist.append(stations[x])

    tussenstations = ', '.join(tussenstationslist)

    print()

    print('Het beginstation ' + str(beginstation) + ' heeft rangnummer ' + str(beginstationindex) + ' in het traject.')
    print('Het eindstation ' + str(eindstation) + ' heeft rangnummer ' + str(eindstationindex) + ' in het traject.')

    print()

    print('De afstand bedraagt ' + str(stationsafstand) + ' station(s).')

    print()

    print('De prijs van het kaartje is ' + str(ritprijs) + ' euro')

    print()

    print('Jij stapt in de trein in: ' + str(beginstation))
    print('Tussenstations: ' + str(tussenstations))
    print('Jij stapt uit in: ' + str(eindstation))

inlezen_beginstation()

inlezen_eindstation()

omroepen_reis()
