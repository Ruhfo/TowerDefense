import pygame
import sys
import os
import random

#defining constants
LOCATION = os.getcwd() #Working directory
MAXFPS = 60 #Guess what

pygame.init()

def load_images():
    #Function for loading all images into a dictionary
    img_path = os.path.join(LOCATION, "img/PNG/Landscape")
    sprites_landscape = []

    if os.path.exists(img_path):
        for img in range(40):
            sprites_landscape+=[pygame.image.load(
                                os.path.join(img_path,"landscape_"+str(img)+".png"))
                                .convert()]
    else:
        pass #Something is wrong, but we don't know it yet

    return sprites_landscape

def generate_map(width, height):
    #Generating 2d array and filling it with items
    #G stands for grass and R for road
    r = random.Random()
    game_map = [["G" for i in range(width)] for i in range(height)] 
    
    #Generating points from start to finish 
    points = [(r.randint(0, width-1), 0)] #start

    pointnr = r.randint(3, 5)
    for i in range(pointnr):
        points+=[(r.randint(0, width-1), r.randint(0, height-1))]

    points+=[(r.randint(0, width-1), height-1)]

    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        game_map[x1][y1] = "R"

        if r.randint(0, 1) == 1:
            #go vertical first
            for x in range(x2-x1):
                game_map[x1+x][y1] = "R"
            for y in range(y2-y1):
                game_map[x2][y1+y] = "R"
        else:
            #go horizontal first
            for y in range(y1, y2):
                game_map[x2][y] = "R"
            for x in range(x1, x2):
                game_map[x][y2] = "R"

    #Debug only drawing grid
    #for y in range(height):
    #   for x in range(width):
    #        print(game_map[x][y], end="")
    #    print("")
    #return game_map

#Create window 
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

#Load images -> RAM
sprites_landscape = load_images()

#Define color tuples R, G, B
black = (0,0,0)
#Load game data -> RAM

#Generate Map 
game_map = generate_map(12,12)
game_area = pygame.Rect(width/8, height/8, 2*width/3,2*height/3) #x, y, width, height

#Start counting for waves --> counter on new thread
clock = pygame.time.Clock() #clock for limiting framerate

while True:
    #Game loop
    clock.tick(MAXFPS)
    #Game logic 

    #Drawing
    screen.fill(black)
    for i in range(int(width/128)):
        screen.blit(sprites_landscape[0], (i*128, 0))
    pygame.display.flip()
    #Get userinput
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

quit()
