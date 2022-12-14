# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


import pygame

class Tileset:
    def __init__(self, file_name, tile_size=(32, 32)):
        self._filename = file_name
        self.tile_size = tile_size
        self._image = pygame.image.load(self._filename)
        self._image.convert_alpha()
        self._image_rect = self._image.get_rect()
        self._tile_library = {}
        self._tile_library_alpha = {}
        self.load_library()


    #Cria uma lista com as "surfaces" que representam os tiles
    def load_library(self):
        #limpa o dicionário
        self._tile_library = {}
        self._tile_library_alpha = {}
        x0 = y0 = 0
        w, h = self._image_rect.size
        dx = self.tile_size[0]
        dy = self.tile_size[1]
        
        tile_index = 0
        for y in range(y0, h, dy):
            for x in range(x0, w, dx):
                #cria o tile normal
                tile = pygame.Surface(self.tile_size)
                tile.blit(self._image, (0, 0), (x, y, *self.tile_size))                
                self._tile_library[tile_index] = tile

                #cria a versão com alpha
                tile_alpha = pygame.Surface(self.tile_size, pygame.SRCALPHA)
                tile_alpha.blit(self._image, (0, 0), (x, y, *self.tile_size),special_flags = pygame.BLEND_RGBA_ADD)
                self._tile_library_alpha[tile_index] = tile_alpha

                tile_index +=1
        

    #Função que retorna um ladrilho no formato surface
    def get_tile(self, tile_code):
        return self._tile_library.get(tile_code, self._tile_library[0])

    #Função que retorna um ladrilho no formato surface com alfa
    def get_tile_alpha(self, tile_code):        
        return self._tile_library_alpha.get(tile_code, self._tile_library_alpha[0])

    def get_tileset_size(self):
        return len(self._tile_library)