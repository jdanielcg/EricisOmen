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