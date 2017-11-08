def gemiddelde():
    'reken het gemiddelde aantal letters in een zin uit'

    zin = input("Willekeurige zin: ")

    wordLen = 0

    zinSplit = zin.split()

    wordCount = len(zinSplit)

    for word in zinSplit:

        wordLen = wordLen + len(word)

    gem = wordLen / wordCount

    print(gem)

gemiddelde()
