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

def generate_map(width, height, sprites):
    #Creating 2d array and filling it with items
    # G-grass and R-road S-start F-finish
    game_map = [] #Simple human readable array with necessary contents
    grid = [[0 for i in range(LENGTH)] for i in range(LENGTH)] #More complex array
    
    #initialize grid

    game_map.append(["G", "G", "G", "S", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "G", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "G", "G", "G", "G"])
    game_map.append(["G", "G", "G", "R", "R", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "R", "G", "G"])
    game_map.append(["G", "G", "G", "G", "G", "F", "G", "G"])
    
    #Defining map drawing starting positions
    startx = (0.5*LENGTH*IMG_W)-IMG_W*0.5
    starty = IMG_H

    for x in range(LENGTH):
        for y in range(LENGTH):
            unit = []

            posx = (startx-x*IMG_W*0.5)+y*IMG_H*0.5
            posy = (starty+x*IMG_W/4)+y*IMG_H/4
            rect = pygame.Rect(posx, posy, IMG_W, IMG_H )
            unit.append(rect) #Cordinate area rect

            if (game_map[x][y] == "R" or game_map[x][y] == "S" or game_map[x][y] == "F" ):
                unit.append(sprites[17])
            else:
                unit.append(sprites[13])
            grid[x][y] = unit

    return grid 

def draw_grid(screen, grid):
    #Function for drawing the landscape
    surf = screen
    for x in range(LENGTH):
        for y in range(LENGTH):
            unit = grid[x][y]
            pos = unit[0]
            surf.blit(unit[1], pos)

def drawing(screen, grid):
    #Function for drawing litteraly everything
    screen.fill(black)
    draw_grid(screen, grid)
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
game_map = generate_map(LENGTH,LENGTH, sprites_landscape)

#Start counting for waves --> counter on new thread

clock = pygame.time.Clock() #clock for limiting framerate

while True:
    #Game loop
    clock.tick(MAXFPS)
    #Game logic 

    #Drawing
    drawing(screen, game_map)
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

quit()
