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
        self.delay = 1    
        self.timer = 0  
        

    def generate(self):
        self.delay = randint(3,4)
        for pos in Settings.enemy_spawns:           
            if len(self.world.creatures) < Settings.max_enemies:
                cell = self.world.cells[pos[1]][pos[0]]
                if cell.vacant:                
                    creature = Creature(self.game, pos)
                    self.world.creatures.append(creature)                    
        

    def update(self, world, delta_time):   
        #gera criaturas continuamente
        self.timer += delta_time
        if self.timer >= self.delay:
            self.generate()                   
            self.timer = 0

        for creature in world.creatures:
            creature.update(delta_time)