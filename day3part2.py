def countThrees(stepsRight, stepsDown):
    file=open('day3input.txt', 'r')
    lines = file.readlines()
    numberOfThrees = 0
    currentLine = 0
    currentPositionInLine = 0

    while len(lines) > currentLine:
        rowLength = 31
        if (currentPositionInLine + stepsRight) >= rowLength:
            currentPositionInLine = (stepsRight - (rowLength - currentPositionInLine))
        else:
            currentPositionInLine += stepsRight
        currentLine += stepsDown
        if currentLine < len(lines) and lines[currentLine][currentPositionInLine] == "#":
            numberOfThrees += 1
    
    return numberOfThrees

result =  countThrees(1, 1) * countThrees(3, 1) * countThrees(5, 1) *  countThrees(7, 1) *  countThrees(1, 2)

print("Number of threes: " + str(result))