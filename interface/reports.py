# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: RAMON SANTOS         ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from match import Match
from interface.icons import text_icon
import interface.research as research
from movables.waver import Waver


def redesenhar_menu_vermelho(barra_botoes2_jogo,botao_jogo_close):
    barra_botoes2_jogo.draw()
    botao_jogo_close.draw()

#waves

def next_wave(interface):
    #precisa ser feito alguma condição aqui pro jogo saber que já acabou a wave de inimigos e reiniciar o contador. Por exemplo:
    #if number_max_enemies == 0:
    #   interface.isAttacking = False
    #   interface.AttackTimer = 120
    pos = (1092, 300)
    if (Waver.is_attacking):
        Match.game.screen.blit(text_icon("sword",  "   ATTACK".format(round(Waver.interval)), (200, 5,5), large = True),pos)        
    else:
        Match.game.screen.blit(text_icon("shield",  "ATTACK IN {}".format(round(Waver.interval - Waver.timer)), (255, 255,255), large = True),pos)


def research_informations(interface):
    interface.window.draw_text("Research:", 30, 200, size=20, bold=True, color=(109, 113, 46))
    interface.research_bar_idle.draw()
    interface.window.draw_text("Time left:", 30, 295, size=20, bold=True, color=(109, 113, 46))

    if interface.pt == True:
        research.draw_research_bar(interface, 'Pack Tactics')
        interface.window.draw_text("Pack Tactics", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.pack_tactics['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))
    elif interface.ds == True:
        research.draw_research_bar(interface,'double saw')
        interface.window.draw_text("Double Saw", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.double_saw['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))
    elif interface.wp == True:
        research.draw_research_bar(interface,'warpainting')
        interface.window.draw_text("warpainting", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.warpainting['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))
    elif interface.es == True:
        research.draw_research_bar(interface,'eficient smelting')
        interface.window.draw_text("Eficient Smelting", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.eficient_smelting['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))