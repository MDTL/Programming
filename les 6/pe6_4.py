studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentcijfers):
    'pakt de list van cijfers en rekent het gemiddelde per student uit'

    antw = []

    for i in range(len(studentcijfers)):

        length = len(studentcijfers[i])

        som = sum(studentcijfers[i]) / length

        gem = round(som)

        antw.append(gem)

    return antw

def gemiddelde_van_alle_studenten(studentcijfers):
    'rekent het gemiddelde van alle studenten uit'

    som = 0
    count = 0

    for row in studentcijfers:
        for elem in row:
            som = som + elem
            count = count + 1
            antw = som / count

    antw = round(antw)

    return antw


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
