from PPlay.window import*
from PPlay.sprite import*
from tilemap import Tilemap
from tileset import Tileset
import pygame

tile_set_file = 'otsp_tiles_01.png'

gameApplicationName = "EricisOmen"
gameWindow = Window(800,800)

averageFrameTime = 0.0
lastFrameTime = 0.0

#cria e carrega o tilemap
tilemap = Tilemap(Tileset(tile_set_file, (32, 32)))

#loop principal
while(True):  
    #limpa a janela     
    gameWindow.set_background_color([128,128,128])

    #escreve a imagem do mapa na janela
    tilemap.draw_tilemap(gameWindow)

    #calcula o intervalo entre frames
    lastFrameTime = gameWindow.delta_time()
    averageFrameTime = (averageFrameTime + lastFrameTime)/2.0

    #atualiza a janela e rendeniza tudo
    gameWindow.set_title(gameApplicationName +  "  " + str(averageFrameTime*1000) + " ms") #ideal < 16ms = 60fps
    gameWindow.update()
