file=open('day9input.txt', 'r')
lines = file.readlines()
magicNumber = 0

target = 1492208709

for i in range(len(lines)):
    currentSum = int(lines[i])
    steps = 0
    while currentSum < target:
        steps += 1
        currentSum += int(lines[i + steps])
        

    if currentSum == target:
        print("currentIndex: " + i.__str__())
        print("steps: " + steps.__str__())
        currentLines = lines[i:i+steps + 1]
        for i in range(0, len(currentLines)): 
            currentLines[i] = int(currentLines[i]) 
        currentLines.sort()
        magicNumber = int(currentLines[0]) + int(currentLines[-1])
        break

print(magicNumber.__str__())