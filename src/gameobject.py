from pygame import image, sprite 
#This is base gameobject for every active object in game
#Enemies, Towers, missiles, etc ...


class GameObject(sprite.Sprite):
    def __init__(self, images):
        #Initializing base variables
        super(self)
        
        self.image = images[0] #image for parent object
        self.images = images #Image list for animations
        
        self.rect = self.image.get_rect() #get rekt
        pass
    def draw(self):
        #draw calls go here
        pass
    def step(self):
        #Just like step in game maker
        pass
