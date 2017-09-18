def convert(tempC):
    tempF = (tempC * 1.8) + 32

    return tempF


def table():
    for i in range(-30, 40, 10):

        iF = convert(i)
        print(str(iF) + "   " + str(i))

table()
