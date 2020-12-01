import math

file=open('day1input.txt', 'r')
lines = file.readlines()

for line in lines:
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines):
            currentNumber = int(line)
            if (currentNumber + int(lines[i]) + int(lines[j])) == 2020:
                print('Found the numbers!')
                print(str(currentNumber) + ' + ' + lines[i]+ ' + ' + lines[j])
                print('Multiplication is:')
                print(str(currentNumber * int(lines[i]) * int(lines[j])))
            j += 1
        i += 1