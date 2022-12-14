# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import json
from math import ceil, floor
from mapa.cell import*
from settings import Settings

class World:
    def __init__(self):        
        self.cells = []
        self.creatures = []
        self.building_list = []
        self._dominion_buildings = []
        self.generate_map()
        self.attack_possible_positions = []
        self.domain_cells = []

    #atualiza a ocupação das celulas
    def update(self, delta_time):      
        self.attack_possible_positions.clear()
        self.domain_cells.clear()
        for cell_line in self.cells:
            for cell in cell_line:
                cell.update()
                #atualiza a lista de posições de ataque possiveis
                cell.possible_attack_position = False
                if cell.dominion_level >= Settings.dominion_threshold and cell.vacant:                    
                    #verificando alvos nos arredores
                    for neighbor in cell.close_neighbors:
                        if neighbor.building != None:
                            self.attack_possible_positions.append(cell)
                            cell.possible_attack_position = True
                
                #atualiza lista de celulas do  dominio
                if cell.dominion_level >= Settings.dominion_threshold:
                    self.domain_cells.append(cell)
    
    def add_dominion(self, building):
        self._dominion_buildings.append(building)            
        
        for cell_line in self.cells:
            for cell in cell_line:
                bu = building.u + floor(building.info.size[0]/2)
                bv = building.v + floor(building.info.size[1]/2)
                factor = building.info.dominion_factor/((cell.location[0] - bu)**2 + (cell.location[1] - bv)**2 + 1)
                cell.dominion_level += factor                

    def remove_dominion(self, building):
        self._dominion_buildings.append(building)
        for cell_line in self.cells:
            for cell in cell_line:
                bu = building.u + floor(building.info.size[0]/2.0)
                bv = building.v + floor(building.info.size[1]/2.0)
                factor = building.info.dominion_factor/((cell.location[0] - bu)**2 + (cell.location[1] - bv)**2 + 1)
                cell.dominion_level -= factor 

    # crial cells com valores apartir de um arquino json
    def generate_map(self):        
        cells_data = {}
        #abre o arquivo
        with open("world.tmj") as json_file:
            cells_data = json.load(json_file)

        # verifica sucesso da leitura
        if len(cells_data) == 0:
            print("erro na leitura do arquivo de mapa")

        self.height = cells_data["layers"][0]["height"]
        self.width = cells_data["layers"][0]["width"]
        self.cells = []
        h_max = self.height -1
        w_max = self.width -1
        for h in range(self.height):
            line = []
            for w in range(self.width):
                tile_code = cells_data["layers"][0]["data"][h*self.width + w] - 1                
                cell = Cell((w, h), tile_code) 
                cell.is_map_edge = (h == h_max or h == 0 or w == 0 or w == w_max) 

                cell.walkable = (tile_code == 0 or tile_code == 1 or tile_code == 2 or
                                tile_code == 3 or tile_code == 4 or tile_code == 5)

                extra = cells_data["layers"][1]["data"][h*self.width + w] - 1 
                if extra == 43 :
                    cell.resource = "wood"   
                    cell.walkable = False 
                    cell.resource_amount = 100
                elif extra == 73:
                    cell.resource = "iron"
                    cell.walkable = False
                    cell.resource_amount = 100

                line.append(cell)
            self.cells.append(line)

        #registra os vizinhos
        for v in range(1,self.height-1):            
            for u in range(1,self.width-1):
                self.cells[v][u].close_neighbors.append(self.cells[v-1][u])
                self.cells[v][u].close_neighbors.append(self.cells[v+1][u])
                self.cells[v][u].close_neighbors.append(self.cells[v][u+1])
                self.cells[v][u].close_neighbors.append(self.cells[v][u-1])
