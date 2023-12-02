def getPowerOfSetOfCubes(line):
    minimumCubeCount = 1
    minimumCubeCountMapping = {
        'red': None,
        'blue': None,
        'green': None,
    }

    gameIdIndex = line.find(':')
    setGroups = line[gameIdIndex + 1:].split(';')

    for setGroup in setGroups:
        colorDataList = setGroup.strip().split(',')

        for colorData in colorDataList:
            quantity, color = colorData.strip().split()

            if color in minimumCubeCountMapping and (minimumCubeCountMapping[color] is None or minimumCubeCountMapping[color] < int(quantity)):
                minimumCubeCountMapping[color] = int(quantity)

    
    for value in minimumCubeCountMapping.values():
        minimumCubeCount *= value

    return minimumCubeCount


with open('/home/daniels/aoc/day_2/input.txt', 'r') as file:
    totalMinimumCubeCount = 0

    for line in file:
        minimumCubeCount = getPowerOfSetOfCubes(line)

        totalMinimumCubeCount += minimumCubeCount

        
print(totalMinimumCubeCount)