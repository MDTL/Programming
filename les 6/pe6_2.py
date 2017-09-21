list = eval(input('Geef lijst met minimaal 10 strings: '))

newList = []

for x in list:
    if len(x) == 4:

        newList.append(x)

print('De nieuwe gemaakte lijst met alle vier-letter strings is: ' + str(newList))
