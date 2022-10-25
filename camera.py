# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para controlar os parametros de visualização do mundo

from logging import root
from math import ceil
from PPlay.window import Window
from settings import Settings


class Camera:
    #qual ladrilho está sendo desenhado no canto superior 
    # esquerdo da tela
    rootU = 0
    rootV = 0
    
    #numero de ladrilhos que devem ser desenhados    
    def nU() -> int:
        return ceil(Window.screen.get_width()/Settings.tilesize)    
    def nV() -> int:
        return ceil(Window.screen.get_height()/Settings.tilesize)

    #deltas usados na rendenização de objetos que estão com
    #coordenadas reais
    dx = 0
    dy = 0

    def set_view_from_center(u,v):
        Camera.rootU = round(u - Camera.nU()/2)
        Camera.rootV = round(v - Camera.nV()/2)

        #corrige u
        if Camera.rootU < 0 :
            Camera.rootU = 0
        elif Camera.rootU > (Settings.tile_number_u - Camera.nU()):
            Camera.rootU = Settings.tile_number_u - Camera.nU()

        #corrige v
        if Camera.rootV < 0 :
            Camera.rootV = 0
        elif Camera.rootV > (Settings.tile_number_v - Camera.nV()):
            Camera.rootV = Settings.tile_number_v - Camera.nV()

        Camera.dx = Camera.rootU*Settings.tilesize
        Camera.dy = Camera.rootV*Settings.tilesize



    def __init__(self) -> None:
        pass