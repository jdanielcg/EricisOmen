# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from pickle import TRUE
from PPlay.window import*
from interface.customcursor import load_custom_cursor
from settings import Settings
from screens.game import Game
from screens.mainmenu import MainMenu

def main():
    s = Settings()   

    gameWindow = Window(s.game_w,s.game_h)
    gameWindow.set_title(s.gameApplicationName)

    s.gamescreen = Game(s, gameWindow)
    s.mainmenuscreen = MainMenu(s,gameWindow)
    s.current_screen = s.mainmenuscreen

    load_custom_cursor("cursor.png")

    
    while s.current_screen != None:
        delta_time = gameWindow.delta_time()
        s.current_screen.update(delta_time)       

        gameWindow.update()


#verifica se esse é o script inicial e roda a função main
if __name__ == "__main__":    
    main()
