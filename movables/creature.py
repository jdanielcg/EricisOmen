import math
from random import randint
from pygame import Vector2
from movables.animcontroller import CharAnimationController
from movables.manualmovcontroller import ManualMovController

class Creature:
    def __init__(self, gamewindow,tile_pos = (0, 0)):
        self.u = tile_pos[0]
        self.v = tile_pos[1]
        self.x = tile_pos[0]*32
        self.y = tile_pos[1]*32

        self.anim_controller = CharAnimationController(Vector2(self.x, self.y))
        self.mov_controller = ManualMovController(gamewindow, self.anim_controller)        
        print("creature created at {0}, {1} ".format(self.u, self.v))


    def update(self, delta_time):
        self.mov_controller.update(delta_time)




