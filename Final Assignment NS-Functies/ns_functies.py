def standaardPrijs(afstandKM):
    'Gebruikt de ingevoerde afstand in kilometers op de standaardprijs uit te rekenen'

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
    'Gebruikt de ingevoerde leeftijd, weekendrit, en afstand in kilometers op de totale ritprijs uit te rekenen'

    sPrijs = standaardPrijs(afstandKM)

    if weekendrit:

        if leeftijd < 12 or leeftijd >= 65:

            korting = 0.35

        else:

            korting = 0.40

    else:

        if leeftijd < 12 or leeftijd >= 65:

            korting = 0.30

        else:

            korting = 0

    prijs = sPrijs - (sPrijs * korting)

    print(round(prijs, 2))

ritPrijs(30, True, 20)
