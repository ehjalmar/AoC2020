import time

def findNextBus(orderedBuses, currentBus, startTimeBuses, isFirstBus):
    currentBusTime = startTimeBuses[currentBus]
    busPosition = departures.index(currentBus)
    bus2 = departures[busPosition + 1]
    startTimeDiff = orderedBuses.index(bus2) - orderedBuses.index(currentBus)
    nextBusTime = 0
    
    if startTimeBuses[bus2] > int(bus2) + int(bus2):
        nextBusTime = startTimeBuses[bus2]
    else:
        nextBusTime = int(bus2) + int(bus2)

    foundLast = False
    
    if isFirstBus:    
        while nextBusTime <> currentBusTime + startTimeDiff:
            while nextBusTime < currentBusTime + startTimeDiff:
                nextBusTime += int(bus2)
            if nextBusTime <> currentBusTime + startTimeDiff: # Only add if we haven´t foudn a match
                currentBusTime += int(currentBus)
        startTimeBuses[currentBus] = currentBusTime
        startTimeBuses[bus2] = nextBusTime # - int(bus2)
        foundLast = findNextBus(orderedBuses, bus2, startTimeBuses, False)[0]
    else:  
        while nextBusTime < currentBusTime + startTimeDiff:
            nextBusTime += int(bus2)
        startTimeBuses[bus2] = nextBusTime
        if nextBusTime == currentBusTime + startTimeDiff:
            if orderedBuses.index(bus2) < orderedBuses.__len__() - 1:
                foundLast = findNextBus(orderedBuses, bus2, startTimeBuses, False)[0]
            else:
                foundLast = True        
    
    return (foundLast, currentBusTime)

def findRoutes(orderedBuses, departures, startTimeBuses):
    allBusesAligned = False
    currentT = 0
    while not allBusesAligned:
        currentBus = departures[0]
        
        result = findNextBus(orderedBuses, currentBus, startTimeBuses, True)
        allBusesAligned = result[0]
        currentT = result[1]
        startTimeBuses[currentBus] = currentT + int(currentBus)

    
    print("Found last! Start time of first bus: " + currentT.__str__())

file=open('day13input.txt', 'r')
lines = file.readlines()

buses = lines[1].split(",")
departures = list()
position = 0
orderedBuses = list()
startTimeBuses = dict()

for bus in buses:
    if bus != "x":
        departures.append(bus)
        startTimeBuses[bus] = position
        position += 1
    
    orderedBuses.append(bus)

startTime = time.time()
findRoutes(orderedBuses, departures, startTimeBuses)
endTime = time.time()
print("Done processing in: " + str(endTime - startTime) + " seconds")