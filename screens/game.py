
from PPlay.sprite import*
from globals import Globals
from interface.framerate import Framerate
from interface.gameinterface import Gameinterface
from mapa.tilemap import Tilemap
from mapa.tileset import Tileset
from movables.movablesmanager import MovablesManager
from world import World
from buildings.objectmap import Objectmap
from buildings.objectset import Objectset
import pygame

class Game: 
    def __init__(self, g, gameWindow):
        self.g = g      
        self.gameWindow = gameWindow
        self.framerate = Framerate()

        #world: gerencia a representação lógica do mundo, é onde estão as células (cell)
        self.world = World() 

        #tilemap: gerencia a representação visual do mapa fixo, apartir das cells
        #uma cell representa um tile
        self.tilemap = Tilemap(Tileset("edit_terrain.png",(32, 32)))    

        #objectmap: gerencia a representação visual dos objetos
        #várias cell/tile podem representar um objeto
        self.objectmap = Objectmap(Objectset("edit_terrain.png",(32, 32))) 

        #movablesmanager: gerencia os personagens
        self.movables_manager = MovablesManager(gameWindow,self.world)    

        #interface do jogo
        self.gameinterface = Gameinterface(g,gameWindow)

    #loop principal
    def update(self, delta_time):  
        #limpa a janela     
        self.gameWindow.set_background_color([128,128,128])     

        #escreve a imagem do mapa na janela
        self.tilemap.draw(self.gameWindow, self.world) 

        #escreve a imagem dos objetos na janela
        self.objectmap.draw(self.gameWindow, self.world)   

        #escreve a imagem das criaturas na tela
        self.movables_manager.update(self.world, delta_time)

        #escreve a interface na tela
        self.gameinterface.update(delta_time)

        #atualiza a janela e rendeniza tudo
        self.gameWindow.set_title(self.g.gameApplicationName + self.framerate.get_text(delta_time))
        #ideal < 16ms = 60fps

        