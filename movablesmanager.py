from random import randint
import pygame

from movables.creature import Creature



class MovablesManager:
    def __init__(self, gamewindow, world):
        self.generate_test_creatures(gamewindow,world)

    def generate_test_creatures(self,gamewindow, world):
        for h in world.cells:
            for w in h:            
                roll = randint(1, 20)
                if roll == 20 :
                    creature = Creature(gamewindow ,w.location)
                    world.creatures.append(creature)
        print("generated " + str(len(world.creatures)) + " creatures ")

    def update(self, world, delta_time):                
        for creat in world.creatures:
            creat.update(delta_time)