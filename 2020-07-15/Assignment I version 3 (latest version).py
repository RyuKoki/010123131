###################################################################################################
# Writer : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# Subject ID : 010123131 Software Development Practice I
# File Name : Assignment I version 3 (latest version).py
###################################################################################################

# import all of libraries for using in this program
import pygame
import random

# setting width, height and frame per second
WIDTH, HEIGHT, FPS = 800, 600, 5

# initialize pygame
pygame.init()

# setting width x height of screen
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# setting color of screen
screen.fill((255, 255, 255))
# setting name of screen
pygame.display.set_caption('Hidden Circle Game')
# setting clock for pygame
clock = pygame.time.Clock()

# creating class name 'Circle' for drawing circles
class Circle():

    def __init__(self):
        # random x point on x-axis between 20 to width-20 pixels. Because of protecting to draw out of frame's screen
        self.x = random.randint(20, WIDTH-20)
        # random y point on y-axis between 20 to height-20 pixels. This is the same reason of random x point
        self.y = random.randint(20, HEIGHT-20)
        # random radius for each circle
        self.radius = random.randint(10, 20)
        # random color for each circle
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def draw(self):
        # 'draw_circle' method in 'Circle' class for using PyGame to draw circle
        draw_circle = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.display.update()
        return draw_circle

    def hidden(self):
        # 'hidden_circle' method in 'Circle' class for using PyGame to draw circle for hidden the largest circle
        hidden_circle = pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        pygame.display.update()
        return hidden_circle

# 'checkOverlap' function for checking when each circles overlapped
def checkOverlap(x1, y1, diameter1, x2, y2, diameter2):
    r1 = diameter1 / 2
    r2 = diameter2 / 2
    if ( ( (x1-x2)**2 + (y1-y2)**2 ) >= (r1+r2)**2 ):
        return True
    elif ( ( (x1-x2)**2 + (y1-y2)**2 ) < (r1+r2)**2 ):
        return False

# 'clickCircle' function for checking what input of player click on circle
def clickCircle(x_circle, y_circle, r_circle, x_mouse, y_mouse):
    if ( ( (x_circle-x_mouse)**2 + (y_circle-y_mouse)**2 ) <= (r_circle)**2 ):
        return True
    elif ( ( (x_circle-x_mouse)**2 + (y_circle-y_mouse)**2 ) <= (r_circle)**2 ):
        return False

# random 10 circles processing
random_circles = []
num_circle = 10
all_radius = []
for i in range(num_circle):
    # set clock that has FPS = 5
    clock.tick(FPS)

    # call 'Circle' class
    circle = Circle()
    random_circles.append(circle)   # pick 'circle' object to 'random_circles list'
    all_radius.append(circle.radius)    # pick 'redius' of each object to 'all_radius list'

    # reach and check overlapped all pairs of circles
    for j in range(len(random_circles)):
        for k in range(len(random_circles)):
            if k != j:
                # using function 'checkOverlap' for all pairs of circles
                overlap = checkOverlap(random_circles[j].x, random_circles[j].y, random_circles[j].radius, 
                            random_circles[k].x, random_circles[k].y, random_circles[k].radius)
                if overlap == False:
                    # if it's overlapped, using 'Circle' class to random new circle and replace the old one
                    new_random_circles = Circle()
                    random_circles[k] = new_random_circles
                    # drawing the newest circle
                    new_random_circles.draw()
                    # if it's non-overlappe, drawing it!
                elif overlap == True:
                    random_circles[j].draw()

        # drawing all circle on screen
        screen.blit(screen, (0,0))
        # update each procressing
        pygame.display.update()

# part of running all of program
running = True
while running:

    for event in pygame.event.get():
        # checking if player close the program
        if event.type == pygame.QUIT:
            running = False

        # checking if player click the largest circle
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for num in random_circles:
                click_on_circle = clickCircle(num.x, num.y, num.radius, mouse_position[0], mouse_position[1])
                if click_on_circle == True:
                    # if player click the largest circle HIDDEN IT!
                    if num.radius == max(all_radius):
                        num.hidden()
                        random_circles.remove(num)
                        all_radius.remove(max(all_radius))
    pygame.display.update()

pygame.quit()

###################################################################################################