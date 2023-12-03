def getValidNumbersFromCurrentLine(currentLine, previousLine, nextLine):
    validNumbers = []
    allNumberDataInLine = []
    currentNumber = ''

    for i, char in enumerate(currentLine):
        if char.isdigit():
            currentNumber += char
        elif currentNumber:
            startingPosition = i - len(currentNumber) 
            endingPosition = i 

            number = int(currentNumber)
            allNumberDataInLine.append({'startingPosition': startingPosition, 'endingPosition': endingPosition, 'number': number})

            currentNumber = ''

    if currentNumber:
        startingPosition = len(currentLine) - len(currentNumber)
        endingPosition = len(currentLine)

        number = int(currentNumber)
        allNumberDataInLine.append({'startingPosition': startingPosition, 'endingPosition': endingPosition, 'number': number})


    def isValidNumberInCurrentLine(line, startingPos, endingPos):
        startingPos = max(0, startingPos - 1)
        endingPos = min(endingPos, len(line))

        if startingPos >= 0 and line[startingPos].isascii() and line[startingPos] != '.' and not line[startingPos].isdigit():
            return True

        if endingPos < len(line) and line[endingPos].isascii() and line[endingPos] != '.' and line[endingPos] != '\n' and not line[endingPos].isdigit():
            return True

    
    def isValidNumberInAdjacentLines(line, startingPos, endingPos):
        startingPos = max(0, startingPos - 1)
        for char in line[startingPos:endingPos]:
            if char.isascii() and char != '.' and char != '\n' and not char.isdigit():
                return True

        return False

    for numberData in allNumberDataInLine:
        isValidInCurrentLine = isValidNumberInCurrentLine(currentLine, numberData['startingPosition'], numberData['endingPosition'])
        if isValidInCurrentLine:
            validNumbers.append(numberData['number'])

            continue

        if previousLine:
            isValidInPreviousLine = isValidNumberInAdjacentLines(previousLine, numberData['startingPosition'], numberData['endingPosition'] + 1)
            if isValidInPreviousLine:
                validNumbers.append(numberData['number'])

                continue

        if nextLine:
            isValidInNextLine = isValidNumberInAdjacentLines(nextLine, numberData['startingPosition'], numberData['endingPosition'] + 1)
            if isValidInNextLine:
                validNumbers.append(numberData['number'])

                continue

    return validNumbers

with open('day_3/input.txt', 'r') as file:
    allLines = file.readlines()
    allNumberData = []

    for i, line in enumerate(allLines):
        previousLine = []
        nextLine = []

        if i > 0:
            previousLine = allLines[i - 1]

        if i < len(allLines) - 1:
            nextLine = allLines[i + 1]

        allNumberData.append(getValidNumbersFromCurrentLine(line, previousLine, nextLine))

validNumberSum = 0
for numberData in allNumberData:
    validNumberSum += sum(numberData)

print(validNumberSum)