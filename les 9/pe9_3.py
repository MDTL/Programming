import csv

with open('gamers.csv', newline='') as f:

    reader = csv.reader(f, delimiter=';')

    scorelist = []

    for x in reader:

        scorelist.append(x[2])

    maxscore = max(scorelist)


with open('gamers.csv', newline='') as f2:

    reader = csv.reader(f2, delimiter=';')

    for y in reader:

        if y[2] == maxscore:

            print('De hoogste score is: ' + y[2] + ' op ' + y[1] + ' behaald door ' + y[0])

