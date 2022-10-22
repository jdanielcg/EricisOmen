# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#modulo usado para desenhar um minimpa na tela

from pygame import Surface

from PPlay.window import Window


class Minimap:
    def __init__(self, world):    
        #cria o mapa base
        self.world = world
        self.scale = 3
        self.base_surf = Surface((len(world.cells[0])*self.scale, len(world.cells)*self.scale))
        self.base_surf.fill((30,30,30)
)
        self.x = Window.screen.get_width() - self.base_surf.get_width() - 20
        self.y = Window.screen.get_height() - self.base_surf.get_height() - 20

        self.walkable_surf = Surface((self.scale,self.scale))
        self.walkable_surf.fill((50, 50, 50))

        self.wood_surf = Surface((self.scale,self.scale))
        self.wood_surf.fill((30, 20, 40))

        self.iron_surf = Surface((self.scale,self.scale))
        self.iron_surf.fill((40, 50, 10))

        self.enemy_surf = Surface((self.scale,self.scale))
        self.enemy_surf.fill((255, 0, 0))

        #self.domain_surf = Surface((self.scale,self.scale))
        #self.domain_surf.fill(180, 0, 255)

        for cell_line in world.cells:
            for cell in cell_line:
                if cell.walkable: self.base_surf.blit(self.walkable_surf, (cell.u*self.scale, cell.v*self.scale))
                if cell.resource == "wood": self.base_surf.blit(self.wood_surf, (cell.u*self.scale, cell.v*self.scale))
                if cell.resource == "iron": self.base_surf.blit(self.iron_surf, (cell.u*self.scale, cell.v*self.scale))      

        self.map_surf = Surface((len(world.cells[0])*self.scale, len(world.cells)*self.scale))

    def update(self):

        self.map_surf.blit(self.base_surf, (0,0))
        self.map_surf.set_alpha(200)
        for creature in self.world.creatures:
            self.map_surf.blit(self.enemy_surf, (creature.u*self.scale, creature.v*self.scale))

        Window.screen.blit(self.map_surf, (self.x,self.y))
