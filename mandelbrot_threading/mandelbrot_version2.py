###################################################################
# Author : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# Subject Name : 010123131 Software Development Practice I
# Date : 24 July 2020
# File name : mandelbrot_version2.py
###################################################################

# import all of libraries for using in this program
import threading
import time
import pygame

print( 'File : ', __file__)

# initialize pygame
pygame.init()

# set HEIGHT x WIDTH of screen
WIDTH, HEIGHT = 500, 500
HALF_WIDTH, HALF_HEIGHT = WIDTH/2, HEIGHT/2
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# set program name
pygame.display.set_caption('Fractal Image : MANDELBROT (version2.0 LATEST)')

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

# define 'plotMandelbrot' function
def plotMandelbrot(surface, id, lock, sem):
    scale = 0.006 # this is zoom like lens in microscope
    offset = complex(-0.6, 0.0) # 'offset' for moveing the picture mandelbrot which is ploted on center of screen
    if sem.acquire(timeout=0.1): # aquire lock
        for x in range(id*Screen_N, (id+1)*Screen_N):
            for y in range(HEIGHT):
                with lock:
                    real_part = scale*(x-HALF_WIDTH) + offset.real
                    imag_part = scale*(y-HALF_HEIGHT) + offset.imag
                    complex_num = complex( real_part, imag_part )
                    color = mandelbrot(complex_num, 63)
                    r = (color << 6) & 0xc0 # shifting binary to choose color in hexadecimal to RGB
                    g = (color << 4) & 0xc0
                    b = (color << 2) & 0xc0
                    surface.set_at( (x, y), (255-r,255-g,255-b) )
            # release the lock
#----------------------------------------------------------------

# the number of threads
N = 50

# create lock thread
lock = threading.Lock()

# separate width for giving thread know scope max and min
Screen_N = int(WIDTH/N)

# create list for giving all of threads
thread_obj = []

# create semaphored list
list_sem = [ threading.Semaphore(0) for i in range(N) ]

# create each thread by num_threads
for j in range(N):
    sem = list_sem[j]
    a_thread = threading.Thread( target=plotMandelbrot, args=(surface, j, lock, sem) )
    thread_obj.append( a_thread )

#----------------------------------------------------------------

# start each of theads in 'thread_obj' list
for a_thread in thread_obj:
    a_thread.start()

#----------------------------------------------------------------


#----------------------------------------------------------------
running = True
while running:
    
    clock.tick( 100 )

    for sem in list_sem:
        sem.release()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit( surface, (0,0) )
    pygame.display.update()
pygame.quit()
#----------------------------------------------------------------
###################################################################
# Reference's PART
# Model code : Dr.Rawat Siripokarpirom (RSP : Author)
# File model name : python_threading_demo-8.py
# File adapte name(s) : python_threading_demo-7.py
# This is the second version. And I give it 'the LATEST VERSION'.
# Link video for output >> https://youtu.be/60cvfhG2gHA
###################################################################