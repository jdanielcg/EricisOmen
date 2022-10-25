# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from enum import Enum


class Settings:
    #classe para armazenar configurações e propriedades globais

    tilesize = 32
    tile_number_u = 60
    tile_number_v = 60
    show_debug = False
    breach_level = 1
    game_won = False
    dominion_threshold = 1

    def __init__(self):
        self.game_w = 1280
        self.game_h = 720
        self.current_screen = None
        self.mainmenuscreen = None
        self.gamescreen = None
        self.gameApplicationName = "EricisOmen"

        #variavéis da partida
        self.portal_level_percent = 0

#varaivel que determina o estado princiapl de interação com o jogo
class SimulationMode(Enum):
    BUILDING = 1
    RUNNING = 0
