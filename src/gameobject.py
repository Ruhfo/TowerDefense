from pygame import image, sprite 
#This is base gameobject for every active object in game
#Enemies, Towers, missiles, etc ...

class GameObject(sprite.Sprite):
    def __init__(self, images, speed, pos):
        #Initializing base variables
        super()
        
        self.imageIndex = 0 # Current image
        self.image = images[self.imageIndex] #image for parent object
        self.imageCount = len(images) #Total number of images
        self.imageSpeed = speed #How fast is the animation ? (not used @ the moment)
        self.images = images #Image list for animations

        self.rect = self.image.get_rect() #get rekt (for collision and position)
        self.rect = self.rect.move(pos.x, pos.y)

    def draw(self, surf):
        #draw calls go here (maybe)
        surf.blit(self.image, self.rect)
    def update(self):
        #Just like step in game maker
        
        #changing current image not bound to speed yet
        if self.imageIndex < self.imageCount:
            self.imageIndex+=1
        else:
            self.imageIndex = 0
        self.image = images[self.imageIndex]

