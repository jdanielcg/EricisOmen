# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: RAMON SANTOS         ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import pygame

from settings import Settings

from match import Match

def music_level(interface):
    interface.window.draw_text("Audio", 64, 225, size=18, bold=True, color=(224, 224, 220))
    interface.botao_sound_direita.draw()
    interface.botao_sound_esquerda.draw()
    if interface.volume_level == 1:
        Settings.audio_volume = 0.0
    else:
        Settings.audio_volume = interface.volume_level/10.0
    if interface.clickjogo.is_over_object(interface.botao_sound_direita) and interface.clickjogo.is_button_pressed(True) and interface.volume_level <= 9:
        interface.volume_level +=1
    if interface.clickjogo.is_over_object(interface.botao_sound_esquerda) and interface.clickjogo.is_button_pressed(True) and interface.volume_level >= 2:
        interface.volume_level -=1
    if interface.volume_level == 1:
        interface.volume_level_1.draw()
    if interface.volume_level == 2:
        interface.volume_level_2.draw()
    if interface.volume_level == 3:
        interface.volume_level_3.draw()
    if interface.volume_level == 4:
        interface.volume_level_4.draw()
    if interface.volume_level == 5:
        interface.volume_level_5.draw()
    if interface.volume_level == 6:
        interface.volume_level_6.draw()
    if interface.volume_level == 7:
        interface.volume_level_7.draw()
    if interface.volume_level == 8:
        interface.volume_level_8.draw()
    if interface.volume_level == 9:
        interface.volume_level_9.draw()
    if interface.volume_level == 10:
        interface.volume_level_10.draw()

def fullscreen(interface):
    interface.window.draw_text("Fullscreen", 44, 329, size=18, bold=True, color=(224, 224, 220))
    if interface.p_fullscreen == False:
        interface.checkbox_fullscreen_false.draw()
        interface.checkbox_fullscreen.set_position(56, 359.5)
        interface.checkbox_fullscreen.draw()
        if interface.clickjogo.is_over_object(interface.checkbox_fullscreen) and interface.clickjogo.is_button_pressed(True):
            pygame.display.toggle_fullscreen()
            interface.p_fullscreen = True
    if interface.p_fullscreen == True:
        interface.checkbox_fullscreen_true.draw()
        interface.checkbox_fullscreen.set_position(104, 359.5)
        interface.checkbox_fullscreen.draw()
        if interface.clickjogo.is_over_object(interface.checkbox_fullscreen) and interface.clickjogo.is_button_pressed(True):
            pygame.display.toggle_fullscreen()
            interface.p_fullscreen = False

def exit(interface):
    interface.botao_jogo_restart.draw()
    interface.botao_jogo_quit.draw()
    if interface.clickjogo.is_over_object(interface.botao_jogo_restart) and interface.clickjogo.is_button_pressed(True):
        from screens.game import Game
        Settings.gamescreen = Game(interface.window)
        Settings.current_screen = Settings.gamescreen
    if interface.clickjogo.is_over_object(interface.botao_jogo_quit) and interface.clickjogo.is_button_pressed(True):
        interface.p_quit = True
    if interface.p_quit == True:
        interface.barra_botao_quit.draw()
        interface.botao_barra_quit_quit.draw()
        interface.botao_barra_quit_close.draw()
        interface.window.draw_text("Are you sure?", 206, 560, size=18, bold=True, color=(224, 224, 220))
        if interface.clickjogo.is_over_object(interface.botao_barra_quit_quit) and interface.clickjogo.is_button_pressed(True):
            from screens.game import Game
            Settings.current_screen = Settings.mainmenuscreen
            Settings.gamescreen = Game(interface.window)
        if interface.clickjogo.is_over_object(interface.botao_barra_quit_close) and interface.clickjogo.is_button_pressed(True):
            interface.p_quit = False