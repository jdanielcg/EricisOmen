# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import pygame
from audio.spacialsfx import SpacialSFX
from buildings.breach import add_breach, breach_update
from buildings.buildings import Building, BuildingInfo
from buildings.gathers import buildResourceList, gather
from effects.effects import Fireball, Stoneball, Iceball
from match import Match
from settings import Settings, SimulationMode

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()

        self.infos = {}
        self.infos["demolition"] = BuildingInfo("dormitory", (0, 0), (1,1), self._image, False)
        self.infos["dormitory"] = BuildingInfo("dormitory", (12, 0), (2,2), self._image, False, wood_cost= 24, setup_function= self.add_population_cap)
        self.infos["stockpile"] = BuildingInfo("stockpile", (15, 0), (2,2), self._image, False, wood_cost= 20, setup_function= self.add_resource_cap, on_destroy=self.remove_resource_cap)

        self.infos["wall"] = BuildingInfo("wall", (0, 6), (1,1), self._image, False, wood_cost= 4, iron_cost= 4)
        self.infos["miningcamp"] = BuildingInfo("miningcamp", (0, 4), (1,2), self._image, False, gather, wood_cost= 8, setup_function = buildResourceList,gather_type="iron")
        self.infos["lumbercamp"] = BuildingInfo("lumbercamp", (1, 4), (1,2), self._image, False, gather, wood_cost= 8, setup_function = buildResourceList,gather_type="wood")
        self.infos["firetower"] = BuildingInfo("firetower", (14, 2), (1,2), self._image, False, self.tower_action,   iron_cost=20, wood_cost=25)
        self.infos["icetower"] = BuildingInfo("icetower", (12, 2), (1,2), self._image, False, self.tower_action,     iron_cost=30, wood_cost=50)
        self.infos["stonetower"] = BuildingInfo("stonetower", (13, 2), (1,2), self._image, False, self.tower_action, recharge_time= 1, iron_cost=10, wood_cost=10)

        self.infos["poisontrap"] = BuildingInfo("poisontrap", (13, 5), (1,1), self._image, True, None, iron_cost=5, wood_cost=20)
        self.infos["firetrap"] = BuildingInfo("firetrap", (12, 5), (1,1), self._image, True, None, iron_cost=15, wood_cost=10)

        self.infos["breach1"] = BuildingInfo("breach1", (0, 11), (7,7), self._image, False, breach_update, 1, 2500, 60, on_destroy= self.set_gameover, can_demolish= False)
        self.infos["breach2"] = BuildingInfo("breach2", (7, 11), (7,7), self._image, False, breach_update,  1, 2500, 70, on_destroy= self.set_gameover,can_demolish= False)
        self.infos["breach3"] = BuildingInfo("breach3", (14, 11), (7,7), self._image, False, breach_update,  1, 2500, 85, on_destroy= self.set_gameover,can_demolish= False)
        self.infos["breach4"] = BuildingInfo("breach4", (0, 18), (7,7), self._image, False, breach_update,  1, 2500, 95, on_destroy= self.set_gameover,can_demolish= False)
        self.infos["breach5"] = BuildingInfo("breach5", (7, 18), (7,7), self._image, False, breach_update,  1, 2500, 100, on_destroy= self.set_gameover,can_demolish= False)
        self.infos["obelisk"] = BuildingInfo("obelisk", (14, 18), (1,2), self._image, False, None, 10, 2500, 10, aether_cost= 30, setup_function= self.add_aeter_cap, on_destroy=self.remove_aeter_cap)
        self.game = game   

    def add_population_cap(self, building, world):
        Match.max_population += 5 
        if Match.max_population > 20:
            Match.max_population = 20       

    def add_resource_cap(self,building,world):
        Match.max_stock += 100     

    def add_aeter_cap(self,building,world):
        Match.max_aether += 100    

    def remove_aeter_cap(self,building):
        Match.max_aether -= 100
        if Match.max_aether < 200:
            Match.max_aether = 200

    def remove_resource_cap(self,building):
        Match.max_stock -= 100
        if Match.max_stock < 100:
            Match.max_stock = 100

    def build_base(self):
        add_breach(Settings.breach_center[0] - 3, Settings.breach_center[1] - 3, self)

    def set_gameover(self, building):    
        if not Match.beach_enabled:
            Match.simulation_mode = SimulationMode.LOSE
            Match.speed = 0.0

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

        SpacialSFX("towershot",building.x, building.y) 

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
        if building in self.game.world.building_list:
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
        else:
            SpacialSFX("demolish",building.x, building.y)

    def add(self, buildingInfo, posUV):        
        building = Building(posUV, buildingInfo, self.game)

        #remove connstrução e aliados se já houver
        for cell_mask in buildingInfo.mask:            
            v = posUV[1] + cell_mask[1]
            u = posUV[0] + cell_mask[0]
            if self.game.world.cells[v][u].building != None :
                self.remove(self.game.world.cells[v][u].building)

            creature = self.game.world.cells[v][u].creature
            if  creature!= None:
                if (not creature.is_enemy) and creature in self.game.world.creatures:
                    self.game.world.creatures.remove(creature)
                if (not creature.is_enemy) and creature in Match.allies:
                    Match.allies.remove(creature)



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

        return building
            