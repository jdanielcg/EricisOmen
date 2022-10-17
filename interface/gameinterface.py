from PPlay.sprite import *
from interface.spritebutton import SpriteButton

class Gameinterface:

    def __init__(self,g, gamewindow):
        self.gamewindow = gamewindow
        self.g = g

        #atalhos
        w = self.gamewindow.width
        h = self.gamewindow.height        
        gw = gamewindow

        self.menu_jogo = SpriteButton(gw, self.show_menu_bar, (12,12), "menu_jogo.png")
        self.build_menu_button = SpriteButton(gw, self.show_build_menu, (w/2 - 265, 20), "Botao_jogo_construct.png")
        self.close_build_button = SpriteButton(gw, self.show_build_menu, (140, h/2 - 210), "Botao_close.png")
        self.resources_menu_button = SpriteButton(gw, self.not_implemented, (w/2 - 165, 20), "Botao_jogo_resources.png")
        self.research_menu_button = SpriteButton(gw, self.not_implemented, (w/2 - 65, 20), "Botao_jogo_research.png")
        self.reports_menu_button = SpriteButton(gw, self.not_implemented, (w/2 + 35, 20), "Botao_jogo_reports.png")
        self.options_menu_button = SpriteButton(gw, self.not_implemented, (w/2 + 135, 20), "Botao_jogo_options.png")

        #variaveis de controle da exibição de menus
        self.menu_bar_enabled = False
        self.build_menu_enabled = False
        self.resources_menu_enabled = False
        self.researches_menu_enabled = False
        self.reports_menu_enabled = False
        self.options_menu_enabled = False

        #painel barra de botoes jogo
        self.menu_button_bar = Sprite("assets\Buttons\Barra_botoes_jogo.png")
        self.menu_button_bar.set_position(w/2 - 340,7)  
        
        #painel portal level 
        self.portal_level = Sprite("assets\Buttons\portal_level.png")
        self.portal_level.set_position(w/2 + 450, 12)

        #menu buildings
        self.build_panel = Sprite("assets\Buttons\Barra_botoes2_jogo.png")
        self.build_panel.set_position(20,h/2 - 220) 


#######################fuções dos botões
    def not_implemented(self):
        print("function not implemented")

    def show_menu_bar(self):
        #inverte valor da variável        
        self.menu_bar_enabled = not self.menu_bar_enabled
    
    def show_build_menu(self):             
        self.build_menu_enabled = not self.build_menu_enabled

    def show_resources_menu(self):             
        self.resources_menu_enabled = not self.resources_menu_enabled
#########################################

    def draw_portal_level_panel(self):
        #escreve as coisas dentro do painel portal level
        gw = self.gamewindow
        w = self.gamewindow.width
        h = self.gamewindow.height

        gw.draw_text("Portal Level: ", w/2 + 470, 23, size=20, bold=True, color=(0, 0, 0))
        gw.draw_text(str(self.g.portal_level_counter), w/2 + 595, 23.5, size=20, bold=True, color=(0, 0, 0))
        gw.draw_text(str(self.g.portal_level_percent), w/2 + 482, 47, size=17, bold=True, color=(0, 0, 0))
        gw.draw_text("% Chance of", w/2 + 493, 48, size=17, bold=True, color=(0, 0, 0))
        gw.draw_text("spawning Ericis", w/2 + 474, 68, size=17, bold=True, color=(0, 0, 0))


    def update(self, delta_time):
        self.menu_jogo.update()
        self.portal_level.draw()    
        self.draw_portal_level_panel()          
        
        if self.menu_bar_enabled:   
            self.menu_button_bar.draw()  
            self.build_menu_button.update()  
            self.resources_menu_button.update()   
            self.research_menu_button.update()  
            self.reports_menu_button.update()
            self.options_menu_button.update()

        #menu de construção
        if self.build_menu_enabled:
            self.build_panel.draw()
            self.close_build_button.update()

        #menu resources
        if self.resources_menu_enabled:
            pass

        #menu researches
        if self.researches_menu_enabled:
            pass

        #menu resources
        if self.reports_menu_enabled:
            pass

        #menu options
        if self.options_menu_enabled:
            pass
                    



            

