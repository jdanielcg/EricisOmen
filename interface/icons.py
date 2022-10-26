# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para carregar e disponiblizar icones

import os
import pygame

class Icon:
    def __init__(self, name, atlas16, atlas32, u, v):
        self.name = name
        self.surf16 = pygame.Surface((u*16, v*16), pygame.SRCALPHA)
        self.surf16.fill((0,0,0,0))
        self.surf16.blit(atlas16,(0,0),(u*16, v*16, 16,16), special_flags = pygame.BLEND_RGBA_ADD)

        self.surf32 = pygame.Surface((u*32, v*32), pygame.SRCALPHA)
        self.surf32.fill((0,0,0,0))
        self.surf32.blit(atlas32,(0,0),(u*32, v*32, 32,32), special_flags = pygame.BLEND_RGBA_ADD)

#inicializa a fonte
font = pygame.font.SysFont("bahnschrift semibold", 20, False, False)
font_large = pygame.font.SysFont("bahnschrift semibold", 40, False, False)
icondic = None
error_icon = None

def build_dic():
    global icondic, error_icon
    #carrega as imagens com os icones
    sprites16 = pygame.image.load(os.path.join("assets","icons16.png"))
    sprites32 = pygame.image.load(os.path.join("assets","icons32.png"))
    sprites16.convert_alpha()
    sprites32.convert_alpha()
    error_icon = Icon("error", sprites16, sprites32, 13, 8)



    icondic = { "wood":     Icon("wood", sprites16, sprites32, 13, 20),
                "iron":     Icon("wood", sprites16, sprites32, 13, 21),
                "worker":   Icon("worker", sprites16, sprites32, 7, 11),
                "soldier":  Icon("soldier", sprites16, sprites32, 12, 11),
                "aether":   Icon("aether", sprites16, sprites32, 10, 9),                
                "book":   Icon("book", sprites16, sprites32, 2, 2),     
                "error":    error_icon,
    }

def get_icon(name):
    if icondic == None: build_dic()
    return icondic.get(name, error_icon)

def text_icon(icon, text, cor = (255,240,255), large = False) -> pygame.Surface:
    s = 16 if not large else 32   
    icon = get_icon(icon).surf16 if not large else get_icon(icon).surf32
    
    #cria a surface com o texto escrito
    textsurf = font.render(text, True, cor) if not large else font_large.render(text, True, cor)

    #cria a surface para colocar o texto e o icone
    font_rect = textsurf.get_rect()       
    back_surf = pygame.Surface([font_rect.width + s, font_rect.height+s], pygame.SRCALPHA)
    back_surf.fill((0,0,0,0))

    #escreve o texto e o icone    
    back_surf.blit(icon,(0,0), special_flags = pygame.BLEND_RGBA_ADD )
    back_surf.blit(textsurf, (s,0))
    return back_surf

def make_cost_text(wood_cost, iron_cost, aether_cost) -> pygame.Surface:
    y = 10
    x = 10
    surf = pygame.Surface((100,100), pygame.SRCALPHA)
    surf.fill((0,0,0,0))

    if wood_cost > 0:
        surf.blit(text_icon("wood", str(wood_cost)), (x, y), special_flags = pygame.BLEND_RGBA_ADD )
        y += 20
    if iron_cost > 0:
        surf.blit(text_icon("iron", str(iron_cost)), (x, y), special_flags = pygame.BLEND_RGBA_ADD )
        y += 20
    if aether_cost > 0:
        surf.blit(text_icon("aether", str(aether_cost)), (x, y), special_flags = pygame.BLEND_RGBA_ADD )
        y += 20
    return surf




