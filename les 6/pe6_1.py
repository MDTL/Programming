def seizoen(maand):
    'haalt de maand op voor het gegeven nummer'
    seizoenen = ['lente', 'zomer', 'herfst', 'winter']

    if '1' in maand or '2' in maand or '3' in maand:
        maandS = seizoenen[0]

    if '4' in maand or '5' in maand or '6' in maand:
        maandS = seizoenen[1]

    if '7' in maand or '8' in maand or '9' in maand:
        maandS = seizoenen[2]

    if '10' in maand or '11' in maand or '12' in maand:
        maandS = seizoenen[3]

    print(str(maand) + ' | ' + str(maandS))

seizoen('7')
