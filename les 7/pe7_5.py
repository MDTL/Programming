def namen():

    list = []

    dict = {}

    while True:

        studentnaam = input('Volgende naam: ')

        if studentnaam != '':

            list.append(studentnaam)

        else:

            break

    for x in list:

        name = x
        namecount = list.count(x)

        dict.update({name : namecount})

    for key, val in dict.items():

        print('De naam ' + key + ' komt ' + str(val) + ' keer voor')

namen()
