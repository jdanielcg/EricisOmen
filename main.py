from PPlay.window import*
from globals import Globals
from screens.game import Game
from screens.mainmenu import MainMenu

def main():
    g = Globals()   

    gameWindow = Window(g.game_w,g.game_h)
    gameWindow.set_title(g.gameApplicationName)

    g.gamescreen = Game(g, gameWindow)
    g.mainmenuscreen = MainMenu(g,gameWindow)
    g.current_screen = g.mainmenuscreen
    
    while g.current_screen != None:
        delta_time = gameWindow.delta_time()
        g.current_screen.update(delta_time)
        gameWindow.update()


#verifica se esse é o script inicial e roda a função main
if __name__ == "__main__":    
    main()
