maxColorCount = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def getGameId(line):
    gameIdStringEndIndex = line.find(':')
    
    gameIdString = ''

    for char in line[:gameIdStringEndIndex]:
        if char.isdigit():
            gameIdString += char

    return int(gameIdString)

def isGameValid(line):
    gameIdIndex = line.find(':')
    setGroups = line[gameIdIndex + 1:].split(';')

    for setGroup in setGroups:
        colorDataList = setGroup.strip().split(',')

        for colorData in colorDataList:
            quantity, color = colorData.strip().split()

            if color in maxColorCount and int(quantity) > maxColorCount[color]:
                return False
    
    return True

with open('/home/daniels/aoc/day_2/input.txt', 'r') as file:
    validGameIds = []

    for line in file:
        gameId = getGameId(line)
        gameIsValid = isGameValid(line)
        
        if gameIsValid:
            validGameIds.append(gameId)

        

sumOfAllValidIds = sum(validGameIds)

print(sumOfAllValidIds)