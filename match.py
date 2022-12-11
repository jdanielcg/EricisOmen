# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para armazenar as informações pertinentes a partida, como
#recursos, estágios, etc

class Match:
    wood = 1000
    iron = 1000
    aether = 100

    max_stock = 100
    max_population = 5
    
    allies = []
    enemies = []




    #registra a velocidade da simuulaçãoo [para testes]
    speed = 1.0

    #registra quando o jogador decidir expandir a fenda
    beach_enabled = False

    #registra o estado atual da fenda
    breach_level = 1

    #registra a vitória ou derrota
    game_won = False
    game_lost = False

    def __init__(self) -> None:
        pass

