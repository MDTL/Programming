import os, datetime

time = datetime.datetime.today()
timeNow = time.strftime("%a %d %b %Y, %H:%M:%S")

hNaam = input('Hardlopers naam: ')

if os.path.isfile("hardlopers.txt"):

    with open("hardlopers.txt", 'a') as f:

        newH = str("\n" + timeNow) + ", " + str(hNaam)

        f.write(newH)

        f.close()

else:

    with open("hardlopers.txt", "w") as f:

        newH = str(timeNow) + ", " + str(hNaam)

        f.write(newH)

        f.close()
