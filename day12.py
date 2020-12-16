from enum import Enum
import re

class Direction(Enum):
    EAST = 0
    WEST = 1
    NORTH = 2
    SOUTH = 3

# class ship
class Ship():

    def __init__(self, startDirection):
         self.x = 0
         self.y = 0
         self.direction = 90 #Direction.EAST
    
    def move(self, x, y, direction):
        self.x += int(x)
        self.y += int(y)
        self.direction = (self.direction + direction) % 360
        
    

file=open('day12input.txt', 'r')
lines = file.readlines()
myShip = None

for line in lines:
    instructions = re.split(r'(\d+)',line)
    move = instructions[0]
    distance = int(instructions[1])
    x = y = direction = forward = 0

    if myShip is None:
        myShip = Ship(90)

    if move == "N":
        y = distance
    elif move == "S":
        y -= distance
    elif move == "E":
        x = distance
    elif move == "W":
        x -= distance
    elif move == "L":
         direction -= distance
    elif move == "R":
        direction += distance
    elif move == "F":
        if myShip.direction == 90:
            x = distance
        elif myShip.direction == 0 or myShip.direction == 360:
            y = distance
        elif myShip.direction == 270:
            x -= distance
        elif myShip.direction == 180:
            y -= distance

    myShip.move(x, y, direction)

print("Manhattan distance: " + int(abs(myShip.x) + abs(myShip.y)).__str__())


# räkna ut Manhattan distance