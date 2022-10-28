# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint
import pygame
import json
from camera import Camera
from mapa.borderchecker import border_maker, can_be_dominated
from settings import Settings

from world import World


class Tilemap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.tile_w, self.tile_h = tileset.tile_size

        self.debug_red = pygame.Surface((32,32))
        self.debug_red.fill((255,0,0))
        self.debug_red.set_alpha(150)

        self.debug_blue = pygame.Surface((32,32))
        self.debug_blue.fill((0,0,255))
        self.debug_blue.set_alpha(150)

        self.debug_green = pygame.Surface((32,32))
        self.debug_green.fill((0,255,0))
        self.debug_green.set_alpha(150)

        #self.surface = pygame.Surface((self.tile_w*20, self.tile_h*20))
        #self.rect = self.surface.get_rect()        

    def draw(self, game_window, world):
        height = world.height
        width = world.width
        screen = game_window.get_screen()

        cell = None
        for v in range(Camera.rootV, Camera.rootV + Camera.nV()):
            for u in range(Camera.rootU, Camera.rootU + Camera.nU()):  
                cell = world.cells[v][u]

                tile_code = cell.tile_code
                tile = self.tileset.get_tile(cell.tile_code)

                #verifica para criar a mancha de dominio no piso
                if can_be_dominated(cell) and not cell.is_map_edge:
                    border_tile_code = border_maker(cell, world)
                    cell.is_dominion_border = border_tile_code != 208
                    tile = self.tileset.get_tile(border_tile_code)

                #verifica para desenhar recurso no piso
                extra_surf = None
                if cell.resource != None and cell.resource_amount > 0:
                    #cell.walkable = False
                    if cell.resource == "wood":
                        if cell.dominion_level > Settings.dominion_threshold:
                            extra_surf = self.tileset.get_tile_alpha(68)
                        else:
                            extra_surf = self.tileset.get_tile_alpha(67)
                    elif cell.resource == "iron":
                        extra_surf = self.tileset.get_tile_alpha(66)

                debug_mark = None
                if Settings.show_debug:
                    if not cell.vacant:
                        debug_mark = self.debug_red
                    if cell.future_creature != None:
                        debug_mark = self.debug_blue
                    if cell.possible_attack_position == True:
                        debug_mark = self.debug_green

                screen.blit(tile, (cell.x - Camera.dx, cell.y - Camera.dy))

                if debug_mark != None:
                    screen.blit(debug_mark, (cell.x - Camera.dx, cell.y - Camera.dy))

                if extra_surf != None :
                    screen.blit(extra_surf, (cell.x - Camera.dx, cell.y - Camera.dy))
                #self.surface.blit(tile, (cell.x, cell.y))




