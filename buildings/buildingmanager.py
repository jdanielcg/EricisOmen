# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import pygame
from buildings.breach import add_breach, breach_update
from buildings.buildings import Building, BuildingInfo
from effects.effects import Fireball
from match import Match
from settings import Settings

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()

        self.infos = {}
        self.infos["dormitory"] = BuildingInfo("dormitory", (0, 12), (2,2), self._image, True, wood_cost= 50)
        self.infos["miningcamp"] = BuildingInfo("miningcamp", (0, 4), (1,2), self._image, True, wood_cost= 50)
        self.infos["lumbercamp"] = BuildingInfo("lumbercamp", (1, 4), (1,2), self._image, True, wood_cost= 50)
        self.infos["firetower"] = BuildingInfo("firetower", (20, 12), (1,2), self._image, True, self.tower_action, iron_cost=50, wood_cost=50)
        self.infos["breach1"] = BuildingInfo("breach1", (0, 23), (1,1), self._image, True, breach_update, 1, 2500, 15, on_destroy= self.set_gameover)
        self.infos["breach2"] = BuildingInfo("breach2", (0, 24), (3,3), self._image, True, breach_update, 1, 2500, 20, on_destroy= self.set_gameover)
        self.infos["breach3"] = BuildingInfo("breach3", (0, 27), (3,3), self._image, True, breach_update, 1, 2500, 35, on_destroy= self.set_gameover)
        self.infos["breach4"] = BuildingInfo("breach4", (0, 30), (3,3), self._image, True, breach_update, 1, 2500, 40, on_destroy= self.set_gameover)
        self.infos["breach5"] = BuildingInfo("breach5", (9, 23), (5,5), self._image, True, breach_update, 1, 2500, 40, on_destroy= self.set_gameover)
        self.infos["breach6"] = BuildingInfo("breach6", (3, 23), (5,5), self._image, True, breach_update, 1, 2500, 50, on_destroy= self.set_gameover)
        self.infos["breach7"] = BuildingInfo("breach7", (3, 28), (7,7), self._image, True, breach_update, 1, 2500, 60, on_destroy= self.set_gameover)
        self.infos["obelisk"] = BuildingInfo("obelisk", (10, 28), (1,2), self._image, True, None, 10, 2500, 10, aether_cost= 30)
        self.game = game

    def build_base(self):
        add_breach(Settings.breach_center[0], Settings.breach_center[1], self)

    def set_gameover(self, building):        
        Match.game_lost = True

    def tower_action(self, building, manager):
        #a ação da torre é disparar seu projetil
        closest_enemy = None
        closest_sqr_dist = 200000
        dist = 0
        
        #acha o inimigo mais proximo
        for enemy in self.game.world.creatures:
            if enemy.is_dead or not enemy.is_enemy : continue
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
                screen.blit(building.info.surf, building.posXY_render())
                #executa a ação da construçao, se houver
                building.timer += delta_time
                if building.action != None:
                    if building.timer > building.recharge_time:
                        building.timer = 0
                        building.action(building, self)
            else:                
                self.remove(building)

    def remove(self, building):
        #if building in self.game.world.building_list
        self.game.world.building_list.remove(building)

        if building.info.dominion_factor > 0:
            self.game.world.remove_dominion(building) 

        for cell_mask in building.info.mask:
            v = building.posUV[1] + cell_mask[1]
            u = building.posUV[0] + cell_mask[0]
            self.game.world.cells[v][u].walkable = True
            self.game.world.cells[v][u].buildable = True
            self.game.world.cells[v][u].building = None

        if building.on_destroy != None:
            building.on_destroy(building)

    def add(self, buildingInfo, posUV):        
        building = Building(posUV, buildingInfo)

        #remove connstrução se já houver
        for cell_mask in buildingInfo.mask:            
            v = posUV[1] + cell_mask[1]
            u = posUV[0] + cell_mask[0]
            if self.game.world.cells[v][u].building != None :
                self.remove(self.game.world.cells[v][u].building)


        #adiciona a contrução 
        self.game.world.building_list.append(building)  
        if building.info.dominion_factor > 0:
            self.game.world.add_dominion(building)  

        for cell_mask in buildingInfo.mask:            
            v = posUV[1] + cell_mask[1]
            u = posUV[0] + cell_mask[0]
            self.game.world.cells[v][u].walkable = buildingInfo.walkable
            self.game.world.cells[v][u].buildable = False
            self.game.world.cells[v][u].building = building
            