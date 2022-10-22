# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para modificar o cursor padrão

import os
import pygame


def load_custom_cursor(file = "cursor16.png"):
    surf = pygame.image.load(os.path.join("assets",file))
    surf.convert_alpha()

    if surf != None:
        custom = pygame.cursors.Cursor((1,1), surf)
        pygame.mouse.set_cursor(custom)