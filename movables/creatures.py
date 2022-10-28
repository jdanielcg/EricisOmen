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
    def __init__(self, game : "Game", tile_pos = (0.0, 0.0), is_enemy = True, folder = "kobold"):
        self.game = game
        self.code = str(randint(10000, 99999)) + str(is_enemy)
        self.is_enemy = is_enemy

        self.x = 1.0*tile_pos[0]* Settings.tilesize
        self.y = 1.0*tile_pos[1]* Settings.tilesize

        self.path = []
        self.path_color = (randint(0, 255),randint(0, 255),randint(0, 255))

        self.speed = 20.0

        self.anim_controller = CharAnimationController(self, folder)      

        self.damage = 300
        self.lifebar = None

        self.max_integrity = 1000    
        self.integrity = self.max_integrity    

        #registra o alvo do movimento
        self.target_uv = None

        #usados para acompanhar as células ocupadas durante os movimentos
        self.current_cell = None
        self.future_cell = None
        self.current_cell = self.game.world.cells[self.v][self.u]
        self.current_cell.creature = self

        #seleciona o estado inicial da criatura
        self.state = IdleState(self)     
        self.is_dead = False


        #print("creature created at {0}, {1} ".format(self.u, self.v))
    
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

        #controla a ocupação das celulas
        self.current_cell = self.game.world.cells[round(self.y/Settings.tilesize)][round(self.x/Settings.tilesize)]
        if self.current_cell != None:
            self.current_cell.creature = self
        if self.target_uv != None:
            self.future_cell = self.game.world.cells[self.target_uv[1]][self.target_uv[0]]
            if self.future_cell != None:
                self.future_cell.future_creature = self
        else:
            self.future_cell = None

        #[debug] exibe o caminho gerado
        if Settings.show_debug:
            screen = self.game.gameWindow.get_screen() 
            start, end = (0,0)       
            if len(self.path) > 0:
                for step in range(len(self.path) -1 ):   
                    start = (self.path[step][0]*32 + 16 - Camera.dx, self.path[step][1]* 32  + 16 - Camera.dy)                     
                    end = (self.path[step +1][0]*32  + 16 - Camera.dx, self.path[step+1][1]*32  + 16 - Camera.dy)                 
                    pygame.draw.line(screen, self.path_color, start, end, 5)

    def get_attackable_target(self):
        #verifica entornos para alvos atacaveis
        if self.current_cell == None:
            return None
        for cell in self.current_cell.close_neighbors:
            if self.is_enemy:
                if cell.building != None:
                    return cell
            else:
                if cell.creature != None:
                    if cell.creature.is_enemy:
                        return cell
 
        return None
        




