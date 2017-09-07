cijferICOR = 6.0
cijferPROG = 7.5
cijferCSN = 6.5

gemiddelde = round((cijferICOR + cijferPROG + cijferCSN) / 3, 2)

beloning = (cijferICOR + cijferPROG + cijferCSN) * 30

overzicht = "Mijn cijfers (gemiddeld een " + str(gemiddelde) + ") leveren een beloning van € " + str(beloning) + " op"

print(overzicht)
