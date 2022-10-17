from random import randint

class Cell:
    def __init__(self, location, tile_code = 0, image_size = (32, 32)):
        self.image_size = image_size
        self.location = location
        self.tile_code = tile_code            
        self.building_code = 999