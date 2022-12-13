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

    def __init__(self, gamewindow, game):
        self.gamewindow = gamewindow        
        self.s = Settings
        self.game = game
        self.show_buttons = False

        #atalhos
        w = self.gamewindow.width
        h = self.gamewindow.height        
        

        self.speed_up_button = TextButton( self.speed_up, (20,440), "SPEED UP")    
        self.speed_down_button = TextButton( self.speed_down, (20,470), "SPEED DOWN")    
        self.debug_show_button = TextButton( self.show_debug_info, (20,560), "SHOW PATH")   
        self.debug_up_ripple = TextButton( self.build_obelisk, (20,590), "OBELISK") 
        self.buildmining_button = TextButton( self.build_mining, (20,620), "MINING")
        self.buildmill_button = TextButton( self.build_lumber, (20,650), "LUMBER")        
        self.buildwall_button = TextButton( self.build_wall, (20,530), "WALL")  
        self.buildfiretower = TextButton( self.build_firetower, (20,410), "FIRETOWER")  
        self.buildicetower = TextButton( self.build_icetower, (20,380), "ICETOWER")  
        self.buildstonetower = TextButton( self.build_stonetower, (20,350), "STONETOWER")  
        self.buildpoisontrap_button = TextButton( self.build_poisontrap, (20,320), "POISONTRAP")  
        self.buildfiretrap_button = TextButton( self.build_firetrap, (20,290), "FIRETRAP")  

        self.build_dorm_button = TextButton( self.build_dormitory, (20,260), "DORM")        
        self.build_stock_button = TextButton( self.build_stock, (20,230), "STOCK")   

        
        self.restart_button = TextButton( self.restart_game, (20,200), "RESTART")
        self.main_menu_button = TextButton( self.mainmenu, (20,170), "MAINMENU")
        self.pause_button = TextButton( self.pause, (20,140), "PAUSE (II)")

        self.end_button = TextButton( self.endgame, (20,110), "END")     
        self.lose_button = TextButton( self.losegame, (20,80), "LOSE")     


        

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

    def endgame(self)    :
        Match.simulation_mode = SimulationMode.ENDING

    def losegame(self)    :
        Match.simulation_mode = SimulationMode.LOSE

    def build_wall(self):
        self.game.building_mode_interface.start("wall")
        Match.simulation_mode = SimulationMode.BUILDING   

    def build_dormitory(self):
        self.game.building_mode_interface.start("dormitory")
        Match.simulation_mode = SimulationMode.BUILDING

    def build_stock(self):
        self.game.building_mode_interface.start("stockpile")
        Match.simulation_mode = SimulationMode.BUILDING

    def build_mining(self):
        self.game.building_mode_interface.start("miningcamp")
        Match.simulation_mode = SimulationMode.BUILDING

    def build_lumber(self):
        self.game.building_mode_interface.start("lumbercamp")
        Match.simulation_mode = SimulationMode.BUILDING

    def build_firetower(self):
        self.game.building_mode_interface.start("firetower")
        Match.simulation_mode = SimulationMode.BUILDING
    def build_stonetower(self):
        self.game.building_mode_interface.start("stonetower")
        Match.simulation_mode = SimulationMode.BUILDING
    def build_icetower(self):
        self.game.building_mode_interface.start("icetower")
        Match.simulation_mode = SimulationMode.BUILDING

    def build_poisontrap(self):
        self.game.building_mode_interface.start("poisontrap")
        Match.simulation_mode = SimulationMode.BUILDING
    def build_firetrap(self):
        self.game.building_mode_interface.start("firetrap")
        Match.simulation_mode = SimulationMode.BUILDING
    def build_obelisk(self):
        self.game.building_mode_interface.start("obelisk")
        Match.simulation_mode = SimulationMode.BUILDING

    def show_debug_info(self):
        Settings.show_debug = not Settings.show_debug

    def enable_breach(self):
        Match.beach_enabled = True

    def speed_up(self):
        Match.speed += 1.0

    def speed_down(self):
        Match.speed -= 1.0

    def restart_game(self):
        from screens.game import Game
        Settings.gamescreen = Game(self.gamewindow)
        Settings.current_screen = Settings.gamescreen

    def mainmenu(self):      
        from screens.game import Game
        Settings.current_screen = Settings.mainmenuscreen
        Settings.gamescreen = Game(self.gamewindow)  

    def pause (self):
        Match.speed = 0.0 if Match.speed == 1.0 else 1.0



#########################################

    def update(self, delta_time):
        if not self.show_buttons:
            self.show_debug_button.update()
        else:
            self.show_debug_button.update()
            self.speed_up_button.update()
            self.speed_down_button.update()
            self.build_dorm_button.update()  
            self.buildfiretower.update()  
            self.buildicetower.update()  
            self.buildstonetower.update()  
            self.debug_show_button.update()
            self.debug_up_ripple.update()
            self.buildmining_button.update()
            self.buildmill_button.update()
            self.buildwall_button.update()
            self.buildfiretrap_button.update()
            self.buildpoisontrap_button.update()
            self.build_stock_button.update()
            self.end_button.update()
            self.lose_button.update()
            self.main_menu_button.update()
            self.pause_button.update()
            self.restart_button.update()

            self.game.screen.blit(self.resources_back, (150,500))

            self.game.screen.blit(text_icon("wood", str(Match.wood) + " / " + str(Match.max_stock)),(160,510))
            self.game.screen.blit(text_icon("iron", str(Match.iron)+ " / " + str(Match.max_stock)),(160,530))            
            self.game.screen.blit(text_icon("soldier", str(len(Match.allies)) + " / " + str(Match.max_population)),(160,570))
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



            

