# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#modulo para gerenciar o funcionamento da construção "fenda dimensional"


from math import ceil
import math
from effects.effects import FloatingIconText
from effects.effectsmanager import EffectsManager
from match import Match
from settings import Settings, SimulationMode



def add_breach(u,v, manager):    
    info = manager.infos.get("breach1")
    if info != None:
        current_breach_building = manager.add(info, [u, v])       




def upgrade_breach(building, manager):  
    Match.breach_level += 1
    stage = Match.breach_level
    if stage >= 5:
        Match.simulation_mode = SimulationMode.ENDING
        Match.speed = 0.0

    name = "breach" + str(stage)
    info = manager.infos.get(name)
    if info != None:        
        u = building.posUV[0]
        v = building.posUV[1]
        manager.remove(building)
        manager.add(info, [u, v])
           
    Match.aether -= Settings.breach_required_aether[Match.breach_level-1]
    Match.beach_enabled = False


#principal loop da fenda. aqui é gerado o recurso aether e o recurso workers(trabalhadores)
def breach_update(building, manager):


    Match.aether += 10
        #EffectsManager.effects.append(FloatingIconText(building.x, building.y,"aether","+75"))

    if Match.aether > Match.max_aether:
        Match.aether = Match.max_aether
    if Match.aether < 0:
        Match.aether = 0

    if Match.aether >= Settings.breach_required_aether[Match.breach_level] and Match.beach_enabled:
        upgrade_breach(building, manager)
        

