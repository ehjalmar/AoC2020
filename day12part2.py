import re

class Ship():

    def __init__(self, startDirection):
         self.x = 0
         self.y = 0
         self.direction = 90
         self.waypointX = 10
         self.waypointY = 1
    
    def move(self, x, y, waypointX, waypointY, direction):
        self.x += int(x)
        self.y += int(y)
        self.direction = (self.direction + direction) % 360
        self.waypointX = int(waypointX)
        self.waypointY = int(waypointY)
    
    def waypointXDistance(self):
        return self.waypointX - self.x
    
    def waypointYDistance(self):
        return self.waypointY - self.y
    
    
import math

def rotate(origin, point, degrees):

        radians = math.radians(degrees)

        x, y = point
        ox, oy = origin

        qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
        qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)

        return qx, qy


file=open('day12input.txt', 'r')
lines = file.readlines()
myShip = None

for line in lines:
    instructions = re.split(r'(\d+)',line)
    move = instructions[0]
    distance = int(instructions[1])
    
    if myShip is None:
        myShip = Ship(90)
    
    x = y = direction = degrees = 0
    waypointX = myShip.waypointX
    waypointY = myShip.waypointY

    if move == "N":
        waypointY = myShip.waypointY + distance
    elif move == "S":
        waypointY = myShip.waypointY - distance
    elif move == "E":
        waypointX = myShip.waypointX + distance
    elif move == "W":
        waypointX = myShip.waypointX - distance
    elif move == "L":
        degrees -= distance
        result = rotate((myShip.x, myShip.y), (myShip.waypointX, myShip.waypointY), degrees)
        waypointX = result[0]
        waypointY = result[1]
    elif move == "R":
        degrees += distance
        result = rotate((myShip.x, myShip.y), (myShip.waypointX, myShip.waypointY), degrees)
        waypointX = result[0]
        waypointY = result[1]
    elif move == "F":
        x = myShip.waypointXDistance() * distance
        y = myShip.waypointYDistance() * distance

        if myShip.direction == 90:
            waypointX += myShip.waypointXDistance() * distance   
            waypointY += myShip.waypointYDistance() * distance
        elif myShip.direction == 0 or myShip.direction == 360:
            waypointX += myShip.waypointXDistance() * distance
            waypointY += myShip.waypointYDistance() * distance
        elif myShip.direction == 270:
            waypointX -= myShip.waypointXDistance() * distance
            waypointY -= myShip.waypointYDistance() * distance
        elif myShip.direction == 180:
            waypointX -= myShip.waypointXDistance() * distance
            waypointY -= myShip.waypointYDistance() * distance
        

    myShip.move(x, y, waypointX, waypointY, direction)

print("Manhattan distance: " + int(abs(myShip.x) + abs(myShip.y)).__str__())