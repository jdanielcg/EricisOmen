# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from enum import Enum


class Settings:
    #classe para armazenar configurações e propriedades globais

    tilesize = 32
    show_debug = False

    def __init__(self):
        self.game_w = 1280
        self.game_h = 720
        self.current_screen = None
        self.mainmenuscreen = None
        self.gamescreen = None
        self.gameApplicationName = "EricisOmen"

        #variavéis da partida
        self.portal_level_counter = 1
        self.portal_level_percent = 0

#varaivel que determina o estado princiapl de interação com o jogo
class SimulationMode(Enum):
    BUILDING = 1
    RUNNING = 0
