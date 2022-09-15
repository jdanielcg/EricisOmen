import pygame


class Creaturemap:
    def __init__(self, creatureset):
        self.creatureset = creatureset
        self.tile_w, self.tile_h = creatureset.tile_size

    def draw(self, game_window, world):
        height = world.height
        width = world.width

        screen = game_window.get_screen()

        for creat in world.creatures:
            creat_image = self.creatureset.get_tile(creat.creature_code)           

            screen.blit(creat_image, (creat.x, creat.y))
