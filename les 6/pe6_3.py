def function(invoer):

    list = invoer.split('-')

    list.sort()

    listMin = min(list)
    listMax = max(list)

    listAantal = len(list)

    listSom = 0

    for x in list:
        listSom += int(x)

    listGem = listSom / listAantal

    print('Gesorteerde lijst van ints: ' + str(list))

    print('Grootste getal: ' + str(listMax) + ' en Kleinste getal: ' + str(listMin))

    print('Aantal getallen: ' + str(listAantal) + ' en Som van de getallen: ' + str(listSom))

    print('Gemiddelde: ' + str(listGem))

function("5-9-7-1-7-8-3-2-4-8-7-9")
