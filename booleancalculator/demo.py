############################################################
# Name : Onpinya Phokhahutthakosol
# Student ID : 6201012620261
# File Name : demo.py
############################################################
import pygame
from splitstring import SplitString
from booleantree import BooleanTree
import sys

# initialize pygame
pygame.init()

# set width and height
WIDTH, HEIGHT = 650, 650

# set screen of program
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Boolean Expression Tree')

# set color 'RGB'
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class DrawTree:

    def __init__(self, x, y, radius, text):

        self.x = x
        self.y = y
        self.radius = radius
        self.GREEN = (0, 255, 0) # Green color
        self.BLACK = (0, 0, 0) # Black color
        self.text = text

    def draw_node(self):
        pygame.draw.circle( screen, self.GREEN, (self.x, self.y), self.radius )
        font = pygame.font.SysFont('Consolas.ttf', self.radius*2)
        text_render = font.render(self.text, True, self.BLACK)
        text_rect = text_render.get_rect()
        text_rect.center = (self.x, self.y)
        pygame.display.update()

class DrawLine:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw_line(self):
        pygame.draw.line(screen, GREEN, (self.x1, self.y1), (self.x2, self.y2), 10)
        pygame.display.update()

split_str = SplitString()
boolean_t = BooleanTree()
# exp_input = "!(1+0)"
# exp_input = "!(!(0+I0&1))"
# exp_input = "(I0+!I1+!(I2))&(!I0+I1+I2)"
# exp_input = "!(I0&I1)+!(I1+I2)"
# exp_input = "(((I0&I1&!I2)+!I1)+I3)"
exp_input = "(I1+I0)"
split_exp = split_str.split_string(exp_input)
create_tree = boolean_t.create_tree(split_exp, 0)


running = True
while running:

    for event in pygame.event.get():
        # quit program if user click quit
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()
