

from effects.effects import FloatingIconText
from effects.effectsmanager import EffectsManager
from effects.effects import SmokeDamage
from match import Match


def gather(building, manager):
    for resourceTile in building.resource_list:
        #adquire recurso e elimina o mesmo do mapa se esgotado
        if resourceTile.resource == building.info.gather_type and resourceTile.resource_amount > 0:
            resourceTile.resource_amount -= 10

            EffectsManager.effects.append(SmokeDamage(resourceTile.x, resourceTile.y))

            if building.info.gather_type == "wood":
                Match.wood += 10
                EffectsManager.effects.append(FloatingIconText(building.x, building.y,"wood","+10"))
            elif building.info.gather_type == "iron":
                Match.iron += 10
                EffectsManager.effects.append(FloatingIconText(building.x, building.y,"iron","+10"))

            break


def buildResourceList(building, world):
    building.resource_list = []

    #mascara dos oito ladrilhos adjacentes
    mask = [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1,1), (0, 1), (1,1)]

    #verifica os ladrilhos adjacentes, se eles possuirem recursos, adicioona a lista
    for tile in mask:
        posU = building.u + tile[0]
        posV = building.v + tile[1]

        if world.cells[posV][posU].resource != None and world.cells[posV][posU].resource_amount > 0:
            building.resource_list.append(world.cells[posV][posU])