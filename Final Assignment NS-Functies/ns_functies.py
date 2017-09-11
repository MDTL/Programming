def standaardPrijs(afstandKM):

    treinritPrijs = 0.80

    if afstandKM > 50:
        treinritPrijs = 0.60
        tarief = (afstandKM * treinritPrijs) + 15
    else:
        tarief = afstandKM * treinritPrijs

    if afstandKM <= 0:
        tarief = 0

    return round(tarief, 2)

def ritPrijs(leeftijd, weekendrit, afstandKM):
    sPrijs = standaardPrijs(afstandKM)

    if weekendrit == False:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = sPrijs - ((sPrijs / 100) * 30)
        else:
            prijs = sPrijs
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = sPrijs - ((sPrijs / 100) * 35)
        else:
            prijs = sPrijs - ((sPrijs / 100) * 40)

    return round(prijs, 2)

print(ritPrijs(66, True, 20))
