file=open('day10input.txt', 'r')
lines = file.readlines()
adapters = [int(i) for i in lines] 
adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

totalPaths = [0] * len(adapters)
totalPaths[0] = 1

for i in range(len(adapters)):
    # Connection 3 step back?
    if (i - 1) >= 0 and adapters[i - 1] >= (adapters[i] - 3):
        totalPaths[i] += totalPaths[i - 1]
    # Connection 3 steps back? 
    if (i - 2) >= 0 and adapters[i - 2] >= (adapters[i] - 3):
        totalPaths[i] += totalPaths[i - 2]
    # Connection 3 steps back? 
    if (i - 3) >= 0 and adapters[i - 3] >= (adapters[i] - 3):
        totalPaths[i] += totalPaths[i - 3]


print("paths: " + totalPaths[-2].__str__())

