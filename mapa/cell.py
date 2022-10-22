# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint

from settings import Settings

class Cell:
    def __init__(self, location, tile_code = 0, image_size = (32, 32)):
        self.image_size = image_size
        self.location = location
        self.tile_code = tile_code                    
        self.buildable = True
        self.walkable = True
        self.creature = None
        self.building = None
        self.dominion_level = 0
        self.original_code = tile_code
        self.is_dominion_border = False
        self.is_map_edge = False
        self.resource = None

    @property
    def u(self):    return self.location[0]
    @property
    def v(self):    return self.location[1]
    @property
    def x(self):    return self.location[0]*Settings.tilesize    
    @property
    def y(self):    return self.location[1]*Settings.tilesize