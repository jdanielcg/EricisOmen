# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from random import randint
from pathfinding.core.node import Node

from settings import Settings

class Cell:
    def __init__(self, location, tile_code = 0, image_size = (32, 32)):
        self.image_size = image_size
        self.code = location[0]*10000 + location[1]
        self.location = location
        self.tile_code = tile_code                    
        self.buildable = True
        self.walkable = True
        
        self.building = None
        self.dominion_level = 0
        self.original_code = tile_code
        self.is_dominion_border = False
        self.is_map_edge = False

        self.resource = None
        self.resource_amount = 0
        
        self.node : Node = None

        #celulas vizinhas proximas
        self.close_neighbors = []

        #controla a ocupação do ladrilho por criaturas
        self.creature = None
        self.future_creature = None

        #registra se a celula é uma posicção possivel de ataque
        self.possible_attack_position = False

    def update(self):
        # remove criatura que não está mais ocupando celula
        if self.creature != None:
            if self.creature.current_cell != self:
                self.creature = None
        # remove criatura que não está mais se encaminhando para a celula       
        if self.future_creature != None:
            #print("cell:", self.code, " f_creat: ", self.future_creature.code, " f_creat: f_cell",
            # self.future_creature.future_cell.code if self.future_creature.future_cell != None else "None")
            if self.future_creature.future_cell != self:
                self.future_creature = None


        #prepara o no do pathfinder
        if self.node != None:
            self.node.walkable = self.vacant
    
    
    #usada para verificar se a célula é ocupavel
    @property
    def vacant(self):
        return self.walkable and self.creature == None and self.future_creature == None

    @property
    def u(self):    return self.location[0]
    @property
    def v(self):    return self.location[1]
    @property
    def x(self):    return self.location[0]*Settings.tilesize    
    @property
    def y(self):    return self.location[1]*Settings.tilesize