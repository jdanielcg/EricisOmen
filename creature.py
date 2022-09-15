
import math
from random import randint
import re

class Creature:
    def __init__(self, position = (0, 0)):
        self.x = position[0]*32
        self.y = position[1]*32
        self.creature_code = 31
        print("creature created at {0}, {1} ".format(self.x, self.y))

        self.target_position = (self.x, self.y)
        self.speed = 0.0001

        

    
    def generate_random_creature_movs(self):
        pass

    def update(self, delta_time):
        roll = randint(1, 20)
        if roll == 20 :
            self.target_position = (self.x + 100, self.y + 100)

        if not self.check_distance_target():
            self.x = self.x + (self.target_position[0] - self.x) * self.speed 
            self.y = self.y + (self.target_position[1] - self.y) * self.speed 


    def check_distance_target(self):
        if math.dist((self.x, self.y), self.target_position) <= 3:
            return True
        return False


