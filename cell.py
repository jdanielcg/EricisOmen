from random import randint

class Cell:
    def __init__(self, location, tile_code = 0, image_size = (32, 32)):
        self.image_size = image_size
        self.location = location
        self.tile_code = tile_code
        self.object_code = 0
        self.object_code = self.random_object()

    def random_object(self):
        #gera um object code generico para testes
        return 16 if  randint(0, 100) > 85 else 28 #28 = nada