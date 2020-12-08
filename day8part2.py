import re

class Argument(object):
    def __init__(self, line):
        self.instructions = line.split()
        self.action = self.instructions[0]
        self.arg = self.instructions[1]
        self.argType = self.arg[0]
        self.size = int(self.arg[1:])

file=open('day8input.txt', 'r')
lines = file.readlines()

currentIndex = 0
accumulator = 0
lastLineIndex = len(lines) - 1
notVisited = True
exclude = dict()

def findPointers(lines, min, max, exlude):
    for i in range(len(lines)):
        line = lines[i]
        args = Argument(line)

        if i not in exclude and (i < min or i > max) and (args.action == "nop" or args.action == "jmp") and (args.argType == "+" and ((i + args.size) <= min and (i + args.size) >= min) or (args.argType == "-" and (i - args.size) <= max and (i - args.size) >= min)):
            print(args.action + " that points to Row "+ str(min) + " - " + str(max) + ": " + str(i + 1))
            
            nextHopFound = False
            nextMin = 0
            nextMax = 0
            foo = 1
            while (i + foo) < len(lines) and not nextHopFound:
                if Argument(lines[i - foo]).action == "jmp":
                    nextHopFound = True
                    break
                foo += 1
            nextMin = i - foo + 1
            
            nextHopFound = False
            while (i + foo) < len(lines) and not nextHopFound:
                if Argument(lines[i + foo]).action == "jmp":
                    nextHopFound = True
                    break
                foo += 1
            nextMax = i + foo - 1
            exclude[i] = 1
            findPointers(lines, nextMin, nextMax, exlude)
            exclude.pop(i)

findPointers(lines, 628, 634, exclude)

