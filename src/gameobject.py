from pygame import image, sprite 
#This is base gameobject for every active object in game
#Enemies, Towers, missiles, etc ...


class GameObject(sprite.Sprite):
    def __init__(self, images):
        #Initializing base variables
        super(self)
        

        self.imageIndex = 0 # Current image
        self.image = images[self.imageIndex] #image for parent object
        self.imageCount = len(images) #Total number of images
        self.images = images #Image list for animations
        
        self.rect = self.image.get_rect() #get rekt (for collision)
        pass
    def draw(self):
        #draw calls go here

        pass
    def update(self):
        #Just like step in game maker
        pass
