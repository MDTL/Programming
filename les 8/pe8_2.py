import random

def monopolyworp():

    eersteDobbel = [random.randint(0,6), random.randint(0,6)]

    print('Eerste dobbel: ' + str(eersteDobbel))

    if eersteDobbel[0] == eersteDobbel[1]:

        print('Gelijke eerste dobbel')

        print()

        tweedeDobbel = [random.randint(0,6), random.randint(0,6)]

        print('Tweede dobbel: ' + str(tweedeDobbel))

        if tweedeDobbel[0] == tweedeDobbel[1]:

            print('Gelijke tweede dobbel')

            print()

            derdeDobbel = [random.randint(0,6), random.randint(0,6)]

            print('Derde dobbel: ' + str(derdeDobbel))

            print()

            if derdeDobbel[0] == derdeDobbel[1]:

                print('Gelijke derde dobbel, naar de gevangenis')


monopolyworp()
