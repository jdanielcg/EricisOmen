# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from pygame import Surface
from PPlay.sprite import *
from PPlay.window import Window
from interface.breachmeter import setup_breachmeter, update_breachmeter
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
        self.show_buttons = False

        #atalhos
        w = self.gamewindow.width
        h = self.gamewindow.height        
        

        self.speed_up_button = TextButton( self.speed_up, (20,440), "SPEED UP")    
        self.speed_down_button = TextButton( self.speed_down, (20,470), "SPEED DOWN")    
        self.buildtestbutton = TextButton( self.build_dormitory, (20,500), "DORM")        
        self.buildtestbutton2 = TextButton( self.build_firetower, (20,530), "FIRETOWER")  
        self.debug_show_button = TextButton( self.show_debug_info, (20,560), "SHOW PATH")   
        self.debug_up_ripple = TextButton( self.build_obelisk, (20,590), "OBELISK") 
        self.buildmining_button = TextButton( self.build_mining, (20,620), "MINING")
        self.buildmill_button = TextButton( self.build_lumber, (20,650), "LUMBER")        
        self.restart_button = TextButton( self.restart_game, (round(w/2 - 50),round(h/2-10)), "RESTART")

        self.show_debug_button = TextButton( self.show_debug_menu, (20,680), "DEBUG MENU")  

        self.resources_back = Surface((150, 130))        
        self.resources_back.fill((0,0,0))
        self.resources_back.set_alpha(150)
        self.minimap = Minimap(game.world)

        self.won_lost_back = Surface((w, 200))        
        self.won_lost_back.fill((0,0,0))
        self.won_lost_back.set_alpha(200)

        setup_breachmeter()


#######################fuções dos botões

    def show_debug_menu(self):
        self.show_buttons = not self.show_buttons        

    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_mining(self):
        self.game.building_mode_interface.start("miningcamp")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_lumber(self):
        self.game.building_mode_interface.start("lumbercamp")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_firetower(self):
        self.game.building_mode_interface.start("firetower")
        self.game.simulation_mode = SimulationMode.BUILDING

    def build_obelisk(self):
        self.game.building_mode_interface.start("obelisk")
        self.game.simulation_mode = SimulationMode.BUILDING

    def show_debug_info(self):
        Settings.show_debug = not Settings.show_debug

    def enable_breach(self):
        Match.beach_enabled = True

    def speed_up(self):
        Match.speed += 1.0

    def speed_down(self):
        Match.speed -= 1.0

    def restart_game(self):
        print("restarts the game")


#########################################

    def update(self, delta_time):
        if not self.show_buttons:
            self.show_debug_button.update()
        else:
            self.show_debug_button.update()
            self.speed_up_button.update()
            self.speed_down_button.update()
            self.buildtestbutton.update()  
            self.buildtestbutton2.update()  
            self.debug_show_button.update()
            self.debug_up_ripple.update()
            self.buildmining_button.update()
            self.buildmill_button.update()

            self.game.screen.blit(self.resources_back, (150,500))

            self.game.screen.blit(text_icon("wood", str(Match.wood)),(160,510))
            self.game.screen.blit(text_icon("iron", str(Match.iron)),(160,530))
            self.game.screen.blit(text_icon("worker", str(Match.workers)),(160,550))
            self.game.screen.blit(text_icon("soldier", str(Match.soldiers)),(160,570))
            self.game.screen.blit(text_icon("aether", str(Match.aether)),(160,590))

        #desenha a mensagem de vitória caso jogo ganho
        if Match.game_won:
            w = Window.screen.get_width()
            h = Window.screen.get_height()
            surf = text_icon("book", "GAME WON", large= True)
            w = round(w/2 - surf.get_width()/2)
            h = round(h/2 - surf.get_height())

            self.game.screen.blit(self.won_lost_back,(0,h-100))
            self.game.screen.blit(surf,(w,h))
            self.restart_button.update()

        #desenha a mensagem de derrota caso jogo seja perdido
        if Match.game_lost:
            w = Window.screen.get_width()
            h = Window.screen.get_height()
            surf = text_icon("book", "GAME LOST", large= True)
            w = round(w/2 - surf.get_width()/2)
            h = round(h/2 - surf.get_height())

            self.game.screen.blit(self.won_lost_back,(0,h-100))
            self.game.screen.blit(surf,(w,h))
            self.restart_button.update()

        #atualiza o minimapa
        self.minimap.update()

        #atualiza o medidor da fenda
        update_breachmeter(delta_time)



            

