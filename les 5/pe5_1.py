def convert(tempC):
    'draait temp in celcius om in fahrenheit'
    tempF = (tempC * 1.8) + 32

    return tempF


def table():
    'veranderd celsius in fahrenheit en print dit uit'
    for i in range(-30, 40, 10):

        iF = convert(i)
        print(str(iF) + "   " + str(i))

table()
