# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint
import pygame
import json


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
        for y in range(height):
            for x in range(width):
                tile = self.tileset.get_tile(world.cells[y][x].tile_code)
                self.surface.blit(tile, (x*self.tile_w, y*self.tile_h))
                screen.blit(tile, (x*self.tile_w, y*self.tile_h))

    def __str__(self):
        return f'{self.__class__.__name__} {self._tile_number}'
