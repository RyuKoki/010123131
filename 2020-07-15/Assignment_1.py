#++++++++++++++++++++++++++++++++++++++++++++++++++
# File name : Assignment I
# Subject ID : 010123131 Software Development Practice I
# Date : Wednesday 15th July 2020
# Name : Onpinya Phokhahutthakosol
# Student ID : 62-0101262-0261
#++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++
# Source code from : Dr.Rawat Siripokarpirom
# File name : pygame_demo-1.py
#++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++
# Importing all of libraries that have to use in this program
import pygame
import random

# Initialize PyGame
pygame.init()

# Set name of program
pygame.display.set_caption("Circles Game")

# Set the size of screen
HEIGHT, WIDTH = 600, 800
screen = pygame.display.set_mode( (WIDTH, HEIGHT))

# Create a clock
clock = pygame.time.Clock()

# Set FRAME RATE (FPS) 30 frames per second
FPS = 10

# Lists for getting positions (x, y) and radius (r) of circles
x_positions = []
y_positions = []
radius = []
draw_lists = []
def drawCircles():
    num_circle = 10
    for item in range(num_circle):
        x = random.randint(0, WIDTH-50)
        y = random.randint(0, HEIGHT-50)
        r = random.randint(10, 50) # Radius 10 to 20 pixels

        if x not in x_positions:
            x_positions.append(x)
            y_positions.append(y)
            radius.append(r)
        else:
            getPosition()

        # Randomise color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        drawing = pygame.draw.circle( screen, color, (x, y), r )
        draw_lists.append(drawing)
        pygame.display.update()
    return 0

def getLargestRadius():
    index_largest_radius = radius.index(max(radius))
    return radius[index_largest_radius]

def getLargestCircle():
    index_largest_circle = draw_lists.index(max(draw_lists))
    return draw_lists[index_largest_circle]

def delCircle():
    circle = getLargestRadius()
    index = radius.index(circle)
    draw_lists.remove(draw_lists[index])
    radius.remove(radius[index])
    x_positions.remove(x_positions[index])
    y_positions.remove(y_positions[index])
    return 0

# Drawing Circles
drawCircles()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            get_largest_circle = getLargestCircle()
            get_largest_radius = getLargestRadius()
            if get_largest_circle.collidepoint(mouse_position):
                pygame.draw.circle(screen, (0, 0, 0), mouse_position, get_largest_radius)
                delCircle()
    pygame.display.update()
pygame.quit()
#++++++++++++++++++++++++++++++++++++++++++++++++++
