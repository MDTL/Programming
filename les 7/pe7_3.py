dictionary = {'Hans': 10.0, 'Piet': 9.5, 'Klaas': 9.0, 'Jan': 8.5, 'Sjon': 8.0, 'Wilco': 7.5, 'Menno': 7.0, 'Abel': 6.5}

for key in dictionary.items():

    if key[1] > 9.0:

        print(key[0], key[1])
