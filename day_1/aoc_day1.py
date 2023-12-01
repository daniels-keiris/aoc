with open('/home/daniels/aoc/day_1/input.txt', 'r') as file:
    allNumbers = []

    for line in file:
        firstDigit = None
        lastDigit = None
        fullNumber = None

        for char in line:
            if char.isdigit():
                if firstDigit is None:
                    firstDigit = char

                lastDigit = char

        fullNumber = int(firstDigit + lastDigit)

        allNumbers.append(fullNumber)

sumOfAllNumbers = sum(allNumbers)

print(sumOfAllNumbers)