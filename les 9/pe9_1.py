try:

    aantpersonen = int(input('Voer het aantal personen in: '))

    if aantpersonen < 0:

        print('Negatieve getallen zijn niet toegestaan!')

    else:

        hotelprijs = 4356

        kosten = round(hotelprijs / aantpersonen, 2)

        print(kosten)

except ValueError:

    print('Gebruik cijfers voor het invoeren van het aantal!')

except ZeroDivisionError:

    print('Delen door nul kan niet!')

except:

    print('Onjuiste invoer!')


