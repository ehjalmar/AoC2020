file=open('day2input.txt', 'r')
lines = file.readlines()
validPasswords = 0

for line in lines:
    currentData = line.split()
    maxminChars = currentData[0].split("-")
    currentChar = currentData[1].replace(":","")
    occurrence = currentData[2].count(currentChar)
    if occurrence >= int(maxminChars[0]) and occurrence <= int(maxminChars[1]):
        validPasswords += 1

print("Valid passwords: " + str(validPasswords))

