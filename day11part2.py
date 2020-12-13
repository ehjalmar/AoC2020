class GFG: 
      
    def __init__(self): 
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],  
                    [1, -1], [-1, -1], [-1, 1], 
                    [0, 1], [0, -1]] 
                      
    # This function searches in all 8-direction  
    # from point(row, col) in grid[][] 
    def search2D(self, grid, row, col): 
          
        # Search word in all 8 directions  
        # starting from (row, col) 
        seatsOccupied = 0
        seatsFree = 0
            
        for x, y in self.dir: 
              
            # Initialize starting point  
            # for current direction 
            rd, cd = row + x, col + y 

            seatFound = False
            index = 0

            while not seatFound:
                # If out of bound or not matched, break 
                if (0 <= rd <self.R and 
                    0 <= cd < self.C):
                    
                    if "#" == grid[rd][cd]:
                        seatsOccupied += 1
                        seatFound = True
                    elif "L" == grid[rd][cd]:
                        seatsFree += 1
                        seatFound = True
                      
                    # Moving in particular direction 
                    rd += x 
                    cd += y 
                else: 
                    break

                index += 1
        
        return seatsOccupied

                  
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

gfg = GFG() 

def rearrangeSeats(rows):
    stateChange = False
    newRows = deepcopy(rows)
    
    gfg.R = len(rows) 
    gfg.C = len(rows[0]) 
    
    for row in range(gfg.R): 
        for col in range(gfg.C): 
            currentSeat = rows[row][col]
            result = gfg.search2D(rows, row, col)

            if currentSeat == "#" and result >= 5:
                newRows[row][col] = "L"
                stateChange = True
            elif currentSeat == "L" and result == 0:
                newRows[row][col] = "#"
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
