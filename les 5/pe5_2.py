with open("kaartnummers.txt", "r") as f:
    data = f.readlines()

for line in data:
    words = line.split(',')
    name = words[1].replace('\n', '')

    sentence = str(name) + ' heeft als kaartnummer: ' + str(words[0])
    print(sentence)

f.close()
