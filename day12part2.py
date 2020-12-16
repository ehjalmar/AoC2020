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
        self.waypointX += int(waypointX) + int(x)
        self.waypointY += int(waypointY) + int(y)
    
    def waypointXDistance(self):
        return self.waypointX - self.x
    
    def waypointYDistance(self):
        return self.waypointY - self.y
    
    
import math
import numpy as np

def rotate(origin, point, degrees):

        radians = np.deg2rad(degrees)
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(radians) * (px - ox) - math.sin(radians) * (py - oy)
        qy = oy + math.sin(radians) * (px - ox) + math.cos(radians) * (py - oy)
        return qx, qy


file=open('day12input.txt', 'r')
lines = file.readlines()
myShip = None

for line in lines:
    instructions = re.split(r'(\d+)',line)
    move = instructions[0]
    distance = int(instructions[1])
    x = y = direction = waypointX = waypointY = 0

    if myShip is None:
        myShip = Ship(90)

    if move == "N":
        waypointY = distance
    elif move == "S":
        waypointY -= distance
    elif move == "E":
        waypointX = distance
    elif move == "W":
        waypointX -= distance
    elif move == "L":
        direction -= distance
        result = rotate((myShip.x, myShip.y), (myShip.x + myShip.waypointX, myShip.y + myShip.waypointY), -direction)
        waypointX = myShip.waypointX - result[0]
        waypointY = myShip.waypointY - result[1]
    elif move == "R":
        direction += distance
        result = rotate((myShip.x, myShip.y), (myShip.x + myShip.waypointX, myShip.y + myShip.waypointY), direction)
        waypointX = myShip.waypointX - result[0]
        waypointY = myShip.waypointY - result[1]
    elif move == "F":
        if myShip.direction == 90:
            x = myShip.waypointXDistance() * distance
            y = myShip.waypointYDistance() * distance
        elif myShip.direction == 0 or myShip.direction == 360:
            x = myShip.waypointXDistance() * distance
            y = myShip.waypointYDistance() * distance
        elif myShip.direction == 270:
            x -= myShip.waypointXDistance() * distance
            y -= myShip.waypointYDistance() * distance
        elif myShip.direction == 180:
            x -= myShip.waypointXDistance() * distance
            y -= myShip.waypointYDistance() * distance

    myShip.move(x, y, waypointX, waypointY, direction)

print("Manhattan distance: " + int(abs(myShip.x) + abs(myShip.y)).__str__())