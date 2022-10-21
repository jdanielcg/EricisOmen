# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from PPlay.sprite import *
from interface.textbutton import TextButton
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

        self.buildtestbutton = TextButton(gw, self.build_dormitory, (20,500), "DORM")        
        self.buildtestbutton2 = TextButton(gw, self.build_firetower, (20,530), "FIRETOWER")  
        self.debug_show_button = TextButton(gw, self.show_debug_info, (20,560), "SHOW PATH")   
        self.debug_up_ripple = TextButton(gw, self.show_debug_info, (20,590), "UP PORTAL")


#######################fuções dos botões
    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_firetower(self):
        self.game.building_mode_interface.start("firetower")
        self.game.simulation_mode = SimulationMode.BUILDING

    def show_debug_info(self):
        Settings.show_debug = not Settings.show_debug


#########################################

    def update(self, delta_time):
        self.buildtestbutton.update()  
        self.buildtestbutton2.update()  
        self.debug_show_button.update()
        self.debug_up_ripple.update()
                    



            

