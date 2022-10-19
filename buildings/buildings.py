#loads all info about buildings and their sprites
import pygame
from settings import Settings

class Building:
    def __init__(self, posUV, info):
        self.posUV = posUV
        self.info = info
        
    def posXY(self):
        return (Settings.tilesize * self.posUV[0], Settings.tilesize * self.posUV[1])

class BuildingInfo:
    def __init__(self, name, origin, size, atlas, walkable):
        self.name = name
        self.origin = origin
        self.size = size      
        self.mask = self.generate_cellMask(size) 
        self.atlas = atlas
        self.walkable = False
        self.surf = self.make_surf()
        self.silhouette = self.make_silhouette((0, 255, 0))
        self.silhouette_red = self.make_silhouette((255, 0, 0))

    def generate_cellMask(self, size):
        mask = []
        for n in range(size[0]):
            for m in range(size[1]):
                mask.append((n,m))
        return mask


    def make_surf(self):
        x0 = Settings.tilesize * self.origin[0]
        y0 = Settings.tilesize * self.origin[1]        
        dx = Settings.tilesize * self.size[0]
        dy = Settings.tilesize * self.size[1]

        surf = pygame.Surface((dx, dy))
        surf.fill((255, 0, 255))
        surf.blit(self.atlas, (0,0), (x0, y0, x0 + dx, y0 + dy))
        surf.set_colorkey((255, 0 , 255))
        return surf

    def make_silhouette(self, color):
        dx = Settings.tilesize * self.size[0]
        dy = Settings.tilesize * self.size[1]

        sil = pygame.Surface((dx, dy))
        sil.fill(color)
        sil.set_alpha(200)
        return sil
        