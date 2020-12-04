file=open('day4input.txt', 'r')
lines = file.readlines()
currentIndex = 0
passports = {}
newline = True

for line in lines:
    if line == "\n":
        currentIndex += 1
        newline = True
    else:
        if(newline):
            passports[currentIndex] = line.split()
        else:
            passports[currentIndex] += line.split()
        newline = False

requiredFields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"} #,"cid"}
validPassports = 0
for passport in passports:
    validpassport = True
    currentPassportDict = {}
    currentPassport = passports[passport]

    for foo in currentPassport:
        bar = foo.split(":")
        currentPassportDict[bar[0]] = bar[1]

    for field in requiredFields:
        if field in currentPassportDict:
            print("contains "+ field)
        else:
            print("does not contains "+ field)
            validpassport = False
    
    if(validpassport):
        validPassports += 1

print("Valid passports: " + str(validPassports))
    
