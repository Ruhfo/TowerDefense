import gameobject
from pygame import sprite, image
#added enemy template here

class Projectile(gameobject.GameObject):
    def __init__(self, direction):
        #Initializing base variables
        super() #We probably should initialize parrent object
        self.movex, self.movey = direction
    def update(self):
        #Overwrite parrent step
        x+=self.movex
        y+=self.movey
    def draw(self):
        pass 
