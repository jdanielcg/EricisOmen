# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#loads all info about buildings and their sprites
import pygame
from settings import Settings

class Building:
    def __init__(self, posUV, info):
        self.posUV = posUV
        self.info = info
        self.integrity = info.max_integrity
        self.recharge_time = info.recharge_time
        self.timer = 0
        self.action = info.action

    #substitui as informações e recria a construção
    def morph_to(self, posUV, info):
        self.__init__(posUV, info)
        
    def posXY(self):
        return (Settings.tilesize * self.posUV[0], Settings.tilesize * self.posUV[1])

    @property
    def x(self):
        return self.posUV[0]*Settings.tilesize
    
    @property
    def y(self):
        return self.posUV[1]*Settings.tilesize

    @property
    def v(self):
        return self.posUV[1]

    @property
    def u(self):
        return self.posUV[0]

class BuildingInfo:
    def __init__(self, name, origin, size, atlas, walkable, action = None, recharge_time = 3, max_integrity = 1000, dominion_factor = 0):
        self.name = name
        self.origin = origin
        self.size = size      
        self.mask = self.generate_cellMask(size) 
        self.atlas = atlas
        self.walkable = False
        self.surf = self.make_surf()
        self.silhouette = self.make_silhouette((0, 255, 0))
        self.silhouette_red = self.make_silhouette((255, 0, 0))
        self.max_integrity = max_integrity
        self.action = action
        self.recharge_time = recharge_time
        self.dominion_factor = dominion_factor

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

        surf = pygame.Surface((dx, dy), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 0))
        surf.blit(self.atlas, (0,0), (x0, y0, x0 + dx, y0 + dy), special_flags = pygame.BLEND_RGBA_ADD)
        #surf.set_colorkey((255, 0 , 255))
        return surf

    def make_silhouette(self, color):
        dx = Settings.tilesize * self.size[0]
        dy = Settings.tilesize * self.size[1]

        sil = pygame.Surface((dx, dy))
        sil.fill(color)
        sil.set_alpha(200)
        return sil
        