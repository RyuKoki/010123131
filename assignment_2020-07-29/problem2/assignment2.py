###################################################################################################
# Student Name : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# Subject ID : 010123131 Software Development Practice I
# File Name : asg2_demo1.py
# Model File Name : pygame_camera_demo-1.py
# Model Author Name : RSP
###################################################################################################
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

image = pygame.image.load("C:/Users/RyuKoki/Desktop/image_dragDrop.jpg")

image_rect = image.get_rect()

image_width, image_height = image_rect.w, image_rect.h

scr_w, scr_h = image_width, image_height

screen = pygame.display.set_mode((scr_w, scr_h))

pygame.display.set_caption('Asg2 : Drag and Drop')

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )


all_rect = []
M, N = 5, 5
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        rect = pygame.rect.Rect( i*rw, j*rh, rw, rh )
        all_rect.append(rect)
        pygame.draw.rect( image, RED, rect, 1 )
        surface.blit( image, rect, rect )

dragging = False
dropping = True
running = True
while running:

    for event in pygame.event.get():

        # check when user use QUIT to close program
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for a_rect in all_rect:
                    click_down = event.pos
                    if a_rect.collidepoint(click_down):
                        dragging = True
                        original_rect = a_rect
                        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click_up = event.pos
                for a_rect in all_rect:
                    if dropping:
                        a_rect, original_rect = original_rect, a_rect
                        dropping = False              

    screen.blit( image, (0, 0) )
    pygame.display.update()
pygame.quit()
###################################################################################################
