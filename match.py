# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para armazenar as informações pertinentes a partida, como
#recursos, estágios, etc

class Match:
    wood = 250
    max_wood = 500
    iron = 150
    max_iron = 300
    workers = 0
    soldiers = 0
    max_soldiers = 50
    aether = 0
    max_aether = 100

    #registro da atualização de recursos:
    income = {"wood": 5,"iron": 4,"soldiers":0,"aether":0}
    outcome = {"wood": 0,"iron": 0,"soldiers":0,"aether":0}
    Balance = {
        "wood": income['wood'] - outcome['wood'],
        "iron": income['iron'] - outcome['iron'], 
        "soldiers": income['soldiers'] - outcome['soldiers'], 
        "aether": income['aether'] - outcome['aether']
        }

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

