# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import floor
from random import randint
import pygame
from camera import Camera
from effects.effects import Lifebar, SmokeDamage
from movables.animcontroller import CharAnimationController
from movables.states import IdleState, WalkingState
from settings import Settings

import typing

if typing.TYPE_CHECKING:
    from screens.game import Game    

class Creature:
    def __init__(self, game : "Game", tile_pos = (0.0, 0.0)):
        self.x = 1.0*tile_pos[0]* Settings.tilesize
        self.y = 1.0*tile_pos[1]* Settings.tilesize

        self.path = []
        self.path_color = (randint(0, 255),randint(0, 255),randint(0, 255))

        self.speed = 20.0

        self.anim_controller = CharAnimationController(self)      

        self.damage = 300
        self.lifebar = None


        self.max_integrity = 1000    
        self.integrity = self.max_integrity    

        self.game = game
        self.state = IdleState(self)     
        self.is_dead = False
        print("creature created at {0}, {1} ".format(self.u, self.v))
    
    @property
    def u(self):
        return floor(self.x/Settings.tilesize)

    @property
    def v(self):
        return floor(self.y/Settings.tilesize)

    def take_damage(self, damage):
        self.integrity -= damage
        self.game.effects_manager.effects.append(SmokeDamage(self.x, self.y))
        if self.lifebar != None:
            self.lifebar.renew()
        else:
            self.lifebar = Lifebar(self)
            self.game.effects_manager.effects.append(self.lifebar)
        if self.integrity < 0:
            self.anim_controller.set_dead()
            self.is_dead = True
            self.lifebar = None

    def update(self, delta_time):
        if not self.is_dead : self.state.update(delta_time)
        self.anim_controller.update(delta_time)

        if Settings.show_debug:
            screen = self.game.gameWindow.get_screen()        
            if len(self.path) > 0:
                for step in range(len(self.path) - 1):   
                    start = (self.path[step][0]*32 + 16 - Camera.dx, self.path[step][1]* 32  + 16 - Camera.dy)                 
                    end = (self.path[step +1][0]*32  + 16 - Camera.dx, self.path[step+1][1]*32  + 16 - Camera.dy)                 
                    pygame.draw.line(screen, self.path_color, start, end, 5)

    def get_attackable_target(self):
        #verifica entornos para alvos atacaveis
        if self.game.world.cells[self.v - 1][self.u].building != None:
            return [self.v - 1,self.u]
        elif self.game.world.cells[self.v + 1][self.u].building != None:
            return [self.v + 1, self.u]
        elif self.game.world.cells[self.v][self.u-1].building != None:
            return [self.v, self.u-1]
        elif self.game.world.cells[self.v][self.u+1].building != None:
            return [self.v,self.u+1]
        return None
        




