# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import floor


from camera import Camera
from interface.icons import make_cost_text
from match import Match
from settings import SimulationMode
from settings import Settings

class BuildingMode:

    def __init__(self, game):
        self.game = game
        self.screen = game.gameWindow.get_screen()
        self.mouse = game.gameWindow.get_mouse()
        self.selected = None
        self.left_clicked = False
        self.cost_text = None

    def start(self, name):
        self.selected = self.game.buildings_manager.infos[name]
        self.left_clicked = False
        self.cost_text = make_cost_text(self.selected.wood_cost,self.selected.iron_cost,self.selected.aether_cost)

    def update(self, delta_time):
        if self.selected != None:
            pos = self.mouse.get_position()
            u = floor((pos[0] + Camera.dx)/Settings.tilesize)
            v = floor((pos[1] + Camera.dy)/Settings.tilesize)



            possible = True
            for cell_mask in self.selected.mask:
                vc = v + cell_mask[1]
                uc = u + cell_mask[0]
                if not self.game.world.cells[vc][uc].walkable : possible = False  
                if self.game.world.cells[vc][uc].is_dominion_border: possible = False
                #verifica se esta sobre um tile dominado:
                if self.game.world.cells[vc][uc].dominion_level < Settings.dominion_threshold: possible = False
            #Verifica se possui recursos o suficiente
            if self.selected.wood_cost > Match.wood: possible = False
            if self.selected.iron_cost > Match.iron: possible = False
            if self.selected.aether_cost > Match.aether: possible = False




            x = floor((pos[0])/Settings.tilesize)*Settings.tilesize
            y = floor((pos[1])/Settings.tilesize)*Settings.tilesize

            #desenha o contorno da construção e seu custo

            self.screen.blit(self.selected.silhouette if possible else self.selected.silhouette_red, (x,y))
            if self.cost_text != None:
                self.screen.blit(self.cost_text,(x-60,y))

            if possible:
                #verifica o click para construcao
                if self.mouse.is_button_pressed(self.mouse.BUTTON_LEFT):
                    if not self.left_clicked:                    
                        self.left_clicked = True
                #a ação ocorre ao soltar o botão, evitando erros
                elif self.left_clicked:                
                    self.build((u,v))
                    self.left_clicked = False

                    
            #verifica o click para cancelar
            if self.mouse.is_button_pressed(self.mouse.BUTTON_RIGHT):
                self.game.simulation_mode = SimulationMode.RUNNING

    def build(self, posUV):        
        self.game.buildings_manager.add(self.selected, posUV)        
        Match.wood -= self.selected.wood_cost 
        Match.iron -= self.selected.iron_cost
        Match.aether -= self.selected.aether_cost 



