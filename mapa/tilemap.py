# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint
import pygame
import json

from world import World


class Tilemap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.tile_w, self.tile_h = tileset.tile_size

        self.surface = pygame.Surface((self.tile_w*20, self.tile_h*20))
        self.rect = self.surface.get_rect()        

    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()
        for v in range(height):
            for u in range(width):                
                tile = self.tileset.get_tile(world.cells[v][u].tile_code)
                self.surface.blit(tile, (u*self.tile_w, v*self.tile_h))
                screen.blit(tile, (u*self.tile_w, v*self.tile_h))





