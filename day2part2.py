file=open('day2input.txt', 'r')
lines = file.readlines()
validPasswords = 0

for line in lines:
    currentData = line.split()
    positions = currentData[0].split("-")
    currentChar = currentData[1].replace(":","")
    charsInPassword = list(currentData[2])
    position1 = int(positions[0]) - 1
    position2 = int(positions[1]) - 1
    if  (len(charsInPassword) > position1 and charsInPassword[position1] == currentChar) != ( len(charsInPassword) > position2 and charsInPassword[position2]  == currentChar):
        validPasswords += 1
        print(line)

print("Valid passwords: " + str(validPasswords))

