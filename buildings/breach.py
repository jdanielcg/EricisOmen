# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#modulo para gerenciar o funcionamento da construção "fenda dimensional"

from distutils.command.build import build
from math import ceil
import math
from effects.effects import FloatingIconText
from effects.effectsmanager import EffectsManager
from match import Match
from settings import Settings

def add_breach(u,v, manager):
    info = manager.infos.get("breach1")
    if info != None:
        manager.add(info, [u, v])  

worker_interval = 3
worker_timer = 0

aether_interval = 5
aether_timer = 0

def upgrade_breach(building, manager):
    Match.breach_level += 1
    stage = Match.breach_level
    if stage >= 7:
        Match.game_won = True

    name = "breach" + str(stage)
    info = manager.infos.get(name)
    if info != None:
        dx = round((info.size[0]-building.info.size[0])/2)
        dy = round((info.size[1]-building.info.size[1])/2)
        u = building.posUV[0] - dx
        v = building.posUV[1] - dy
        manager.remove(building)
        manager.add(info, [u, v])
        Match.game_lost = False   
    Match.aether -= Settings.breach_required_aether
    Match.beach_enabled = False


#principal loop da fenda. aqui é gerado o recurso aether e o recurso workers(trabalhadores)
def breach_update(building, manager):
    global worker_interval, worker_timer, aether_interval,aether_timer
    worker_timer += 1
    aether_timer +=1

    if worker_timer >= worker_interval and Match.soldiers <= Match.max_soldiers:
        worker_timer =0
        Match.soldiers += 5
        if Match.soldiers > Match.max_soldiers:
            Match.soldiers = Match.max_soldiers
        if Match.soldiers < 0:
            Match.soldiers = 0
        EffectsManager.effects.append(FloatingIconText(building.x, building.y,"worker","+5"))

    if aether_timer >= aether_interval and Match.aether <= Match.max_aether:
        aether_timer =0
        Match.aether += 75
        if Match.aether > Match.max_aether:
            Match.aether = Match.max_aether
        if Match.aether < 0:
            Match.aether = 0
        EffectsManager.effects.append(FloatingIconText(building.x, building.y,"aether","+75"))

    if Match.aether >= Settings.breach_required_aether and Match.beach_enabled:
        upgrade_breach(building, manager)
        

