import re

file=open('day7input.txt', 'r')
lines = file.readlines()

rulesDict = dict()
colorsThatCanHoldGold = list()
colorsThatCanHoldGoldSummary = list()
shinyGold = "shiny gold"

def addColorsThatCanHoldGold(inputList):
    colorsThatCanHoldGoldSubLevel = list()
    for rule in rulesDict.items():
        for ruleColor in list(rule[1]):
            if ruleColor in inputList and shinyGold not in rule[0]:
                colorsThatCanHoldGoldSubLevel.append(rule[0])
                
    
    return colorsThatCanHoldGoldSubLevel

print("Rules loaded: " + str(len(lines)))

for line in lines:
    if "contain no other bags" not in line:
        bagColor = line[0:line.find("bags") - 1]
        rules = line.split(",")
 
        currentRules = list()
        for currentRule in rules:
            c = re.search(r"\d", currentRule)
            color = currentRule[c.end()+1:].replace(" bags.","").replace(" bag.","").replace("\n","").replace(" bags","").replace(" bag","")
            currentRules.append(color)
            if shinyGold in color:
                colorsThatCanHoldGold.append(bagColor)
        rulesDict[bagColor] = currentRules

colorsThatCanHoldGoldSummary.extend(colorsThatCanHoldGold)
inList = colorsThatCanHoldGold
itemsFound = len(inList)

while itemsFound > 0:
    result = addColorsThatCanHoldGold(inList)
    myset = set(result)
    itemsFound = len(myset)
    inList = list(myset)
    colorsThatCanHoldGoldSummary.extend(inList)

myset = set(colorsThatCanHoldGoldSummary)
distinctItems = len(myset)
print("Sum of distinctItems: " + str(distinctItems))