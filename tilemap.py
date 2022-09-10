from random import randint
import pygame
import json


class Tilemap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.tile_w, self.tile_h = tileset.tile_size

        # Matriz de tile_codes
        self.map_matrix = []
        self.surface = pygame.Surface((self.tile_w*20, self.tile_h*20))
        self.rect = self.surface.get_rect()        
        self.make_map_from_file()

    # Cria map_matrix com valores sequenciais para testes
    def make_sequential_map(self):
        self.map_matrix = []
        ii = jj = 16
        for i in range(ii):
            line = []
            for j in range(jj):
                tile_code = i*jj + j
                line.append(tile_code)
            self.map_matrix.append(line)

    # Cria map_matrix com valores apartir de um arquino json
    def make_map_from_file(self):        
        tilemap_data = {}
        with open("world.tmj") as json_file:
            tilemap_data = json.load(json_file)

        # verifica sucesso da leitura
        if len(tilemap_data) > 0:
            height = tilemap_data["layers"][0]["height"]
            width = tilemap_data["layers"][0]["width"]
            self.map_matrix = []
            for h in range(height):
                line = []
                for w in range(width):
                    tile_code = tilemap_data["layers"][0]["data"][h*width + w] - 1
                    line.append(tile_code)
                self.map_matrix.append(line)

    def draw_tilemap(self, game_widnow):
        height = len(self.map_matrix)
        width = len(self.map_matrix[0])

        for y in range(height):
            for x in range(width):
                tile = self.tileset.get_tile(self.map_matrix[y][x])
                self.surface.blit(tile, (x*self.tile_w, y*self.tile_h))
        game_widnow.get_screen().blit(self.surface, (0, 0))

    def __str__(self):
        return f'{self.__class__.__name__} {self._tile_number}'
