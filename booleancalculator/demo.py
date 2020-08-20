############################################################
# Name : Onpinya Phokhahutthakosol
# Student ID : 6201012620261
# File Name : demo.py
############################################################

import splitstring
import pygame

def enter_expression(expression):

    count_open_brac = [] # list for counting open bracket(s)
    
    # access for all elements in expression
    for i in range(len(expression)):
        if expression[i] == '(':
            # if finding '(' (open bracket), loading for checking couple(s) of brackets
            count_open_brac.append(expression[i])

        elif expression[i] == ')':
            # if finding ')' (close bracket), pop() lastest open bracket
            # you'll know which lastest couple of brackets
            if len(count_open_brac) > 1:
                # then this couple of brackets is not lastest couple
                count_open_brac.pop()
            elif len(count_open_brac) == 1 and i == len(expression)-1:
                # then this close bracket is the lastest bracket
                # so open bracket which it is its couple, it is the lastest couple
                return expression[1:-1] # return expression in the lastest couple of bracket
        
        elif expression[0] == '!': # if first element is 'NOT'
            # return original expression
            return expression

    return expression

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

# convert string to list()
test_input = "!(1+0)"
split_str = splitstring.SplitString()
split_list = split_str.split_string(test_input)










running = True
while running:

    for event in pygame.event.get():
        # quit program if user click quit
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()