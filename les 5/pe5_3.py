with open("kaartnummers.txt", "r") as f:
    data = f.readlines()

    lineCount = str(len(data))

    print('Deze file telt ' + lineCount + ' regels')

numbersList = []

for line in data:
    numbers = line.split(',')[0]

    numbersList.append(numbers)

highestNumber = str(max(numbersList))

f.close()

with open("kaartnummers.txt") as f:
    for num, line in enumerate(f, 1):
        if highestNumber in line:
            highestNumberLine = str(num)

print('Het grootste kaartnummer is: ' + highestNumber + ' en dat staat op regel ' + highestNumberLine)

f.close()
