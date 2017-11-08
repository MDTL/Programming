def kwadraten_som(grondgetallen):
    'neemt de grondgetallen list over en rekent de kwadraten hiervan uit'
    sum = 0
    for x in grondgetallen:
        if x >= 0:
            sum += x ** 2
    return sum

list = [4, 5, 3, -81]

print(kwadraten_som(list))
