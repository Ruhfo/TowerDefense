from gameobject import GameObject

class BaseTower(GameObject):
    def __init__(self, images, speed, pos):
        super().__init__(images, speed, pos)
        
    def update(self):
        pass
    def draw(self, surf):
        for i in range(len(self.images)):
            img = self.images[i]
            surf.blit(img, self.rect)

class CannonTower(BaseTower):
    def __init__(self):
        pass
class MudTower(BaseTower):
    def __init__(self):
        pass
