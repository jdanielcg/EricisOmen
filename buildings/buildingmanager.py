# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import pygame
from buildings.breach import add_breach, breach_update
from buildings.buildings import Building, BuildingInfo
from buildings.gathers import buildResourceList, gather
from effects.effects import Fireball, Stoneball, Iceball
from match import Match
from settings import Settings

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()
        
        
        self.infos = {}
        self.infos["dormitory"] = BuildingInfo("dormitory", (0, 12), (2,2), self._image, False, wood_cost= 24, setup_function= self.add_population_cap)
        self.infos["stockpile"] = BuildingInfo("stockpile", (3, 12), (2,2), self._image, False, wood_cost= 20, setup_function= self.add_resource_cap)

        self.infos["wall"] = BuildingInfo("wall", (0, 6), (1,1), self._image, False, wood_cost= 4, iron_cost= 4)
        self.infos["miningcamp"] = BuildingInfo("miningcamp", (0, 4), (1,2), self._image, False, gather, wood_cost= 8, setup_function = buildResourceList,gather_type="iron")
        self.infos["lumbercamp"] = BuildingInfo("lumbercamp", (1, 4), (1,2), self._image, False, gather, wood_cost= 8, setup_function = buildResourceList,gather_type="wood")
        self.infos["firetower"] = BuildingInfo("firetower", (20, 12), (1,2), self._image, False, self.tower_action,   iron_cost=20, wood_cost=25)
        self.infos["icetower"] = BuildingInfo("icetower", (18, 12), (1,2), self._image, False, self.tower_action,     iron_cost=30, wood_cost=50)
        self.infos["stonetower"] = BuildingInfo("stonetower", (19, 12), (1,2), self._image, False, self.tower_action, recharge_time= 1, iron_cost=10, wood_cost=10)

        self.infos["poisontrap"] = BuildingInfo("poisontrap", (19, 15), (1,1), self._image, True, None, iron_cost=5, wood_cost=20)
        self.infos["firetrap"] = BuildingInfo("firetrap", (18, 15), (1,1), self._image, True, None, iron_cost=15, wood_cost=10)

        self.infos["breach1"] = BuildingInfo("breach1", (0, 26), (7,7), self._image, False, breach_update, 1, 2500, 60, on_destroy= self.set_gameover)
        self.infos["breach2"] = BuildingInfo("breach2", (7, 26), (7,7), self._image, False, breach_update,  1, 2500, 70, on_destroy= self.set_gameover)
        self.infos["breach3"] = BuildingInfo("breach3", (14, 26), (7,7), self._image, False, breach_update,  1, 2500, 85, on_destroy= self.set_gameover)
        self.infos["breach4"] = BuildingInfo("breach4", (0, 33), (7,7), self._image, False, breach_update,  1, 2500, 95, on_destroy= self.set_gameover)
        self.infos["breach5"] = BuildingInfo("breach5", (7, 33), (7,7), self._image, False, breach_update,  1, 2500, 100, on_destroy= self.set_gameover)
        self.infos["obelisk"] = BuildingInfo("obelisk", (14, 33), (1,2), self._image, False, None, 10, 2500, 10, aether_cost= 30)
        self.game = game   

    def add_population_cap(self, building, world):
        Match.max_population += 5        

    def add_resource_cap(self,building,world):
        Match.max_stock += 100        

    def build_base(self):
        add_breach(Settings.breach_center[0] - 3, Settings.breach_center[1] - 3, self)

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

        effect = None
        if building.info.name == "firetower":
            effect = Fireball(building.x, building.y, closest_enemy)
        elif building.info.name == "icetower":
            effect = Iceball(building.x, building.y, closest_enemy)
        elif building.info.name == "stonetower":
            effect = Stoneball(building.x, building.y, closest_enemy)

        if effect != None:
            self.game.effects_manager.effects.append(effect)



    def update(self, game_window, world, delta_time):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for building in world.building_list:   
            #print("drawing building ", building.info.name, "in ", building.posXY())
            if building.integrity > 0:        
                screen.blit(building.info.get_surf(world.cells[building.v][building.u], world), building.posXY_render())
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
        building = Building(posUV, buildingInfo, self.game)

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
            