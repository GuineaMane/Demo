"""
This program just has a ball that moves/bounces around screen based on speed modifiers (dx,dy)
Was just a test to get to know how pygame works
"""

import pygame
from pygame.locals import *
import sys
import time

pygame.init()
# Upper right (640,0)
# Lower left (0,480)
# Lower Right (640, 480)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#colorname = (r,g,b)
blue = (0,0,255)
white = (255,255,255)

#speed and xy
x = y = 0
dx = 5
dy = 2

#Main Game loop
while True:
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit(); sys.exit();
    screen.fill(white)

    pygame.draw.circle(screen, blue, (50+x,50+y),50, 5)

    #move xy by speed
    x += dx
    y += dy

    #try to create borders so object does not go outside of window
    if x < 0 or x > width-50:
        dx = -dx
        x += dx
    if y < -50 or y > height-50:
        dy = -dy
        y += dy

    time.sleep(0.01)
    pygame.display.update()
