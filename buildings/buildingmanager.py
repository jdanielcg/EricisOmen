import pygame
from buildings.buildings import Building, BuildingInfo
from world import World

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()
        
        self.infos = {}
        self.infos["dormitory"] = BuildingInfo("dormitory", (0, 12), (2,2), self._image, True)
        self.game = game        

    def update(self, delta_time):
        pass

    def add(self, buildingInfo, posUV):        
        building = Building(posUV, buildingInfo)
        self.game.world.building_list.append(building)  
        for cell_mask in buildingInfo.mask:
            v = posUV[1] + cell_mask[1]
            u = posUV[0] + cell_mask[0]
            self.game.world.cells[v][u].walkable = buildingInfo.walkable
            self.game.world.cells[v][u].buildable = False


    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for building in world.building_list:   
            #print("drawing building ", building.info.name, "in ", building.posXY())        
            screen.blit(building.info.surf, building.posXY())