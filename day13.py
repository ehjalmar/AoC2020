file=open('day13input.txt', 'r')
lines = file.readlines()

earliestTimestamp = int(lines[0])
print("earliestTimestamp: " + earliestTimestamp.__str__())

buses = lines[1].split(",")
departures = dict()

for bus in buses:
    if bus == "x":
        continue

    totalTime = 0

    while totalTime < earliestTimestamp:
        totalTime += int(bus)
    
    departures[bus] = totalTime

sortedDepartures = sorted(departures, key=departures.get)
earliestBus = sortedDepartures[0]
earliestBusTimestamp = int(departures[earliestBus])
result = (earliestBusTimestamp - earliestTimestamp) * int(earliestBus)
print("(earliestBus - earliestTimestamp) * earliestBus: " + result.__str__())