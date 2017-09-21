def gemiddelde():

    zin = input("Willekeurige zin: ")

    wordLen = 0

    zinSplit = zin.split()

    wordCount = len(zinSplit)

    for word in zinSplit:

        wordLen = wordLen + len(word)

    gem = wordLen / wordCount

    print(gem)

gemiddelde()
