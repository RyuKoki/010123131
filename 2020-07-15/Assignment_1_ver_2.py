# File name : Assignment II
# Subject ID : 010123131 Software Development Practice I
# Date : Friday 17th July 2020
# Name : Onpinya Phokhahutthakosol
# Student ID : 62-0101262-0261

import pygame
import random

# initializwepygame
pygame.init()

# set width x height of screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))

# create new surface
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# create clock of pygame
clock = pygame.time.Clock()

x_position = []
y_position = []
position = []
radius = []
def drawCircle():
    # random position x, y of center's circle
    x = random.randint(40, WIDTH-40)
    y = random.randint(40, HEIGHT-40)
    x_position.append(x)
    y_position.append(y)
    position.append((x, y))
    # random radius
    r = random.randint(10, 20)
    radius.append(r)
    # random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(surface, color, (x, y), r)

# draw 10 circles on surface
mem_cir = 10
for i in range(mem_cir):
    drawCircle()



running = True
while running:
    clock.tick( 30 ) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with the white color
    screen.fill((255,255,255))
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    pygame.display.flip()

pygame.quit()