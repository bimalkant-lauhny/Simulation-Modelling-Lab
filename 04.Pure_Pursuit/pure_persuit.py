import math
import random
import sys, time
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Bomb Effect")

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

bomber = pygame.image.load("bomber.png")
bomber = pygame.transform.scale(bomber, (25, 25))

fighter = pygame.image.load("fighter.png")
fighter = pygame.transform.scale(fighter, (25, 25))

missile = pygame.image.load("missile.png")
missile = pygame.transform.scale(missile, (10, 10))

blast = pygame.image.load("blast.png")
blast = pygame.transform.scale(blast, (50, 50))

done = False

def displayBomber(pos):
    screen.blit(bomber, (pos[0], pos[1]))

def displayFighter(pos):
    screen.blit(fighter, (pos[0], pos[1]))

def displayMissile(pos):
    screen.blit(missile, (pos[0], pos[1]))

def displayBlast(pos):
    screen.blit(blast, (pos[0], pos[1]))

fighterPos = [10, 10]
bomberPos = [300, 300]
missilePos = [0, 0]
blastPos = [0, 0]

fVel = 1.0
bVel = 0.7

def newPos(pos, x, y):
    pos[0] += x
    pos[1] += y
    return pos

dist = math.sqrt( math.pow((fighterPos[1]-bomberPos[1]), 2) + math.pow((fighterPos[0]-bomberPos[0]), 2) )

while not done:
    screen.fill(white)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    
    displayFighter(fighterPos)
    displayBomber(bomberPos)

    if dist > 100:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bomberPos = newPos(bomberPos, (-1)*bVel, 0)
            elif event.key == pygame.K_RIGHT:
                bomberPos = newPos(bomberPos, (+1)*bVel, 0)
            elif event.key == pygame.K_UP:
                bomberPos = newPos(bomberPos, 0, (-1)*bVel)
            elif event.key == pygame.K_DOWN:
                bomberPos = newPos(bomberPos, 0, (+1)*bVel)
    
        dist = math.sqrt( math.pow((fighterPos[1]-bomberPos[1]), 2) + math.pow((fighterPos[0]-bomberPos[0]), 2) )

        cosTheta = (float(bomberPos[1]-fighterPos[1])) / dist
        sinTheta = (float(bomberPos[0]-fighterPos[0])) / dist

        fighterPos[0]= fighterPos[0] + fVel*sinTheta
        fighterPos[1]= fighterPos[1] + fVel*cosTheta
        missilePos[0] = fighterPos[0]
        missilePos[1] = fighterPos[1]
    
    elif dist > 2:
        dist = math.sqrt( math.pow((missilePos[1]-bomberPos[1]), 2) + math.pow((missilePos[0]-bomberPos[0]), 2) )
        missilePos[0] = missilePos[0] + fVel*sinTheta
        missilePos[1] = missilePos[1] + fVel*cosTheta
        displayMissile(missilePos)

    else:
        blastPos[0] = bomberPos[0] - 15
        blastPos[1] = bomberPos[1] - 15
        displayBlast(blastPos)

    time.sleep(0.02)
    pygame.display.flip()