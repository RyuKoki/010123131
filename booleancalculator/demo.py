############################################################
# Name : Onpinya Phokhahutthakosol
# Student ID : 6201012620261
# File Name : demo.py
############################################################

import pygame

class DrawNode:

    def __init__(self, x, y, radius, text):

        self.x = x
        self.y = y
        self.radius = radius
        self.GREEN = (0, 255, 0) # Green color
        self.BLACK = (0, 0, 0) # Black color
        self.text = text

    def draw_node(self):
        pygame.draw.circle( screen, self.GREEN, (self.x, self.y), self.radius )
        font = pygame.font.SysFont('Consola.ttf', self.radius*2)
        text_render = font.render(self.text, True, self.BLACK)
        text_rect = text_render.get_rect()
        text_rect.center = (self.x, self.y)

# initialize pygame
pygame.init()

# set width and height
WIDTH, HEIGHT = 650, 650

# set screen of program
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Boolean Expression Tree')

# set color 'RGB'
WHITE = (255, 255, 255)



running = True
while running:

    for event in pygame.event.get():
        # quit program if user click quit
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()
