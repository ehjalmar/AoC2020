import re
file=open('day8input.txt', 'r')
lines = file.readlines()

visited = dict()
currentIndex = 0
accumulator = 0
lastLineIndex = len(lines) - 1
notVisited = True

for i in range(len(lines)):
    line = lines[i]
    instructions = line.split()
    action = instructions[0]
    arg = instructions[1]
    argType = arg[0]
    size = int(arg[1:])
    if action == "jmp" and (i + size) > 628 and (i + size) < 640:
        print("Row: " + str(i + 1)) # 95
    if (i + size) == 629:
        print("Row: " + str(i + 1)) #95 jmp +535
    if action == "jmp" and (((i + size) <= 94 and (i + size) >= 91) or ((i - size) <= 94 and (i - size) >= 91)):
        print("I <= 94 and I >= 91 Row: " + str(i + 1)) #118 jmp -26
    if (((i + size) == 117) or ((i - size) == 117)):
        print("I -> 117 Row: " + str(i + 1)) #
   
    # if action == "nop" and (i + size) == lastLineIndex:
    #     print("Row: " + str(i + 1))
    # elif action == "jmp" and (i + 1) == lastLineIndex:
    #     print("Row: " + str(i + 1))

# while currentIndex <= lastLineIndex:
#     if currentIndex in visited:
#         notVisited = True
#         break

#     visited[currentIndex] = 1

#     line = lines[currentIndex]
#     instructions = line.split()
#     action = instructions[0]
#     arg = instructions[1]
#     argType = arg[0]
#     size = int(arg[1:])

#     if action == "nop":
#         currentIndex += 1
#     elif action == "acc":
#         if argType == "+":
#             accumulator += size
#         else:
#             accumulator -= size
#         currentIndex += 1
#     elif action == "jmp":
#         if argType == "+":
#             currentIndex += size
#         else:
#             currentIndex -= size
        
print("Accumulator is: " + str(accumulator)) 