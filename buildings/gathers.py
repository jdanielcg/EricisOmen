

from audio.spacialsfx import SpacialSFX
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
                value = 10 if not Match.researched_saw else 20
                Match.wood += value
                EffectsManager.effects.append(FloatingIconText(building.x, building.y,"wood","+" + str(value)))
            elif building.info.gather_type == "iron":
                SpacialSFX("pick",building.x, building.y)
                value = 10 if not Match.researched_smelting else 20
                Match.iron += value
                EffectsManager.effects.append(FloatingIconText(building.x, building.y,"iron","+" + str(value)))

            break


def buildResourceList(building, world):
    building.resource_list = []

    #mascara dos dez ladrilhos adjacentes
    mask = [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1,1), (0, 2), (1,1), (-1,2), (1,2)]
    # X X X
    # X G X
    # X G X
    # X X X

    #verifica os ladrilhos adjacentes, se eles possuirem recursos, adicioona a lista
    for tile in mask:
        posU = building.u + tile[0]
        posV = building.v + tile[1]

        if world.cells[posV][posU].resource != None and world.cells[posV][posU].resource_amount > 0:
            building.resource_list.append(world.cells[posV][posU])