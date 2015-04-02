import pygame
import sys
import os
import random

#defining constants
LOCATION = os.getcwd() #Working directory
MAXFPS = 60 #Guess what
MAXPOINTS = 5
MINPOINTS = 3

pygame.init()

def load_images():
    #Function for loading all images into a dictionary
    img_path = os.path.join(LOCATION, "img/PNG/Landscape")
    sprites_landscape = []

    if os.path.exists(img_path):
        for img in range(40):
            pygame.image(img_path, "Landscape_"+str(img)+".png")
    else:
        pass #Something is wrong, but we don't know it yet

    return sprites

def generate_map(width, height):
    #Generating 2d array and filling it with items
    r = random.Random()
    game_map = [["G" for i in range(width)] for i in range(height)] 
    
    #Generating points from start to finish 
    points = [(r.randint(1, width), 1)] #start
    points+=[(r.randint(1, width),height)] #finish

    #Debug only drawing grid
    for y in range(height):
        for x in range(width):
            print(game_map[x][y], end="")
        print("")
    return game_map

#Create window 
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#Load images -> RAM
sprites = load_images

#Define color tuples R, G, B
black = (0,0,0)
#Load game data -> RAM

#Generate Map 
generate_map(12,12)

#Start counting for waves --> counter on new thread
clock = pygame.time.Clock() #clock for limiting framerate

while True:
    #Game loop
    clock.tick(MAXFPS)
    #Game logic 

    #Drawing
    screen.fill(black)

    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

quit()
