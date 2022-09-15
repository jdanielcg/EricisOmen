import pygame

class Creatureset:
    def __init__(self, file_name, tile_size=(32, 32)):
        self._filename = file_name
        self.tile_size = tile_size
        self._image = pygame.image.load(self._filename)
        self._image.convert()
        self._image_rect = self._image.get_rect()
        self._creature_library = {}
        self.load_library()


    #Cria uma lista com as "surfaces" que representam os tiles
    def load_library(self):
        #limpa o dicionário
        self._creature_library = {}
        x0 = y0 = 0
        w, h = self._image_rect.size
        dx = self.tile_size[0]
        dy = self.tile_size[1]
        
        creature_index = 0
        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
                tile = pygame.Surface(self.tile_size)                
                tile.fill((255, 0, 255))

                tile.blit(self._image, (0, 0), (x, y, *self.tile_size))
                tile.set_colorkey((255, 0 , 255))
                tile.convert_alpha()

                self._creature_library[creature_index] = tile
                creature_index +=1
        

    #Função que retorna um ladrilho no formato surface
    def get_tile(self, creature_code):
        return self._creature_library.get(creature_code, self._creature_library[0])

    def get_tileset_size(self):
        return len(self._creature_library)