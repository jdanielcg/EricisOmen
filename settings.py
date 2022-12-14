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
    breach_required_aether = [100, 200, 300, 500, 600, 700]
    breach_center = (40,41)
    enemy_spawns = [(9,8),(9,9),(9,10), (46,4),(45,4),(44,4),(0, 50),(0,51),(0,52),(56,59), (55,59)]
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
