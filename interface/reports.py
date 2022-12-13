import interface.research as research


def redesenhar_menu_vermelho(barra_botoes2_jogo,botao_jogo_close):
    barra_botoes2_jogo.draw()
    botao_jogo_close.draw()

#waves

def next_wave(interface):
    interface.counter_next_wave += 1
    interface.window.draw_text("Next wave:", 1090, 375, size=12, bold=True, color=(0, 0, 0))
    if interface.IsAttacking == True:
        interface.window.draw_text("Attacking", 1170, 372, size=17, bold=True, color=(183,20,20))
    if interface.AttackTimer == 0:
        interface.IsAttacking = True
    if interface.IsAttacking == False and interface.AttackTimer != 0:
        interface.window.draw_text(str(interface.AttackTimer), 1165, 375, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text("seconds", 1190, 375, size=12, bold=True, color=(224, 224, 220))
        if interface.counter_next_wave > 60:
            interface.counter_next_wave = 0
            interface.AttackTimer -= 1



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
    elif interface.hp == True:
        research.draw_research_bar(interface,'hardened picks')
        interface.window.draw_text("Hardened Picks", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.hardened_picks['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))
    elif interface.es == True:
        research.draw_research_bar(interface,'eficient smelting')
        interface.window.draw_text("Eficient Smelting", 180, 203, size=17, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(research.eficient_smelting['time']), 160, 295, size=20, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 195, 295, size=20, bold=True, color=(224, 224, 220))