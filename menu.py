from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *

#musica do menu
p_musica = True
mixer.init()
mixer.music.load('assets\menu.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#dimensões
janela_largura = 1280
janela_altura = 720

#criando a janela
janela = Window(janela_largura, janela_altura)
janela.set_title("Omen of Ericis")

#pegando a entrada do usuário
teclado = janela.get_keyboard()
click = janela.get_mouse()

#fundo do menu
background = Sprite("assets\dragao.webp")

#titulo
titulo = Sprite("assets\Titulo.png")
titulo.set_position(1280/2 - 280, 50)

#janela help
janelahelp = Sprite("assets\submenu.png")
janelahelp.set_position(1280/2 - 460, 65)
p_help = True

#janela settings
janelasettings = Sprite("assets\submenu.png")
janelasettings.set_position(1280/2 - 460, 65)
p_settings = True

#botao play
play = Sprite("assets\Buttons\play.png")
play.set_position(1280/2 - 120, 250)

#botao settings
settings = Sprite("assets\Buttons\settings.png")
settings.set_position(1280/2 - 120, 350)

#botao exit
exit = Sprite("assets\Buttons\exit.png")
exit.set_position(1280/2 - 120 , 450)

#botao help
help = Sprite("assets\Buttons\help.png")
help.set_position(1260 - 70 , 630)

#botao music
music = Sprite("assets\Buttons\music.png")
music.set_position(1260 - 150, 630)

#botao quit
quit = Sprite("assets\Buttons\quit.png")
quit.set_position(1280/2 - 120, 570)

#creditos
creditos = Sprite("assets\creditos.png")
creditos.set_position(1280/2 - 280 , 550)

while True:
    #desenhar tudo
    background.draw()
    titulo.draw()
    play.draw()
    settings.draw()
    music.draw()
    exit.draw()
    help.draw()
    creditos.draw()

    #botao play
    if click.is_over_object(play) and click.is_button_pressed(True):
        janela.draw_text("aqui é pro jogo iniciar", janela_largura/2-200, 10, size=40, bold=True)

    #botao settings
    if click.is_over_object(settings) and click.is_button_pressed(True):
        if p_settings == True:
            p_settings = False

            #janela do settings
            while True:
                janelasettings.draw()
                quit.draw()
                
                janela.draw_text("Settings", janela_largura/2 - 127, 90, size=60, bold=True, color=(224, 224, 222))
                janela.update()
                if click.is_over_object(quit) and click.is_button_pressed(True):
                    break
        else:
            p_settings = True

    #botao exit
    if click.is_over_object(exit) and click.is_button_pressed(True):
        janela.close()

    #botao musica
    if click.is_over_object(music) and click.is_button_pressed(True):
        if p_musica == True:
            mixer.music.pause()
            p_musica = False
        else:
            mixer.music.unpause()
            p_musica = True
    
    #botao help
    if click.is_over_object(help) and click.is_button_pressed(True):
        if p_help == True:
            p_help = False

            #janela do help
            while True:
                janelahelp.draw()
                
                quit.draw()
                
                janela.draw_text("About", janela_largura/2 - 100, 90, size=60, bold=True, color=(224, 224, 222))
                janela.update()
                if click.is_over_object(quit) and click.is_button_pressed(True):
                    break
        else:
            p_help = True

        
        

    janela.update()