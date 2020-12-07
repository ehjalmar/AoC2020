import re
file=open('day7input.txt', 'r')
lines = file.readlines()
totalNumberOfBags = 0

def addBags(rules):
    currentColors = list()
    numberOfBags = 0
    for currentRule in rules:
            c = re.search(r"\d", currentRule)
            currentCount = int(currentRule[c.start():c.end()])
            color = currentRule[c.end()+1:].replace(" bags.","").replace(" bag.","").replace("\n","").replace(" bags","").replace(" bag","")
            for i in range(currentCount):
                currentColors.append(color)
            numberOfBags += currentCount
    return (currentColors, numberOfBags)

colorsToProcess = ["shiny gold"]
while len(colorsToProcess) > 0:
    colorsToProcessOriginal = colorsToProcess[:]
    colorsToProcess = []
    for currentColor in colorsToProcessOriginal:
        for line in lines:
            if "contain no other bags" not in line:
                bagColor = line[0:line.find("bags") - 1]
                rules = line.split(",")

                if rules[0].startswith(currentColor):
                    result = addBags(rules)
                    totalNumberOfBags += result[1]
                    newColors = result[0]
                    colorsToProcess += newColors[:]
        
print("Total number of bags: " + str(totalNumberOfBags))