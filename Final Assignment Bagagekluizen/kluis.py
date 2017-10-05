def toon_aantal_kluizen_vrij():
    'Laat het aantal vrije kluizen zien'

    with open('kluizen.txt', 'r') as f:

        fdata = f.readlines()
        fdataCount = len(fdata)

        vrijeKluizen = 12 - int(fdataCount)

        print('Het aantal vrije kluizen: ' + str(vrijeKluizen))

def nieuwe_kluis():
    'Laat de gebruiker een code invoeren om een kluis te krijgen'

    kluisList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    with open('kluizen.txt', 'r') as f:

        fdata = f.readlines()

        for line in fdata:

            kluisBezetList = line.split()

            kluisBezet = int(kluisBezetList[0])

            kluisList.remove(kluisBezet)

        if len(kluisList) != 0:

            nieuweKluisNr = kluisList[0]
            nieuweKluisCode = input('Voer een code voor je kluis in: ')

            with open('kluizen.txt', 'a') as f:
                f.write(str(nieuweKluisNr) + ' ' + str(nieuweKluisCode) + '\n')

                print('Nieuwe kluisnr: ' + str(nieuweKluisNr) + ' | ' + ' Nieuwe kluiscode: ' + str(nieuweKluisCode))

        else:

            print('Alle kluizen zijn bezet')

def kluis_openen():
    'Laat de gebruiker zijn kluisnr en kluiscode invoeren om de kluis te openen'

    inputKluisnr = int(input('Voer uw kluisnr in: '))
    inputKluiscode = str(input('Voer uw kluiscode in: '))

    with open('kluizen.txt', 'r') as f:

        fdata = f.read()

        if (str(inputKluisnr) + ' ' + str(inputKluiscode)) in fdata:

            print('Kluis geopend')

        else:

            print('Ingevoerde gegevens kloppen niet')

def kluis_teruggeven():
    'Laat de gebruiken zijn kluisnr en kluiscode invoeren om de kluis vrij te geven'

    inputKluisnr = int(input('Voer uw kluisnr in: '))
    inputKluiscode = str(input('Voer uw kluiscode in: '))

    kluisInfo = str(inputKluisnr) + ' ' + str(inputKluiscode)

    with open('kluizen.txt', 'r') as f:

        fdata = f.read()

        if kluisInfo in fdata:

            replaceLine = fdata.replace(kluisInfo + '\n', '')

            with open('kluizen.txt', 'w') as f:

                f.write(replaceLine)

                print('Kluis teruggegeven')

print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug \n5: Ik wil stoppen \n')

while True:

    print()

    keuze = input('Voer je optie in: ')

    if keuze == '1':

        toon_aantal_kluizen_vrij()

    elif keuze == '2':

        nieuwe_kluis()

    elif keuze == '3':

        kluis_openen()

    elif keuze == '4':

        kluis_teruggeven()

    elif keuze == '5':

        break
