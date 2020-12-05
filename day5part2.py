def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1)  
                               if x not in lst] 

file=open('day5input.txt', 'r')
lines = file.readlines()
currentIndex = 0
boardingPasses = []

for line in lines:
    
    charPosition = 0
    rowNumber = 0
    maxRow = 127
    minRow = 0
    maxSeat = 7
    minSeat = 0
    seatNumber = 0
    # Get row number
    while charPosition < 7:
        currentLetter = line[charPosition]
        currentInterval = maxRow - minRow  + 1
        if currentLetter == "F":
            maxRow = (maxRow) - (currentInterval / 2)
        else:
            minRow = (minRow) + (currentInterval / 2)
        charPosition += 1
    
    rowNumber = minRow

    # Get seat number
    while charPosition < 10:
        currentLetter = line[charPosition]
        currentInterval = maxSeat - minSeat + 1
        if currentLetter == "L":
            maxSeat = (maxSeat) - (currentInterval / 2)
        else:
            minSeat = (minSeat) + (currentInterval / 2)
        charPosition += 1

    seatNumber  = maxSeat
    
    # Get seat ID
    seatId = rowNumber * 8 + seatNumber
    boardingPasses.append(seatId)
    print("seatId: " + str(seatId))


# order boarding passes
boardingPasses.sort()
print("Highest seatId: " + str(boardingPasses[-1]))

missingSeats = find_missing(boardingPasses)
print(missingSeats)
