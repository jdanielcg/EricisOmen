from PPlay.sprite import *
from settings import SimulationMode
from interface.spritebutton import SpriteButton

class DebugInterface:

    def __init__(self, s, gamewindow, game):
        self.gamewindow = gamewindow
        self.s = s
        self.game = game

        #atalhos
        w = self.gamewindow.width
        h = self.gamewindow.height        
        gw = gamewindow

        self.buildtestbutton = SpriteButton(gw, self.build_dormitory, (20,500), "help.png")        


#######################fuções dos botões
    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        self.game.simulation_mode = SimulationMode.BUILDING


#########################################

    def update(self, delta_time):
        self.buildtestbutton.update()  
                    



            

