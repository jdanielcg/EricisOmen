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


    dominion_threshold = 1
    breach_required_aether = 300
    breach_center = (30,30)
    enemy_spawns = [(6,6),(6,7),(7,6),(7,7), (54,6), (6, 54), (54,54)]
    max_creatures = 40
    
    game_w = 1280
    game_h = 720
    current_screen = None
    mainmenuscreen = None
    gamescreen = None
    gameApplicationName = "EricisOmen"

    #variavéis da partida
    #portal_level_percent = 0

    

#varaivel que determina o estado princiapl de interação com o jogo
class SimulationMode(Enum):
    BUILDING = 1
    RUNNING = 0
    ENDING = 2
    LOSE = 3
