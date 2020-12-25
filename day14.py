import re
file=open('day14input.txt', 'r')
lines = file.readlines()

mask = ""
memory = dict()

for line in lines:
    currentLine = line.rstrip().replace("=","")
    splittedLine = currentLine.split()

    if currentLine.startswith("mask"):
        mask = currentLine.split()[1]
    else:
        address = int(re.search(r'\[([^]]+)', splittedLine[0]).group(1))
        value = int(splittedLine[1])
        binaryValue = list('{0:036b}'.format(value))

        for i in range(mask.__len__()):
            currentMaskChar = mask[i]
            if currentMaskChar == "0":
                binaryValue[i] = "0"
            elif currentMaskChar == "1":
                binaryValue[i] = "1"
        
        newNumeric = int("".join(binaryValue), 2)
        memory[address] = newNumeric

print(sum(memory.values()))
