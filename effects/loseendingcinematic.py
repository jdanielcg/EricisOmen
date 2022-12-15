import math
import random

from pygame import Surface
import pygame
from audio.audiomanager import AudioManager
from camera import Camera
from effects.effectsmanager import EffectsManager
from match import Match
from settings import Settings
from effects.effects import EricisBirth, Ericis, EricisFire

class LostEnding():
    def __init__(self, game):
        self.game = game
        self.tile_list = []

        self.start = False
        self.timer = 0.0

        self.courtain = Surface((game.screen.get_width(), game.screen.get_height()), pygame.SRCALPHA)
        self.courtain.fill((40,40,40,0))

        font = pygame.font.SysFont("bahnschrift semibold", 45, False, False)

        #cria a surface com o texto escrito
        credits = [
                    font.render("A FENDA FOI DESTRUIDA, FIM DE JOGO", True, (255,255,255)),
                    ]
        ty = 275
        for credit in credits:
            tx =  game.screen.get_width()/2.0 - credit.get_width()/2.0 
            self.courtain.blit(credit, (tx, ty))
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

        EffectsManager.effects.append(EricisFire(self.game.world.cells[ov -1 ][ou - 1]))




    def update(self, delta_time):
        delta_time = Match.game.gameWindow.delta_time()
        if self.start == False:
            self.start = True
            self.start_end()

        self.timer += delta_time

        if self.timer > 5.0 and len(self.tile_list) > 0:
            chosen = random.sample(self.tile_list, 20 if len(self.tile_list) > 19 else len(self.tile_list))
            for item in chosen:
                self.tile_list.remove(item)
                item.dominion_level = -100

        if self.timer > 10.0:
            self.courtain.set_alpha(min(255*(0.4*(self.timer - 10.0)) + 1, 255))  
            self.game.screen.blit(self.courtain, (0,0))

        if self.timer > 20.0:
            self.mainmenu()

    def mainmenu(self):      
        AudioManager.change_music(1)
        from screens.game import Game
        Settings.current_screen = Settings.mainmenuscreen
        Settings.gamescreen = Game(Match.game.gameWindow)


            


