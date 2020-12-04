import re

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
            currentFieldValue = currentPassportDict[field]
            if field == "byr":
                if int(currentFieldValue) < 1920 or int(currentFieldValue) > 2002:
                    validpassport = False
            if field == "iyr":
                if int(currentFieldValue) < 2010 or int(currentFieldValue) > 2020:
                    validpassport = False
            if field == "eyr":
                if int(currentFieldValue) < 2020 or int(currentFieldValue) > 2030:
                    validpassport = False
            if field == "hgt":
                if currentFieldValue.endswith("in"): 
                    indexOfIn = currentFieldValue.find("in")
                    value = int(currentFieldValue[:indexOfIn])
                    if value < 59 or value > 76:
                        validpassport = False
                elif currentFieldValue.endswith("cm"):
                    indexOfCm = currentFieldValue.find("cm")
                    value = int(currentFieldValue[:indexOfCm])
                    if value < 150 or value > 193:
                        validpassport = False
                else:
                    validpassport = False
            if field == "hcl":
                if re.match("^#[0-9,a-f]{6}", currentFieldValue) is None:
                    validpassport = False
            if field == "ecl":
                allowedColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if currentFieldValue not in allowedColors:
                    validpassport = False
            if field == "pid":
                if re.match("^[0-9]{9}$", currentFieldValue) is None:
                    validpassport = False
        else:
            print("does not contain "+ field)
            validpassport = False
    
    if(validpassport):
        validPassports += 1

print("Valid passports: " + str(validPassports))
    
