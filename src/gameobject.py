from pygame import image, sprite 
#This is base gameobject for every active object in game
#Enemies, Towers, missiles, etc ...

class GameObject(sprite.Sprite):
    def __init__(self, images, speed):
        #Initializing base variables
        super(self)
        
        self.imageIndex = 0 # Current image
        self.image = images[self.imageIndex] #image for parent object
        self.imageCount = len(images) #Total number of images
        self.imageSpeed = speed #How fast is the animation ? (not used @ the moment)
        self.images = images #Image list for animations
        
        self.rect = self.image.get_rect() #get rekt (for collision and position)
    def draw(self):
        #draw calls go here (maybe)
        pass
    def update(self):
        #Just like step in game maker
        
        #changing current image
        if self.imageIndex < self.imageCount:
            self.imageIndex++
        else:
            self.imageIndex = 0
        self.image = images[self.imageIndex]

