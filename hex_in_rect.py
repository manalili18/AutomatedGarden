#!/usr/bin/python3

import sys
import math

global bedx
global bedy

bedx = float(sys.argv[1])
bedy = float(sys.argv[2])

yspacing = float(sys.argv[3])
p2edge = float(yspacing) / 2.0
p2vert = float(yspacing) / math.sqrt(3.0) 

xspacing = p2vert * 3.0

global curx
global cury

curx = p2edge
cury = p2edge


def inBounds():

    if curx < bedx - yspacing/2.1 and curx >  yspacing/2.1:
        if cury < bedy - yspacing/2.1 and cury > yspacing/2.1:
            return True
    return False

if(not inBounds()):
    print('Need a bigger area...')
    exit()


# find number of rows a
numrowsA = 0
while(inBounds()):
    numrowsA += 1
    cury += yspacing

# reset position for rows b
curx += p2vert * 1.5
cury = p2edge * 2.0

# find number of rows b
numrowsB = 0
while(inBounds()):
    numrowsB += 1
    cury += yspacing

# reset position for cols a
curx = p2edge
cury = p2edge

# find number of cols a
numcolsA = 0
while(inBounds()):
    numcolsA += 1
    curx += xspacing

# reset position for cols b
curx = p2vert * 1.5 + p2edge
cury = p2edge * 2.0

# find number of cols b
numcolsB = 0
while(inBounds()):
    numcolsB += 1
    curx += xspacing

print(numrowsA,numcolsA,numrowsB,numcolsB)
print(numrowsA*numcolsA+numrowsB*numcolsB)
