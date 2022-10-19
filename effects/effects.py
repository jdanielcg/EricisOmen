from math import sqrt
from PPlay.sprite import Sprite


class SmokeDamage:
    def __init__(self, x, y):
        self.duration = 1000
        self.animation = Sprite("assets\smoke.png", 5)        
        self.animation.set_total_duration(self.duration)
        self.animation.set_position(x, y) 
        self.timer = 0
        
        
    def update(self, delta_time):
        self.animation.update()
        self.animation.draw()
        self.timer += delta_time*1000    


class Fireball:
    def __init__(self, x, y, target_creature):
        self.duration = 10000
        self.timer = 0
        self.animation = Sprite("assets\fireball.png", 2)        
        self.animation.set_total_duration(200)
        self.animation.set_position(x, y) 
        self.x = x
        self.y = y
        self.speed = 50
        self.target_creature = target_creature
        self.damage = 400
        
        
    def update(self, delta_time):
        tarX = self.target_creature.x
        tarY = self.target_creature.y

        #para que seja destruida
        if abs(tarX - self.x) <= 0.9:
            if abs(tarY - self.y) <= 0.9:
                self.timer = self.duration = 10000
                self.target_creature.take_damage(self.damage)
                return

        #move a bola de fogo
        dirX = tarX - self.x; 
        dirY = tarY - self.y; 
        dirT = sqrt(dirX*dirX + dirY*dirY)

        if dirT != 0: 
            dirX = dirX/dirT
            dirY = dirY/dirT
            self.x += dirX*delta_time*self.speed                   
            self.y += dirY*delta_time*self.speed

        self.animation.set_position(self.x, self.y) 
        self.animation.update()
        self.animation.draw()

        

