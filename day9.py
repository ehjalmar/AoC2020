file=open('day9input.txt', 'r')
lines = file.readlines()
magicNumber = 0

premable = 25

for i in range(len(lines)):
    if i >= premable:
        previousNumbers = lines[i-premable:i]
        matchFound = False

        for currentNumber in previousNumbers:
            for currentNumber2 in previousNumbers:
                if int(currentNumber) != int(currentNumber2) and int(currentNumber) + int(currentNumber2) == int(lines[i]):
                    matchFound = True
                    break
            if matchFound:
                break
        
        if not matchFound:
            magicNumber = lines[i]

print(magicNumber.__str__())