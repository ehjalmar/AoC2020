import re
file=open('day8input.txt', 'r')
lines = file.readlines()

visited = dict()
currentIndex = 0
accumulator = 0
notVisited = True


while notVisited:
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
        
print("Accumulator is: " + str(accumulator)) 