from distutils.command.build import build
import pygame
from buildings.buildings import Building, BuildingInfo
from effects.effects import Fireball

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()
        
        self.infos = {}
        self.infos["dormitory"] = BuildingInfo("dormitory", (0, 12), (2,2), self._image, True)
        self.infos["firetower"] = BuildingInfo("firetower", (20, 12), (1,2), self._image, True, self.tower_action)
        self.game = game        


    def tower_action(self, building):
        #a ação da torre é disparar seu projetil
        closest_enemy = None
        closest_sqr_dist = 10000000000
        dist = 0
        
        #acha o inimigo mais proximo
        for enemy in self.game.world.creatures:
            if enemy.is_dead : continue
            dist = (enemy.x - building.x)**2 + (enemy.y - building.y)**2
            if dist < closest_sqr_dist:
                closest_sqr_dist = dist
                closest_enemy = enemy

        if closest_enemy == None: return

        fireball = Fireball(building.x, building.y, closest_enemy)
        self.game.effects_manager.effects.append(fireball)



    def update(self, game_window, world, delta_time):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for building in world.building_list:   
            #print("drawing building ", building.info.name, "in ", building.posXY())
            if building.integrity > 0:        
                screen.blit(building.info.surf, building.posXY())
                #executa a ação da construçao, se houver
                building.timer += delta_time
                if building.action != None:
                    if building.timer > building.recharge_time:
                        building.timer = 0
                        building.action(building)
            else:
                world.building_list.remove(building)
                self.remove(building)

    def remove(self, building):
            for cell_mask in building.info.mask:
                v = building.posUV[1] + cell_mask[1]
                u = building.posUV[0] + cell_mask[0]
                self.game.world.cells[v][u].walkable = True
                self.game.world.cells[v][u].buildable = True
                self.game.world.cells[v][u].building = None

    def add(self, buildingInfo, posUV):        
        building = Building(posUV, buildingInfo)
        self.game.world.building_list.append(building)  
        for cell_mask in buildingInfo.mask:
            v = posUV[1] + cell_mask[1]
            u = posUV[0] + cell_mask[0]
            self.game.world.cells[v][u].walkable = buildingInfo.walkable
            self.game.world.cells[v][u].buildable = False
            self.game.world.cells[v][u].building = building
            