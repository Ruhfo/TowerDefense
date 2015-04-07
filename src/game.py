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
            sprites_landscape+=[pygame.image.load(
                                os.path.join(img_path,"landscape_"+str(img)+".png"))
    else:
        pass #Something is wrong, but we don't know it yet

    return sprites_landscape

def generate_map(width, height):
    #Creating 2d array and filling it with items
    #G stands for grass and R for road
    game_map = [] 
    game_map.append(["G", "G", "G", "R", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "G", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "G", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    
    return game_map

def draw_grid(surf, sprites):
    #Function for drawing the landscape
    startx = (LENGTH/2*IMG_W)-IMG_W/2 
    starty = IMG_H
    for x in range(LENGTH):
        for y in range(LENGTH):
            if game_map[y][x] == "R":
                sprite=sprites[17]
            else:
                sprite=sprites[13]
            surf.blit(sprite, ((startx-x*64)+y*64,(starty+x*32)+y*32))

#Create window 
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

#Load images -> RAM
sprites_landscape = load_images()

#Define color tuples R, G, B
black = (0,0,0)
#Load game data -> RAM

#Generate Map 
game_map = generate_map(LENGTH,LENGTH)

#Start counting for waves --> counter on new thread
clock = pygame.time.Clock() #clock for limiting framerate

while True:
    #Game loop
    clock.tick(MAXFPS)
    #Game logic 

    #Drawing
    screen.fill(black)
    draw_grid(screen, sprites_landscape)
    pygame.display.flip()
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
quit()
