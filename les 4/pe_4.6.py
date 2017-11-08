lijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    'pakt de letterlijst en voegt daar een list aan toe'
    del letterlijst[:]
    letterlijst.extend(('d', 'e', 'f'))

print(lijst)

wijzig(lijst)

print(lijst)
