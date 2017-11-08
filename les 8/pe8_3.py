def code(invoerstring):
    'gebruikt de ingevoerde string en zet de letters om naar de de waarde 3 tekens hoger'

    newinvoerstring = ""

    for x in invoerstring:

        newx = chr(ord(x) + 3)

        newinvoerstring = newinvoerstring + newx

    print(newinvoerstring)

code("RutteAlkmaarDen Helder")
