def getAccumulatedAndIndex(lines):
    notVisited = True
    accumulator = 0
    visited = dict()
    currentIndex = 0

    while notVisited:
        if currentIndex >= len(lines):
            break

        if currentIndex in visited:
            notVisited = True
            break

        visited[currentIndex] = 1
        
        line = lines[currentIndex]
        instructions = line.split()
        action = instructions[0]
        arg = instructions[1]
        argType = arg[0]
        size = int(arg[1:])

        if action == "nop":
            currentIndex += 1
        elif action == "acc":
            if argType == "+":
                accumulator += size
            else:
                accumulator -= size
            currentIndex += 1
        elif action == "jmp":
            if argType == "+":
                currentIndex += size
            else:
                currentIndex -= size
        
    return (accumulator, currentIndex)

file=open('day8input.txt', 'r')
lines = file.readlines()

currentIndex = 0
accumulator = 0
lastLineIndex = len(lines) - 1
notVisited = True
exclude = dict()
nopLines = list()

for i in range(len(lines)):
    if lines[i].startswith("jmp"):
        nopLines.append(i)

for i in range(len(nopLines)):
    linesCopy = lines[:]
    linesCopy[nopLines[i]] = str(linesCopy[nopLines[i]]).replace("jmp", "nop")
    result = getAccumulatedAndIndex(linesCopy)
    if int(result[1]) > 628:
        print("jmp change to nop on line: " + str(nopLines[i]) + " accumulator: " + str(result[0]) + " resulting index: " + str(result[1]))

for i in range(len(lines)):
    if lines[i].startswith("nop"):
        nopLines.append(i)

for i in range(len(nopLines)):
    linesCopy = lines[:]
    linesCopy[nopLines[i]] = str(linesCopy[nopLines[i]]).replace("nop", "jmp")
    result = getAccumulatedAndIndex(linesCopy)
    if int(result[1]) > 628:
        print("nop change to jmp on line: " + str(nopLines[i]) + " accumulator: " + str(result[0]) + " resulting index: " + str(result[1]))

