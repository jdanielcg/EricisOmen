# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

#modulo que cuida de desenhar e gerenciar a parte da interface
#que representa o progresso da fenda


from pygame import Rect, Surface
import pygame
from PPlay.window import Window
from interface.textbutton import TextButton
from match import Match
from settings import Settings

surf : Surface = None
surf_fill : Surface = None
surf_pre_fill : Surface = None
screen : Surface = None
font_surface :Surface = None

base_pos = None
fill_pos = None
fill_area = None
pre_fill_area = None

#controla a inercia do preenchimento da barra
smooth_fill_factor = 0
old_fill_factor = 0
fill_speed = 0.10
is_filling = False
fill_delay = 5
fill_timer = 0

#fator de preenchimento da barra
def fill_factor():
    return Match.aether/(Settings.breach_required_aether*Match.breach_level)

clicked = False
button_rect : Rect = None


def setup_breachmeter():
    global screen, surf, surf_fill, base_pos, fill_pos, fill_area, surf_pre_fill, pre_fill_area, font_surface
    global button_rect
    screen = Window.screen

    x = 250
    h = 50
    xf = x + 10
    hf = h -20
    y = 60
    yf = y -10
    

    surf = Surface((screen.get_width()-2*x, h))
    surf.fill((0,0,0))

    surf_fill = Surface((screen.get_width()-2*xf, hf))
    surf_fill.fill((200,0,255))

    surf_pre_fill = Surface((screen.get_width()-2*xf, hf))
    surf_pre_fill.fill((200,200,200))

    base_pos = [x, screen.get_height() - y]
    fill_pos = [xf, screen.get_height() - yf]
    fill_area = [0, 0, 1, surf_fill.get_height()]
    pre_fill_area = [0,0, 1, surf_fill.get_height()]

    button_rect = Rect(x, screen.get_height() - y, surf.get_width(), surf.get_height())

    font = TextButton.font = pygame.font.SysFont("bahnschrift semibold", 40, False, False)

    #cria a surface com o texto escrito
    font_surface = font.render("BREACH", True, (255,255,255))

    #button = TextButton(upgrade_breach, "BREACH")


def update_breachmeter(delta_time):
    global screen, surf, surf_fill, base_pos, fill_pos, fill_area, pre_fill_area, smooth_fill_factor
    global surf_pre_fill, is_filling,fill_timer,fill_delay, fill_speed, old_fill_factor, font_surface
    global clicked, button_rect


    smooth_fill_factor += (fill_factor() - smooth_fill_factor)*5*delta_time

    #suave
    pre_fill_area[2] = smooth_fill_factor*surf_fill.get_width()

    #instantaneo
    #pre_fill_area[2] = fill_factor()*surf_fill.get_width()

    if not is_filling:
        fill_timer += delta_time
        if (abs(old_fill_factor - fill_factor()) > 0.2) or (fill_timer > fill_delay) or fill_factor() >= 1:
            fill_timer = 0
            is_filling = True
    else:  
        old_fill_factor += fill_speed*delta_time
        fill_area[2] = surf_fill.get_width()*old_fill_factor
        if old_fill_factor > fill_factor():
            old_fill_factor = fill_factor()
            is_filling = False

    screen.blit(surf, base_pos)
    screen.blit(surf_pre_fill, fill_pos, pre_fill_area)
    screen.blit(surf_fill, fill_pos, fill_area)

    if fill_factor() >= 1:
        screen.blit(font_surface, [base_pos[0] + round(surf.get_width()/2 - font_surface.get_width()/2), fill_pos[1] + 5])                
        if Window.get_mouse().is_over_object(button_rect):                            
            if Window.get_mouse().is_button_pressed(True):
                if not clicked:
                   clicked = True            
            elif clicked:
                upgrade_breach()
                clicked = False
        else:                     
            clicked = False

def upgrade_breach():
    global fill_timer, is_filling, old_fill_factor, smooth_fill_factor
    smooth_fill_factor = 0
    fill_timer = 0
    is_filling = False
    old_fill_factor = 0
    Match.beach_enabled = True