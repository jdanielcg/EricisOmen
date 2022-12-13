# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from PPlay.window import*
from interface.customcursor import load_custom_cursor
from match import Match
from screens.game import Game
from screens.mainmenu import MainMenu
from settings import Settings



def main():  
    

    gameWindow = Window(Settings.game_w,Settings.game_h)
    gameWindow.set_title(Settings.gameApplicationName)

    Settings.gamescreen = Game(gameWindow)
    Settings.mainmenuscreen = MainMenu(gameWindow)
    Settings.current_screen = Settings.mainmenuscreen

    load_custom_cursor("cursor16.png")   

    
    while Settings.current_screen != None:
        delta_time = gameWindow.delta_time()*Match.speed
        Settings.current_screen.update(delta_time)       

        gameWindow.update()      

 


#verifica se esse é o script inicial e roda a função main
if __name__ == "__main__":    
    main()
