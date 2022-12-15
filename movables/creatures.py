# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import floor
from random import randint
import pygame
from audio.spacialsfx import SpacialSFX
from camera import Camera
from effects.effects import FloatingIconText, Lifebar, SmokeDamage
from effects.effectsmanager import EffectsManager
from match import Match
from movables.animcontroller import CharAnimationController
from movables.states import IdleState, WalkingState
from settings import Settings

import typing

if typing.TYPE_CHECKING:
    from screens.game import Game    

class Creature:
    def __init__(self, game : "Game", tile_pos = (0.0, 0.0), is_enemy = True, folder = "kobold", aether = 0, damage = 300,
                speed = 20.0, max_integrity = 1000):

        self.game = game
        self.code = str(randint(10000, 99999)) + str(is_enemy)
        self.is_enemy = is_enemy

        self.x = 1.0*tile_pos[0]* Settings.tilesize
        self.y = 1.0*tile_pos[1]* Settings.tilesize

        self.path = []
        self.path_color = (randint(0, 255),randint(0, 255),randint(0, 255))

        self.speed = speed

        self.anim_controller = CharAnimationController(self, folder)      

        self.damage = damage
        self.lifebar = None

        self.max_integrity = max_integrity    
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

        #registra se a criatura esta em uma armadilha
        self.current_trap = None

        #registra se a criatura está envenenada
        self.is_poisoned_level = 0
        self.poison_timer = 0.0 #segundos

        #valor ganho ao derrotar
        self.aether = aether


        #print("creature created at {0}, {1} ".format(self.u, self.v))
    
    @property
    def u(self):
        return floor(self.x/Settings.tilesize)

    @property
    def v(self):
        return floor(self.y/Settings.tilesize)

    def check_trap(self):
        if not self.is_enemy:
            return False
        if self.current_cell.building != None:
            if self.current_trap != self.current_cell.building:
                self.current_trap = self.current_cell.building
                if self.current_cell.building.info.name == "firetrap":
                    self.take_damage(500, "fire")
                    SpacialSFX("firehit",self.x, self.y) 
                elif self.current_cell.building.info.name == "poisontrap":
                    self.is_poisoned_level += 1


    def take_damage(self, damage, damage_type = None):
        if self.is_dead:
            return

        if self.is_enemy and not Match.researched_war:
            damage = damage
        elif self.is_enemy and Match.researched_war:
            damage = 2.0*damage
        elif not self.is_enemy and not Match.researched_war:
            damage = damage
        elif not self.is_enemy and Match.researched_war:
            damage = damage/2.0

        self.integrity -= damage
        self.game.effects_manager.effects.append(SmokeDamage(self.x, self.y, damage_type))
        if self.lifebar != None:
            self.lifebar.renew()
        else:
            self.lifebar = Lifebar(self)
            self.game.effects_manager.effects.append(self.lifebar)
        if self.integrity < 0:
            self.anim_controller.set_dead()
            self.is_dead = True
            self.lifebar = None

            SpacialSFX("dead",self.x, self.y)
            if self.is_enemy:
                Match.aether += round(self.aether)
                EffectsManager.effects.append(FloatingIconText(self.x, self.y,"aether","+" + str(round(self.aether))))

    def slow_down(self):
        self.speed /= 2.0

    def update(self, delta_time):
        if not self.is_dead : self.state.update(delta_time)
        self.anim_controller.update(delta_time)

        #verifica se pisou em armadilha
        self.check_trap()

        #verifica se esta envenenado e aplica dano
        if self.is_poisoned_level > 0:
            self.poison_timer += delta_time
            if self.poison_timer >= 1.5:
                self.poison_timer = 0.0
                SpacialSFX("poisontrap",self.x, self.y) 
                self.take_damage(100 * self.is_poisoned_level, "poison")


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
        




