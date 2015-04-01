import pygame
import sys
import os

#defining constants
LOCATION = os.getcwd()

pygame.init()

def load_images():
    #Function for loading all images into a dictionary
    img_path = os.path.join(LOCATION, "img/PNG")
    sprites = {}
    if os.path.exists(img_path):
        sprites += dict("tileGrass", pygame.image.load(os.path.join( os.path.normalise(img_path), "landscape_13.png")))
    else:
        pass
    return sprites

#Create window 
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#Load images -> RAM
sprites = load_images


#Define color tuples
black = (0,0,0)

#Load game data -> RAM

#Generate Map 

#Start counting for waves --> counter on new thread
while True:
    #Game loop

    #Game logic 

    #Drawing
    screen.fill(black)
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

quit()
