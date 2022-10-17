def informations(nome,janelajogo):
    if nome == 'Pack Tactics':
        janelajogo.draw_text("Pack Tactics",  620, 170, size=20, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("50 Food, 200 Wood, 100 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("By learning how to corner their preys and waiting for the right moment to strike,",  454, 275, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Kobolds are now able to take down larger preys on Hunting Camps. Increases",  454, 290, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Food production rate.",  454, 305, size=12, bold=True, color=(0, 0, 0))         
    if nome == 'Double Saw':
        janelajogo.draw_text("Double Saw",  620, 170, size=20, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("100 Food, 50 Wood, 200 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Cooperative methods of wood cutting turns feeble kobolds on capable lumber",  454, 275, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("jackers. Increases Wood production rate on Woodcutter's camp.",  454, 290, size=12, bold=True, color=(0, 0, 0))
    if nome == 'Hardened Picks':
        janelajogo.draw_text("Hardened Picks",  610, 170, size=20, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("200 Food, 200 Wood, 50 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Well-thought crafting techniques creates stronger tools with higher productivity.",  454, 275, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Increases Stone production rate on quarries.",  454, 290, size=12, bold=True, color=(0, 0, 0))
    if nome == 'Eficient Smelting':
        janelajogo.draw_text("Eficient Smelting",  610, 170, size=20, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("200 Food, 200 Wood, 100 Stone, 25 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("Understanding that gold melts faster and shapes easier than iron, Kobolds now",  454, 275, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("handle it more carefully than other metals. Increase Gold production rate on",  454, 290, size=12, bold=True, color=(0, 0, 0))
        janelajogo.draw_text("mines.",  454, 305, size=12, bold=True, color=(0, 0, 0))  




def popout(background,button,janela,click,nome,botao_next,botao_jogo_close_amarelo):
    while True:
        background.draw()
        button.draw()
        informations(nome,janela)
        if click.is_over_object(button) and click.is_button_pressed(True):
            popout_perma(background,button,janela,click,nome,botao_next,botao_jogo_close_amarelo)
        if click.is_over_object(button) == False:
            break
        janela.update()

def popout_perma(background,button,janela,click,nome,botao_next,botao_jogo_close_amarelo,):
    while True:
        background.draw()
        button.draw()
        botao_next.draw()
        botao_jogo_close_amarelo.draw()
        informations(nome,janela)  
        if click.is_over_object(botao_jogo_close_amarelo) and click.is_button_pressed(True):
            break
        janela.update()  




def buttons(botao1,botao2,botao3,botao4):
    botao1.draw()
    botao2.draw()
    botao3.draw()
    botao4.draw()

#tirar isso daqui dps
def redesenhar_menu(boneco,barra_botoes_jogo,botao_jogo_construct,botao_jogo_resources,botao_jogo_research,botao_jogo_reports,botao_jogo_options,menu_jogo,portal_level,janelajogo, portal_level_counter, portal_level_percent,janela_largura):
    boneco.draw()
    barra_botoes_jogo.draw()
    botao_jogo_construct.draw()
    botao_jogo_resources.draw()
    botao_jogo_research.draw()
    botao_jogo_reports.draw()
    botao_jogo_options.draw()
    menu_jogo.draw()

    portal_level.draw()
    #escrever as coisas dentro do visor portal level
    janelajogo.draw_text("Portal Level: ", janela_largura/2 + 470, 23, size=20, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(portal_level_counter), janela_largura/2 + 595, 23.5, size=20, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(portal_level_percent), janela_largura/2 + 482, 47, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("% Chance of", janela_largura/2 + 493, 48, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("spawning Ericis", janela_largura/2 + 474, 68, size=17, bold=True, color=(0, 0, 0))
    #fim

def redesenhar_menu_vermelho(barra_botoes2_jogo,botao1,botao2,botao3,botao4,botao_jogo_close):
    barra_botoes2_jogo.draw()
    botao_jogo_close.draw()
    botao1.draw()
    botao2.draw()
    botao3.draw()
    botao4.draw()


