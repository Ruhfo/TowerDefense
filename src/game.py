import pygame
import sys
import os
import random

#defining constants
LOCATION = os.getcwd() #Working directory
MAXFPS = 60 #Guess what
LENGTH = 8 #Temporary way to calculate length

IMG_W = 128 #We need 1/2 of it move tile right
IMG_H = 128 #We need 1/4 of it to move tile down

pygame.init()

def load_images():
    #Function for loading all images into a dictionary
    img_path = os.path.join(LOCATION, "img/PNG/Landscape")
    sprites_landscape = []

    if os.path.exists(img_path):
        for img in range(40):
            sprites_landscape+=[pygame.image.load(os.path.join(img_path,"landscape_"+str(img)+".png"))]
    return sprites_landscape

def generate_map(width, height):
    #Creating 2d array and filling it with items
    # G-grass and R-road S-start F-finish
    game_map = [] 

    game_map.append(["G", "G", "G", "S", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "G", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "G", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "F", "G", "G"])
    
    return game_map

def draw_grid(surf, sprites):
    #Function for drawing the landscape
    startx = (LENGTH/2*IMG_W)-IMG_W/2 
    starty = IMG_H
    for x in range(LENGTH):
        for y in range(LENGTH):
            if (game_map[y][x] == "R" or game_map[y][x] == "S" or game_map[y][x] == "F" ):
                sprite=sprites[17]
            else:
                sprite=sprites[13]
            surf.blit(sprite, ((startx-x*IMG_W/2)+y*IMG_H/2,(starty+x*IMG_W/4)+y*IMG_H/4))

def drawing(screen, sprites_land):
    #Function for drawing litteraly everything
    screen.fill(black)
    draw_grid(screen, sprites_land)
    pygame.display.flip()

#Create window 
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

#Load images -> RAM
sprites_landscape = load_images()

#Define color tuples R, G, B
black = (0,0,0)
#Load preferences or saved game into memory 

#Generate Map 
game_map = generate_map(LENGTH,LENGTH)

#Start counting for waves --> counter on new thread
clock = pygame.time.Clock() #clock for limiting framerate

while True:
    #Game loop
    clock.tick(MAXFPS)
    #Game logic 

    #Drawing
    drawing(screen, sprites_landscape)
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            quit()
quit()
