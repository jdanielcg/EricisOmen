# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint
import pygame
import json
from mapa.borderchecker import border_maker, can_be_dominated
from settings import Settings

from world import World


class Tilemap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.tile_w, self.tile_h = tileset.tile_size

        #self.surface = pygame.Surface((self.tile_w*20, self.tile_h*20))
        #self.rect = self.surface.get_rect()        

    def draw(self, game_window, world):
        height = world.height
        width = world.width
        screen = game_window.get_screen()

        for cell_line in world.cells:
            for cell in cell_line:  

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
                
                        


                screen.blit(tile, (cell.x, cell.y))
                if extra_surf != None :
                    screen.blit(extra_surf, (cell.x, cell.y))
                #self.surface.blit(tile, (cell.x, cell.y))




