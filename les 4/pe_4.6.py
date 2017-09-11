lijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    del letterlijst[:]
    letterlijst.extend(('d', 'e', 'f'))

print(lijst)

wijzig(lijst)

print(lijst)
