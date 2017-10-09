def code(invoerstring):

    newinvoerstring = ""

    for x in invoerstring:

        newx = chr(ord(x) + 3)

        newinvoerstring = newinvoerstring + newx

    print(newinvoerstring)

code("RutteAlkmaarDen Helder")
