import math
import random
import sys, time
import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Serial Chase")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

done = False

Apos = [300, 10]
Bpos = [10, 10]
Cpos = [10, 300]
Dpos = [300, 300]

def newPos(pos, x, y):
    pos[0] += x
    pos[1] += y
    return pos

def displayChar(color, pos):
    pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])) , 10, 0)
    
Ovel = 2.0
Dvel = 3.0

distAB = math.sqrt( math.pow((Apos[1]-Bpos[1]), 2) + math.pow((Apos[0]-Bpos[0]), 2) )
distBC = math.sqrt( math.pow((Bpos[1]-Cpos[1]), 2) + math.pow((Bpos[0]-Cpos[0]), 2) )
distCD = math.sqrt( math.pow((Cpos[1]-Dpos[1]), 2) + math.pow((Cpos[0]-Dpos[0]), 2) )

while not done:
    screen.fill(white)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    
    displayChar(green, Dpos)
    displayChar(black, Cpos)
    displayChar(red, Bpos)
    displayChar(blue, Apos)

    if distCD > 1:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bomberPos = newPos(Dpos, (-1)*Dvel, 0)
            elif event.key == pygame.K_RIGHT:
                bomberPos = newPos(Dpos, (+1)*Dvel, 0)
            elif event.key == pygame.K_UP:
                bomberPos = newPos(Dpos, 0, (-1)*Dvel)
            elif event.key == pygame.K_DOWN:
                bomberPos = newPos(Dpos, 0, (+1)*Dvel)
    
        distCD = math.sqrt( math.pow((Cpos[1]-Dpos[1]), 2) + math.pow((Cpos[0]-Dpos[0]), 2) )

        sinCD = (float(Dpos[0]-Cpos[0])) / distCD
        cosCD = (float(Dpos[1]-Cpos[1])) / distCD

        CPos = newPos(Cpos, Ovel*sinCD, Ovel*cosCD)

    if distBC > 1:

        distBC = math.sqrt( math.pow((Bpos[1]-Cpos[1]), 2) + math.pow((Bpos[0]-Cpos[0]), 2) )

        sinBC = (float(Cpos[0]-Bpos[0])) / distBC
        cosBC = (float(Cpos[1]-Bpos[1])) / distBC

        BPos = newPos(Bpos, Ovel*sinBC, Ovel*cosBC)

    if distAB > 1:

        distAB = math.sqrt( math.pow((Apos[1]-Bpos[1]), 2) + math.pow((Apos[0]-Bpos[0]), 2) )

        sinAB = (float(Bpos[0]-Apos[0])) / distAB
        cosAB = (float(Bpos[1]-Apos[1])) / distAB

        APos = newPos(Apos, Ovel*sinAB, Ovel*cosAB)

    time.sleep(0.02)
    pygame.display.flip()
