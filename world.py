# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import json
from mapa.cell import*

class World:
    def __init__(self):        
        self.cells = []
        self.creatures = []
        self.building_list = []
        self.generate_map()

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
        for h in range(self.height):
            line = []
            for w in range(self.width):
                tile_code = cells_data["layers"][0]["data"][h*self.width + w] - 1                
                cell = Cell((w, h), tile_code)                
                line.append(cell)
            self.cells.append(line)
