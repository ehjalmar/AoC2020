from copy import deepcopy

file=open('day11input.txt', 'r')
lines = file.readlines()

rows = list()

for line in lines:
    row = list()
    for char in line:
        if(char != "\n"):
            row.append(char)
    rows.append(row)


def rearrangeSeats(rows):
    stateChange = False
    newRows = deepcopy(rows)
    for i in range(rows.__len__()):
        currentRow = rows[i]
        rowAbove = list()
        rowBelow = list()
        if i > 0:
            rowAbove = rows[i - 1]
        if i < rows.__len__() -1:
            rowBelow = rows[i + 1]

        for n in range(currentRow.__len__()):
            currentSeat = currentRow[n]
            seatsOccupied = 0
            seatFree = 0

            if n == 0: # First seat on row
                m = 0
                while m < 2:
                    # row above
                    if i > 0 and rowAbove[n + m] == "L":
                        seatFree += 1
                    elif i > 0 and rowAbove[n + m] == "#":
                        seatsOccupied += 1

                    # same row
                    if  m > 0 and currentRow[n + m] == "L":
                        seatFree += 1
                    elif m > 0 and  currentRow[n + m] == "#":
                        seatsOccupied += 1

                    # row below
                    if i < (rows.__len__() -1) and rowBelow[n + m] == "L":
                        seatFree += 1
                    elif i < (rows.__len__() -1) and rowBelow[n + m] == "#":
                        seatsOccupied += 1
                    
                    m += 1

                
            elif n == currentRow.__len__() -1: # Last seat on row
                m = -1
                while m < 1:
                    # row above
                    if i > 0 and rowAbove[n + m] == "L":
                        seatFree += 1
                    elif i > 0 and rowAbove[n + m] == "#":
                        seatsOccupied += 1

                    # same row
                    if  m < 0 and currentRow[n + m] == "L":
                        seatFree += 1
                    elif m < 0 and  currentRow[n + m] == "#":
                        seatsOccupied += 1

                    # row below
                    if i < (rows.__len__() -1) and rowBelow[n + m] == "L":
                        seatFree += 1
                    elif i < (rows.__len__() -1) and rowBelow[n + m] == "#":
                        seatsOccupied += 1
                    
                    m += 1
            
            else: # normal row
                m = -1
                while m < 2:
                    # row above
                    if i > 0 and rowAbove[n + m] == "L":
                        seatFree += 1
                    elif i > 0 and rowAbove[n + m] == "#":
                        seatsOccupied += 1

                    # same row
                    if  (m < 0 or m > 0) and currentRow[n + m] == "L":
                        seatFree += 1
                    elif (m < 0 or m > 0) and  currentRow[n + m] == "#":
                        seatsOccupied += 1

                    # row below
                    if i < (rows.__len__() -1) and rowBelow[n + m] == "L":
                        seatFree += 1
                    elif i < (rows.__len__() -1) and rowBelow[n + m] == "#":
                        seatsOccupied += 1
                
                    m += 1

            if currentSeat == "#" and seatsOccupied >= 4:
                newRows[i][n] = "L"
                stateChange = True
            elif currentSeat == "L" and seatsOccupied == 0:
                newRows[i][n] = "#"
                stateChange = True

    return (newRows, stateChange)

stateChange = True

while stateChange:
    result = rearrangeSeats(rows)
    rows = result[0]
    stateChange = result[1]

seatsOccupied = 0
for row in rows:
    for seat in row:
        if seat == "#":
            seatsOccupied += 1


print("Result: " + seatsOccupied.__str__())
