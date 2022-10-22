# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#modulo para gerenciar o funcionamento da construção "fenda dimensional"


from math import ceil
from settings import Settings

def add_breach(u,v, manager):
    info = manager.infos.get("breach1")
    if info != None:
        manager.add(info, [u, v])  


def upgrade_breach(building, manager):
    Settings.breach_level += 1
    stage = Settings.breach_level
    if stage >= 7:
        Settings.game_won = True

    name = "breach" + str(stage)
    info = manager.infos.get(name)
    if info != None:
        dx = round((info.size[0]-building.info.size[0])/2)
        dy = round((info.size[1]-building.info.size[1])/2)
        u = building.posUV[0] - dx
        v = building.posUV[1] - dy
        manager.remove(building)
        manager.add(info, [u, v])    

def breach_update(building, manager):
    upgrade_breach(building, manager)

