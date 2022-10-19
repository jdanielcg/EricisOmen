
from effects.effects import SmokeDamage
from settings import Settings


class EffectsManager:
    def __init__(self):

        self.effects = [SmokeDamage(100, 100)]

        
    def update(self, delta_time):
        for effect in self.effects:
            effect.update(delta_time)
            if effect.timer >= effect.duration:
                self.effects.remove(effect)

    def add_smoke(self, u, v):
        smoke = SmokeDamage(u*Settings.tilesize, v*Settings.tilesize)
        self.effects.append(smoke)