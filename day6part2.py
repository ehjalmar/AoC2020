file=open('day6input.txt', 'r')
lines = file.readlines()
currentIndex = 0
groupsSums = []
groupAnswers = []
newGroup = True

for line in lines:
    yesAnswersInGroup = {}
    if line == "\n":
        currentGroupSum = len(dict.fromkeys(groupAnswers))
        groupsSums.append(currentGroupSum)
        groupAnswers = []
        newGroup = True
    else:
        if newGroup: # add all chars for first row
            for char in line:
                if char != "\n":
                    groupAnswers.append(char)
        else: # remove all that doesn´t exist in this row
            groupAnswersCopy = groupAnswers[:]
            for char in groupAnswers:
                if char not in line:
                    groupAnswersCopy.remove(char)
            groupAnswers = groupAnswersCopy[:]
        newGroup = False

# Add last row as well
currentGroupSum = len(dict.fromkeys(groupAnswers))
groupsSums.append(currentGroupSum)

totalSum = sum(groupsSums)
print("Summary: " + str(totalSum))