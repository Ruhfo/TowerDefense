import pygame
import sys
pygame.init()

#Create window 
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#Load images -> RAM
black = (0,0,0)
#Load game data -> RAM

#Generate Map 

#Start counting for waves
while True:

    #Game logic 

    #Drawing
    screen.fill(black)
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

quit()
