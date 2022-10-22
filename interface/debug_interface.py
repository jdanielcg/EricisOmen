# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from pygame import Surface
from PPlay.sprite import *
from interface.icons import text_icon
from interface.minimap import Minimap
from interface.textbutton import TextButton
from match import Match
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
        self.debug_up_ripple = TextButton(gw, self.build_obelisk, (20,590), "OBELISK") 
        self.buildmining_button = TextButton(gw, self.build_mining, (20,620), "MINING")

        self.resources_back = Surface((150, 130))        
        self.resources_back.fill((0,0,0))
        self.resources_back.set_alpha(150)
        self.minimap = Minimap(game.world)


#######################fuções dos botões
    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_mining(self):
        self.game.building_mode_interface.start("miningcamp")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_firetower(self):
        self.game.building_mode_interface.start("firetower")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_obelisk(self):
        self.game.building_mode_interface.start("obelisk")
        self.game.simulation_mode = SimulationMode.BUILDING

    def show_debug_info(self):
        Settings.show_debug = not Settings.show_debug


#########################################

    def update(self, delta_time):
        self.buildtestbutton.update()  
        self.buildtestbutton2.update()  
        self.debug_show_button.update()
        self.debug_up_ripple.update()
        self.buildmining_button.update()

        self.game.screen.blit(self.resources_back, (150,500))
                    
        self.game.screen.blit(text_icon("wood", str(Match.wood)),(160,510))
        self.game.screen.blit(text_icon("iron", str(Match.iron)),(160,530))
        self.game.screen.blit(text_icon("worker", str(Match.workers)),(160,550))
        self.game.screen.blit(text_icon("soldier", str(Match.soldiers)),(160,570))
        self.game.screen.blit(text_icon("aether", str(Match.aether)),(160,590))
        self.minimap.update()



            

