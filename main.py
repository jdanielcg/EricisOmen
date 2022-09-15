from email.mime import image
from venv import create
from PPlay.window import*
from PPlay.sprite import*
from tilemap import Tilemap
from tileset import Tileset
from world import World
from objectmap import Objectmap
from objectset import Objectset
from creaturemap import Creaturemap
from creatureset import Creatureset
import pygame


gameApplicationName = "EricisOmen"
gameWindow = Window(600,600)

averageFrameTime = 0.0
lastFrameTime = 0.0


#world: gerencia a representação lógica do mundo, é onde estão as células (cell)
world = World()

#tilemap: gerencia a representação visual do mapa fixo, apartir das cells
#uma cell representa um tile
tilemap = Tilemap(Tileset('otsp_tiles_01.png',(32, 32)))

#objectmap: gerencia a representação visual dos objetos
#várias cell/tile podem representar um objeto
objectmap = Objectmap(Objectset('otsp_town_01.png',(32, 32)))

#creaturemap: gerencia a representação visual das criaturas
creaturemap = Creaturemap(Creatureset('otsp_creatures_01.png', (32,32)))

#loop principal
while(True):  
    #limpa a janela     
    gameWindow.set_background_color([128,128,128])

    #atualiza a simulação
    world.update(gameWindow.delta_time())

    #escreve a imagem do mapa na janela
    tilemap.draw(gameWindow, world)

    #escreve a imagem dos objetos na janela
    objectmap.draw(gameWindow, world)

    #escreve a imagem das criaturas na tela
    creaturemap.draw(gameWindow, world)

    #calcula o intervalo entre frames
    lastFrameTime = gameWindow.delta_time()
    averageFrameTime = (averageFrameTime + lastFrameTime)/2.0

    #atualiza a janela e rendeniza tudo
    gameWindow.set_title(gameApplicationName +  " {:10.2f} ms ".format(averageFrameTime*1000)) #ideal < 16ms = 60fps
    gameWindow.update()
