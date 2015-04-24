from gameobject import GameObject

class BaseTower(GameObject):
    def __init__(self, images, speed, pos):
        super().__init__(images, speed, pos)
    def update(self):
        pass
    def shoot(self, xx, yy):
        #Function for calculating trajector of projectile 
        #and launching said projectile
        pass 
class CannonTower(BaseTower):
    def __init__(self):
        pass
class MudTower(BaseTower):
    def __init__(self):
        pass
