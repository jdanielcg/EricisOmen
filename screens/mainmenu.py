# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: RAMON SANTOS         ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from PPlay.sprite import *
from pygame import mixer

class MainMenu:
    def __init__(self,g, gamewindow):
        self.g = g      
        self.gameWindow = gamewindow

        #musica do menu
        self.p_musica = True
        self.is_playing_music = True
        mixer.init()
        mixer.music.load('assets\menu.mp3')
        self.music_volume = 0.5
        mixer.music.set_volume(self.music_volume)
        mixer.music.play(-1)        
        
        #pegando a entrada do usuário
        self.teclado = gamewindow.get_keyboard()
        self.mouse = gamewindow.get_mouse()
        
        #fundo do menu
        self.background_image = Sprite("assets\dragao.webp")
        
        #titulo
        self.title_image = Sprite("assets\Titulo.png")
        self.title_image.set_position(1280/2 - 280, 50)
        
        #janela help
        self.janelahelp = Sprite("assets\submenu.png")
        self.janelahelp.set_position(1280/2 - 460, 65)
        self.p_help = False
        
        #janela settings
        self.janelasettings = Sprite("assets\submenu.png")
        self.janelasettings.set_position(1280/2 - 460, 65)
        self.p_settings = False
        
        #botao play
        self.play_button = Sprite("assets\Buttons\play.png")
        self.play_button.set_position(1280/2 - 120, 250)
        
        #botao settings
        self.settings_button = Sprite("assets\Buttons\settings.png")
        self.settings_button.set_position(1280/2 - 120, 350)
        self.settings_panel_enabled = False
        
        #botao exit
        self.exit_button = Sprite("assets\Buttons\exit.png")
        self.exit_button.set_position(1280/2 - 120 , 450)
        
        #botao help
        self.help_button = Sprite("assets\Buttons\help.png")
        self.help_button.set_position(1260 - 70 , 630)
        self.help_panel_enabled = False
        
        #botao music
        self.music_mute_button = Sprite("assets\Buttons\music.png")
        self.music_mute_button.set_position(1260 - 150, 630)
        
        #botao quit panel
        self.quit_panel_button = Sprite("assets\Buttons\quit.png")
        self.quit_panel_button.set_position(1280/2 - 120, 570)
        self.p_quit_panel = False
        
        #creditos
        self.credits_button = Sprite("assets\creditos.png")
        self.credits_button.set_position(1280/2 - 280 , 550)

    def update(self, delta_time):
        self.background_image.draw()
        self.title_image.draw()
        self.play_button.draw()
        self.settings_button.draw()
        self.music_mute_button.draw()
        self.credits_button.draw()
        self.exit_button.draw()       
        self.help_button.draw()

        #botao play
        if self.mouse.is_over_object(self.play_button) and self.mouse.is_button_pressed(True):
            self.g.current_screen = self.g.gamescreen

        #botao exit
        if self.mouse.is_over_object(self.exit_button) and self.mouse.is_button_pressed(True):
            self.gameWindow.close()

        #botão music
        if self.mouse.is_over_object(self.music_mute_button):              
            if self.mouse.is_button_pressed(True):
                if not self.p_musica:                    
                    self.p_musica = True
            #a ação ocorre ao soltar o botão, evitando erros
            elif self.p_musica: 
                if self.is_playing_music:
                    mixer.music.pause()               
                else:
                    mixer.music.unpause()   
                self.is_playing_music = not self.is_playing_music             
                self.p_musica = False
        else:                 
            self.p_musica = False       

        #botao help       
        if self.mouse.is_over_object(self.help_button):              
            if self.mouse.is_button_pressed(True):
                if not self.p_help:                    
                    self.p_help = True            
            elif self.p_help:                               
                self.p_help = False
                self.help_panel_enabled = True
        else:                 
            self.p_help = False  

        #botao settings
        if self.mouse.is_over_object(self.settings_button):              
            if self.mouse.is_button_pressed(True):
                if not self.p_settings:                    
                    self.p_settings = True            
            elif self.p_settings:                               
                self.p_settings = False
                self.settings_panel_enabled = True
        else:                 
            self.p_settings = False  


        #desenha o painel de ajuda/about
        if self.help_panel_enabled:
            self.janelahelp.draw()
            self.quit_panel_button.draw()
            self.gameWindow.draw_text("About", self.gameWindow.width/2 - 100, 90, size=60, bold=True, color=(224, 224, 222))

        #desenha o painel de settings
        if self.settings_panel_enabled:
            self.janelasettings.draw()
            self.quit_panel_button.draw()
            self.gameWindow.draw_text("Settings", self.gameWindow.width/2 - 127, 90, size=60, bold=True, color=(224, 224, 222))                        

        #botão sair de painel
        if self.help_panel_enabled or self.settings_panel_enabled:
            if self.mouse.is_over_object(self.quit_panel_button):              
                if self.mouse.is_button_pressed(True):
                    if not self.p_quit_panel:                    
                        self.p_quit_panel = True            
                elif self.p_quit_panel:                               
                    self.p_quit_panel = False
                    self.help_panel_enabled = False
                    self.settings_panel_enabled = False
            else:                 
                self.p_quit_panel = False  



        
        
