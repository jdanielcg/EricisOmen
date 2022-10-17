import pygame
from buildings.buildings import Building, BuildingInfo
from world import World

class BuildingManager:
    def __init__(self,game, filename):        
        self._image = pygame.image.load(filename)
        self._image.convert_alpha()
        
        self.infos = {}
        self.infos["dormitory"] = BuildingInfo("dormitory", (0, 12), (2,2), self._image)
        self.game = game        

    def update(self, delta_time):
        pass

    def add(self, buildingInfo, posUV):        
        building = Building(posUV, buildingInfo)
        self.game.world.building_list.append(building)        


    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for building in world.building_list:   
            #print("drawing building ", building.info.name, "in ", building.posXY())        
            screen.blit(building.info.surf, building.posXY())