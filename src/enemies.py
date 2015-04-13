import gameobject
from pygame import sprite, image
#added enemy template here

class Enemy(gameobject.GameObject):
    def __init__(self):
        #Initializing base variables
        super() #We probably should initialize parrent object
        pass
    def update(self):
        #Overwrite parrent step
        pass
    def draw(self):
        #Overwrite parrent draw
        pass
