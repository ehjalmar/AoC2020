file=open('day10input.txt', 'r')
lines = file.readlines()
adapters = [int(i) for i in lines] 
adapters.sort()

oneJolts = 0
threeJolts = 1
currentIndex = 0

for adapter in adapters:
    diff = adapter - currentIndex
    if diff == 1:
        oneJolts += 1
    elif diff == 3:
        threeJolts += 1
    else:
        raise Exception("Could not determine JoltType!")
    
    currentIndex = adapter


print("built-in joltage adapter output(highest + 3) " + str(adapters[-1] + 3))
print("oneJolts " + oneJolts.__str__())
print("threeJolts " + threeJolts.__str__())
print("oneJolts * threeJolts = " + str(oneJolts * threeJolts))
