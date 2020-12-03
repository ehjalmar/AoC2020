file=open('day3input.txt', 'r')
lines = file.readlines()

numberOfThrees = 0
currentLine = 0
currentPositionInLine = 0

stepsRight = 3
stepsDown = 1

while len(lines) > currentLine:
    rowLength = 31
    if (currentPositionInLine + stepsRight) >= rowLength:
        currentPositionInLine = (stepsRight - (rowLength - currentPositionInLine))
    else:
        currentPositionInLine += stepsRight
    currentLine += stepsDown
    if currentLine < len(lines) and lines[currentLine][currentPositionInLine] == "#":
        numberOfThrees += 1

print("Number of threes: " + str(numberOfThrees))