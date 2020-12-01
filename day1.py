import math

file=open('day1input.txt', 'r')
lines = file.readlines()

for line in lines:
    i = 0
    while i < len(lines):
        currentNumber = int(line)
        if (currentNumber + int(lines[i])) == 2020:
            print('Found the numbers!')
            print(str(currentNumber) + ' + ' + lines[i])
            print('Multiplication is:')
            print(str(currentNumber * int(lines[i])))
        i += 1