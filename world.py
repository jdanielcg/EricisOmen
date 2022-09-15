import pygame
import json
from creature import Creature
from cell import*

class World:
    def __init__(self):        
        self.cells = []
        self.creatures = []
        self.generate_map()
        self.generate_creatures()

    def update(self, delta_time):        
        for creat in self.creatures:
            creat.update(delta_time)        

    def generate_creatures(self):
        for h in self.cells:
            for w in h:            
                roll = randint(1, 20)
                if roll == 20 :
                    creature = Creature(w.location)
                    self.creatures.append(creature)
        print("generated " + str(len(self.creatures)) + " creatures ")

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

    # cria mundo com valores sequenciais para testes
#    def generate_sequential(self):
#        self.cells = []
#        ii = jj = 24
#        for i in range(ii):
#            line = []
#            for j in range(jj):
#                tile_code = i*jj + j
#                line.append(tile_code)
#            self.cells.append(line)