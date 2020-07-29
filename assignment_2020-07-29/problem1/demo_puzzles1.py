###################################################################################################
# Student Name : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# Subject ID : 010123131 Software Development Practice I
# File Name : demo_puzzles1.py
# Model File Name : pygame_camera_demo-1.py
# Model Author Name : RSP
###################################################################################################
# import all of libraries for using in this program
import pygame

# initialize pygame
pygame.init()

# setting width, height
WIDTH, HEIGHT = 640, 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# setting width x height of screen
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

# create surface transparent for all objects to draw on
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# create list for keep the rect objects
divide_width, divide_height = 10, 8
# set the width x height of square tiles
rw, rh = WIDTH//divide_width, HEIGHT//divide_height
for i in range(divide_width):
    for j in range(divide_height):
        # specify the location of rect
        rect = (i*rw, j*rh, rw, rh) # pygame.Rect(left, top, width, height)
        # draw the green of around rects border 1 pixels
        pygame.draw.rect( screen, GREEN, rect, 1 )
        # draw all on surface
        surface.blit( screen, rect, rect )

# import image
img = pygame.image.load("C:/Users/RyuKoki/Desktop/sea_pic.jpg")
# give the properties of image
img_rect = img.get_rect()
# get properties width and height of image
img_width, img_height = img_rect.w, img_rect.h

running = True
while running:

    for event in pygame.event.get():

        # check when user use QUIT to close program
        if event.type == pygame.QUIT:
            running = False
        
        # check when user click on screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for i in range(divide_width):
                for j in range(divide_width):
                    # check for delete square tiles
                    if mouse_position[0]>=i*rw and mouse_position[0]<(i+1)*rw:
                        if mouse_position[1]>=j*rh and mouse_position[1]<(j+1)*rh:
                            surface.blit(img, (i*rw,j*rh), (i*rw,j*rh,rw,rh))

    screen.fill(BLACK)
    screen.blit( surface, (0, 0) )
    pygame.display.flip()
pygame.quit()
