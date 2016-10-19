import pygame
import math
import sys, time

v = int(raw_input("Enter initial velocity:\n"))
g = 10.0
theta = int(raw_input("Enter the angle of inclination of the initial velocity from horizontal axis (degree):\n"))

if theta == 90:
	print "Error! tan 90 is undefined.."
	sys.exit()

theta = (math.pi * theta) / 180.0

tanTheta = math.tan(theta)
cosTheta = math.cos(theta)

saviour = (g) / (2.0 * math.pow(v, 2) * math.pow(cosTheta, 2))

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Projectile Bomb")

white = (255, 255, 255)
black = (0, 0, 0)
blue  = (0, 0, 255)
red   = (255, 0, 0)
green  = (0, 255, 0)

clock = pygame.time.Clock()
done = False
pointList = []
x = 100
y = 100
screen.fill(white)
ini = (x * tanTheta) - (math.pow(x, 2) * saviour)
iniy = 500 - int((x * tanTheta) - (math.pow(x, 2) * saviour)) + 1
tk = 0.02
while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(white)
        pygame.draw.line(screen, black, (0, iniy), (1024, iniy))
        x = x + 1
        #y = y + 1
        y = (x * tanTheta) - (math.pow(x, 2) * saviour)
        pointList.append((int(x),500-int(y)))
        tk = (500.0 - y) / 25000
        #print tk
        pygame.draw.circle(screen, blue, pointList[-1], 10, 0)

        for i in pointList:
        	pygame.draw.circle(screen, green, i, 1,0)
        
        if y < ini:
        	done = True
        	time.sleep(5)
        
        #screen.fill(white)
        pygame.display.update()
        time.sleep(tk)
