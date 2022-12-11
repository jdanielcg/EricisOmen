# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint

from numpy import roll
from movables.creatures import Creature
from settings import Settings
from match import Match

class MovablesManager:
    
    def __init__(self, game, world):
        self.game = game
        self.world = world
        self.delay = 1    
        self.timer = 0  
        

    def generate(self):
        self.delay = randint(3,4)
        if len(self.world.creatures) < Settings.max_creatures:
            for pos in Settings.enemy_spawns:           
                if len(Match.enemies) < Settings.max_enemies_wave:
                    cell = self.world.cells[pos[1]][pos[0]]
                    if cell.vacant:                
                        creature = Creature(self.game, pos, True, "human")
                        Match.enemies.append(creature)
                        self.world.creatures.append(creature)   
            self.world.domain_cells.reverse()
            for cell in self.world.domain_cells:
                if cell.vacant and len(Match.allies) < Match.max_population:
                    creature = Creature(self.game, cell.location, False, "kobold")
                    Match.allies.append(creature)
                    self.world.creatures.append(creature)   
                    return 
        

    def update(self, world, delta_time):   
        #gera criaturas continuamente
        self.timer += delta_time
        if self.timer >= self.delay:
            self.generate()                   
            self.timer = 0

        for creature in world.creatures:
            creature.update(delta_time)