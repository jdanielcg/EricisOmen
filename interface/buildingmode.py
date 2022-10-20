# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import floor
from settings import SimulationMode
from settings import Settings

class BuildingMode:

    def __init__(self, game):
        self.game = game
        self.screen = game.gameWindow.get_screen()
        self.mouse = game.gameWindow.get_mouse()
        self.selected = None
        self.cliked = False

    def start(self, name):
        self.selected = self.game.buildings_manager.infos[name]
        self.cliked = False

    def update(self, delta_time):
        if self.selected != None:
            pos = self.mouse.get_position()
            u = floor(pos[0]/Settings.tilesize)
            v = floor(pos[1]/Settings.tilesize)

            x = u*Settings.tilesize
            y = v*Settings.tilesize

            possible = True
            for cell_mask in self.selected.mask:
                vc = v + cell_mask[1]
                uc = u + cell_mask[0]
                if not self.game.world.cells[vc][uc].walkable :
                    possible = False                   

            self.screen.blit(self.selected.silhouette if possible else self.selected.silhouette_red, (x,y))

            if possible:
                #verifica o click para construcao
                if self.mouse.is_button_pressed(True):
                    if not self.cliked:                    
                        self.cliked = True
                #a ação ocorre ao soltar o botão, evitando erros
                elif self.cliked:                
                    self.build((u,v))
                    self.cliked = False

    def build(self, posUV):        
        self.game.buildings_manager.add(self.selected, posUV)
        self.game.simulation_mode = SimulationMode.RUNNING



