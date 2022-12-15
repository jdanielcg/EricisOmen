import math
import random

from pygame import Surface
import pygame
from audio.audiomanager import AudioManager
from audio.spacialsfx import SpacialSFX
from camera import Camera
from effects.effectsmanager import EffectsManager
from match import Match
from settings import Settings
from effects.effects import EricisBirth, Ericis, EricisFire

class Ending():
    def __init__(self, game):
        self.game = game
        self.tile_list = []

        self.start = False
        self.timer = 0.0


        self.firestarted = False
        self.boom_timer = 0.0

        self.courtain = Surface((game.screen.get_width(), game.screen.get_height()), pygame.SRCALPHA)
        self.courtainB = Surface((game.screen.get_width(), game.screen.get_height()), pygame.SRCALPHA)

        font = pygame.font.SysFont("bahnschrift semibold", 40, False, False)

        #cria a surface com o texto escrito
        credits = [
                    font.render("OBRIGADO POR JOGAR ERICIS OMEN", True, (255,255,255)),
                    font.render("DESENVOLVIDO POR", True, (255,255,255)),
                    font.render("RAMON SANTOS", True, (255,255,255)),
                    font.render("JOSE DANIEL C GOMES", True, (255,255,255)),
                    ]
        ty = 75
        for credit in credits:
            tx =  game.screen.get_width()/2.0 - credit.get_width()/2.0 
            self.courtainB.blit(credit, (tx, ty))
            ty += 50

    def start_end(self):
        #centraliza a camera na fenda
        Camera.set_view_from_center(Settings.breach_center[0], Settings.breach_center[1])

        ou = Settings.breach_center[0]
        ov = Settings.breach_center[1]


        #cria lista de tiles
        for cell_line in self.game.world.cells:
            for cell in cell_line: 
                if (abs(cell.u - ou) + abs(cell.v - ov)) < 35:
                    self.tile_list.append(cell)

        ox = (Settings.breach_center[0]-1.5) * Settings.tilesize
        oy = (Settings.breach_center[1]-2) * Settings.tilesize

        EffectsManager.effects.append(EricisBirth(ox, oy, self.birth_ericis))

    def birth_ericis(self):
        ox = (Settings.breach_center[0]-2.5) * Settings.tilesize
        oy = (Settings.breach_center[1]-3) * Settings.tilesize
        SpacialSFX("dragon",ox, oy, real_delta_time= True, max_volume= True, loop=True, given_length=25.0) 

        EffectsManager.effects.append(Ericis(ox, oy))

        AudioManager.change_music(3)



    def update(self, delta_time):
        delta_time = Match.game.gameWindow.delta_time()
        if self.start == False:
            self.start = True
            self.start_end()

        self.timer += delta_time

        if self.timer > 5.0 and len(self.tile_list) > 0:
            if self.firestarted:
                chosen = random.sample(self.tile_list, 10 if len(self.tile_list) > 9 else len(self.tile_list))
                for item in chosen:
                    self.tile_list.remove(item)
                    EffectsManager.effects.append(EricisFire(item))
            else:
                self.firestarted = True
                SpacialSFX("spitfire",1, 1, real_delta_time= True, max_volume= True) 
                SpacialSFX("portalcrack",1, 1, real_delta_time=True, max_volume= True) 
            if self.boom_timer - self.timer < -1.0:
                self.boom_timer = self.timer
                SpacialSFX("portalcrack",1, 1, real_delta_time=True, max_volume= True) 
                

        if self.timer > 15.0:
            self.courtain.fill((0,0,0, min(255*(self.timer - 15.0) + 1, 255)))
            self.game.screen.blit(self.courtain, (0,0))

        if self.timer > 20.0:
            self.courtainB.set_alpha(min(255*(0.2*(self.timer - 20.0)) + 1, 255))            
            self.game.screen.blit(self.courtainB, (0,0))

        if self.timer > 30.0:
            self.mainmenu()
            

    def mainmenu(self):      
        from screens.game import Game
        Settings.current_screen = Settings.mainmenuscreen
        Settings.gamescreen = Game(Match.game.gameWindow)


