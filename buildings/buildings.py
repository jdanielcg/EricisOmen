# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#loads all info about buildings and their sprites
import pygame
from buildings.wall import wall_side_checker
from camera import Camera
from settings import Settings

class Building:
    def __init__(self, posUV, info, game = None):
        self.posUV = posUV
        self.info = info
        self.integrity = info.max_integrity
        self.recharge_time = info.recharge_time
        self.timer = 0
        self.action = info.action
        self.on_destroy = info.on_destroy



        #usada para guardar a referencia para recursos próximos
        self.resource_list = None


        if info.setup_function != None and game != None:
            info.setup_function(self, game.world)

    #substitui as informações e recria a construção
    def morph_to(self, posUV, info):
        self.__init__(posUV, info)
        
    def posXY(self):
        return (Settings.tilesize * self.posUV[0], Settings.tilesize * self.posUV[1])

    def posXY_render(self):
        return (Settings.tilesize * self.posUV[0] - Camera.dx,
                Settings.tilesize * self.posUV[1] - Camera.dy)

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
    def __init__(self, name, origin, size, atlas, walkable = False, action = None,
                 recharge_time = 3, max_integrity = 1000, dominion_factor = 0,
                 iron_cost = 0, aether_cost = 0, wood_cost = 0, on_destroy = None,
                 setup_function = None, gather_type = None, can_demolish = True):
        self.name = name
        self.origin = origin
        self.size = size      
        self.mask = self.generate_cellMask(size) 
        self.atlas = atlas
        self.walkable = walkable
        self.surf = self.make_surf()
        self.silhouette = self.make_silhouette((0, 255, 0))
        self.silhouette_red = self.make_silhouette((255, 0, 0))
        self.max_integrity = max_integrity
        self.action = action
        self.recharge_time = recharge_time
        self.dominion_factor = dominion_factor
        self.on_destroy = on_destroy
        self.setup_function = setup_function
        self.gather_type = gather_type
        self.can_demolish = can_demolish

        #custos
        self.wood_cost = wood_cost
        self.aether_cost = aether_cost
        self.iron_cost = iron_cost

    def get_surf(self, cell = None, world = None):
        if self.name != "wall":
            return self.surf
        elif(self.name == "wall"):
            return self.surf[wall_side_checker(cell, world)]



    def generate_cellMask(self, size):
        mask = []
        for n in range(size[0]):
            for m in range(size[1]):
                mask.append((n,m))
        return mask


    def make_surf(self):
        surf = None
        if self.name != "wall":
            x0 = Settings.tilesize * self.origin[0]
            y0 = Settings.tilesize * self.origin[1]        
            dx = Settings.tilesize * self.size[0]
            dy = Settings.tilesize * self.size[1]

            surf = pygame.Surface((dx, dy))#, pygame.SRCALPHA)
            surf.fill((0, 0, 0, 0))
            surf.blit(self.atlas, (0,0), (x0, y0, x0 + dx, y0 + dy))#, special_flags = pygame.BLEND_RGBA_ADD)
            #surf.set_colorkey((255, 0 , 255))
        elif (self.name == "wall"):
            surf = []
            x0 = Settings.tilesize * self.origin[0]
            y0 = Settings.tilesize * self.origin[1]        
            dx = Settings.tilesize * 1
            dy = Settings.tilesize * 1
            for m in range(4):
                for n in range(10):                
                    ddx = n * dx
                    ddy = m * dy
                    temp_surf = pygame.Surface((dx, dy))
                    temp_surf.blit(self.atlas, (0,0), (x0 + ddx, y0 + ddy, x0 + ddx + dx, y0 + ddy+ dy))
                    surf.append(temp_surf)            
        return surf

    def make_silhouette(self, color):
        dx = Settings.tilesize * self.size[0]
        dy = Settings.tilesize * self.size[1]

        sil = pygame.Surface((dx, dy))
        sil.fill(color)
        sil.set_alpha(200)
        return sil
   