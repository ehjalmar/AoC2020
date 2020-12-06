file=open('day6input.txt', 'r')
lines = file.readlines()
currentIndex = 0
groupsSums = []
groupAnswers = []
newline = True

for line in lines:
    yesAnswersInGroup = {}
    if line == "\n":
        currentGroupSum = len(dict.fromkeys(groupAnswers))
        groupsSums.append(currentGroupSum)
        groupAnswers = []
        newline = True
    else:
        for char in line:
            if char != "\n":
                groupAnswers.append(char)
        newline = False

# Add last row as well
currentGroupSum = len(dict.fromkeys(groupAnswers))
groupsSums.append(currentGroupSum)

totalSum = sum(groupsSums)
print("Summary: " + str(totalSum))