with open("kaartnummers.txt", "r") as f:
    data = f.readlines()

    lineCount = len(data)

    print('Deze file telt ' + str(lineCount) + ' regels')

numbersList = []

for line in data:
    numbers = line.split(',')[0]

    numbersList.append(numbers)

highestNumber = max(numbersList)

f.close()

with open("kaartnummers.txt") as f:
    for num, line in enumerate(f, 1):
        if highestNumber in line:
            highestNumberLine = num

print('Het grootste kaartnummer is: ' + str(highestNumber) + ' en dat staat op regel ' + str(highestNumberLine))
