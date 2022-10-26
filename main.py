# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝
import pygame
from PPlay.window import*
from camera import Camera
from interface.customcursor import load_custom_cursor
from match import Match
from screens.game import Game
from screens.mainmenu import MainMenu
from settings import Settings


def main():
    settings = Settings()   

    gameWindow = Window(settings.game_w,settings.game_h)
    gameWindow.set_title(settings.gameApplicationName)

    settings.gamescreen = Game(settings, gameWindow)
    settings.mainmenuscreen = MainMenu(settings,gameWindow)
    settings.current_screen = settings.mainmenuscreen

    load_custom_cursor("cursor16.png")
    

    
    while settings.current_screen != None:
        delta_time = gameWindow.delta_time()*Match.speed
        settings.current_screen.update(delta_time)       

        gameWindow.update()


#verifica se esse é o script inicial e roda a função main
if __name__ == "__main__":    
    main()
