# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para armazenar as informações pertinentes a partida, como
#recursos, estágios, etc
from settings import SimulationMode

class Match:


        
    wood = 0
    iron = 0
    aether = 0
    max_aether = 0

    max_stock = 0
    max_population = 0
    
    allies = []
    enemies = []

    #registra a velocidade da simuulação
    speed = 1.0

    #registra quando o jogador decidir expandir a fenda
    beach_enabled = False

    #registra o estado atual da fenda
    breach_level = 1

    simulation_mode = SimulationMode.RUNNING

    game = None


    def Setup(game):
        Match.game = game
        Match.wood = 300
        Match.iron = 300
        Match.aether = 0
        Match.max_aether = 1000

        Match.simulation_mode = SimulationMode.RUNNING
    
        Match.max_stock = 500
        Match.max_population = 5
        
        Match.allies = []
        Match.enemies = []      
        Match.speed = 1.0    
        Match.beach_enabled = False    
        Match.breach_level = 1   
        Match.game_won = False
        Match.game_lost = False


    def __init__(self) -> None:
        pass

