uurLoon = float(input('Wat verdien je per uur: '))
aantalUur = int(input('Hoeveel uur heb je gewerkt: '))

salaris = uurLoon * aantalUur

salarisString = str(aantalUur) + " uur werken levert €" + str(salaris) + " euro op"

print(salarisString)
