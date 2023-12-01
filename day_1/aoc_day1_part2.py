def extractNumbers(line):
    wordToNumberMapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    firstNumber = None
    lastNumber = None

    currentNumber = ""

    def addCurrentNumberToList(newNumber):
        nonlocal firstNumber, lastNumber

        if newNumber:
            if firstNumber is None:
                firstNumber = newNumber
            
            lastNumber = newNumber

    def mapStringToNumber(charString):
        extractedNumber = 0

        for numberString, number in wordToNumberMapping.items():
            if numberString in charString:
                return number

        return extractedNumber

    for char in line:
        if firstNumber:
            currentNumber = ""

            break

        if char.isalpha():
            currentNumber += char.lower()
            wordToNumber = mapStringToNumber(currentNumber)

            if wordToNumber:
                addCurrentNumberToList(str(wordToNumber))

        
        if char.isdigit():
            currentNumber = str(char)
            addCurrentNumberToList(currentNumber)
            currentNumber = ""

    for char in line[::-1]:
        if char.isalpha():
            currentNumber += char.lower()
            wordToNumber = mapStringToNumber(currentNumber[::-1])

            if wordToNumber:
                addCurrentNumberToList(str(wordToNumber))

                break

        if char.isdigit():
            currentNumber = str(char)
            addCurrentNumberToList(currentNumber)

            break


    return int(firstNumber + lastNumber)

with open('/home/daniels/aoc/day_1/input.txt', 'r') as file:
    allNumbers = []

    for line in file:
        firstDigit = None
        lastDigit = None
        fullNumber = None

        allNumbers.append(extractNumbers(line))

# print(allNumbers)
sumOfAllNumbers = sum(allNumbers)

print(sumOfAllNumbers)