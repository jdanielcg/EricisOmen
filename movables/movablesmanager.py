# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint

from numpy import roll
from movables.creatures import Creature
from settings import Settings

class MovablesManager:
    
    def __init__(self, game, world):
        self.game = game
        self.world = world
        self.roll = 10      
        

    def generate(self):
        for pos in Settings.enemy_spawns:           
            if len(self.world.creatures) < Settings.max_enemies - 10:
                roll = randint(0,100)
                if roll == 100:
                    creature = Creature(self.game, pos)
                    self.world.creatures.append(creature)                    
        

    def update(self, world, delta_time):   
        self.generate()                   
        for creature in world.creatures:
            creature.update(delta_time)