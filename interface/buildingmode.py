
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
            u = pos[0]/Settings.tilesize
            v = pos[1]/Settings.tilesize

            x = floor(u)*Settings.tilesize
            y = floor(v)*Settings.tilesize

            self.screen.blit(self.selected.silhouette, (x,y))

            #verifica o click para construcao
            if self.mouse.is_button_pressed(True):
                if not self.cliked:                    
                    self.cliked = True
            #a ação ocorre ao soltar o botão, evitando erros
            elif self.cliked:                
                self.build((floor(u),floor(v)))
                self.cliked = False

    def build(self, posUV):        
        self.game.buildings_manager.add(self.selected, posUV)
        self.game.simulation_mode = SimulationMode.RUNNING



