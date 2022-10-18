from PPlay.sprite import *
from settings import Settings, SimulationMode
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
        self.debug_show_button = SpriteButton(gw, self.show_debug_info, (20,600), "help.png")   


#######################fuções dos botões
    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        self.game.simulation_mode = SimulationMode.BUILDING

    def show_debug_info(self):
        Settings.show_debug = not Settings.show_debug


#########################################

    def update(self, delta_time):
        self.buildtestbutton.update()  
        self.debug_show_button.update()
                    



            

