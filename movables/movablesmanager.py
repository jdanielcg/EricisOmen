# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from random import randint
from movables.creatures import Creature

class MovablesManager:

    spawnpoints = [(10,10)]
    goalpoint = (5,5)
    
    def __init__(self, game, world):
        self.generate_test_creatures(game,world)

    def generate_test_creatures(self,gamewindow, world):
        for h in range(10,30):
            for w in range(20,40):            
                roll = randint(1, 10)
                if roll == 10 :
                    creature = Creature(gamewindow, (w, h))
                    world.creatures.append(creature)                    
        print("generated " + str(len(world.creatures)) + " creatures ")

    def update(self, world, delta_time):                        
        for creature in world.creatures:
            creature.update(delta_time)