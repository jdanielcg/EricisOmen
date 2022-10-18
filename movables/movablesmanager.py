from random import randint
from movables.creatures import Creature


    



class MovablesManager:

    spawnpoints = [(10,10)]
    goalpoint = (5,5)
    
    def __init__(self, game, world):
        self.generate_test_creatures(game,world)

    def generate_test_creatures(self,gamewindow, world):
        for h in world.cells:
            for w in h:            
                roll = randint(1, 80)
                if roll == 80 :
                    creature = Creature(gamewindow ,w.location)
                    world.creatures.append(creature)                    
        print("generated " + str(len(world.creatures)) + " creatures ")

    def update(self, world, delta_time):                
        for creat in world.creatures:
            creat.update(delta_time)