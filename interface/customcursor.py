# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


#modulo para modificar o cursor padrão

import pygame


def load_custom_cursor(file = "cursor.png"):
    surf = pygame.image.load("assets\\" + file)
    surf.convert_alpha()

    if surf != None:
        custom = pygame.cursors.Cursor((1,1), surf)
        pygame.mouse.set_cursor(custom)