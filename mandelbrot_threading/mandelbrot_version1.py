###################################################################
# Author : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# Subject Name : 010123131 Software Development Practice I
# Date : 24 July 2020
# File name : mandelbrot_version1.py
###################################################################

# import all of libraries for using in this program
import threading
import time
import cmath
import pygame

print( 'File : ', __file__)

# initialize pygame
pygame.init()

# set HEIGHT x WIDTH of screen
width, height = 500, 500
screen = pygame.display.set_mode( (width, height) )

# set program name
pygame.display.set_caption('Fractal Image : MANDELBROT')

# set clock for pygame
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#----------------------------------------------------------------
def mandelbrot(c, max_iters=100):
    i = 0
    z = complex(0, 0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c # mandelbrot fractal equation : f(z) = (z**2) + c
        i += 1 # c is complex number and z is 0 to infinity
    return i

drawing = True
def plotFractal(id, lock, sem):
    global drawing

    width2, height2 = width/2, height/2 # half width and height of screen
    while drawing:
        try:
            barrier.wait() # wait for all thread to work at the screen
        except threading.BrokenBarrierError:
            continue
        with lock:
            scale = 0.006
            offset = complex(-0.6,0.0)
            for x in range(width):
                for y in range(height):
                    re = scale*(x-width2) + offset.real
                    im = scale*(y-height2) + offset.imag
                    c = complex( re, im )
                    color = mandelbrot(c, 63)
                    r = (color << 6) & 0xc0
                    g = (color << 4) & 0xc0
                    b = (color << 2) & 0xc0
                    surface.set_at( (x, y), (255-r,255-g,255-b) )
                    # draw the surface on the screen
                    screen.blit( surface, (0,0) )
                    # update the display
                    pygame.display.update()
    time.sleep(0.01)
#----------------------------------------------------------------

# set the number of thread to be created
N = 50

# create a thread lock
lock = threading.Lock()

# create a barrier with capacity N
barrier = threading.Barrier(N)

# create a list to give all of threads
list_threads = []

# create threads
for i in range(N):
    id = (i+1)
    a_thread = threading.Thread(target=plotFractal, args=(id, lock, barrier))
    list_threads.append(a_thread)

# start all of threads in 'list_threads'
for a_thread in list_threads:
    a_thread.start()

drawing = False
barrier.reset()

running = True
while running:

    clock.tick(0.1) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
###################################################################
# Reference's PART
# Model code : Dr.Rawat Siripokarpirom (RSP : Author)
# File model name : python_threading_demo-8.py
# File adapte name(s) : python_threading_demo-2.py to python_threading_demo-5.py
# This is the first version. I'll make another version and upload in this github.
###################################################################
