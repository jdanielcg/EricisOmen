import pygame

class Objectmap:
    def __init__(self, objectset):
        self.objectset = objectset
        self.tile_w, self.tile_h = objectset.tile_size

    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for y in range(height):
            for x in range(width):
                object = self.objectset.get_tile(world.cells[y][x].building_code)   
                #pula a rendenização de o objeto for vazio
                if world.cells[y][x].building_code +1 == 0:
                    continue

                screen.blit(object, (x*self.tile_w, y*self.tile_h))