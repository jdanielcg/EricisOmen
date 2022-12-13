from match import Match

janela_largura = 1280
janela_altura = 720

pack_tactics = {'wood' : 200,'iron' : 100,'time' : 60}
double_saw = {'wood' : 50,'iron' : 200,'time' : 60}
hardened_picks = {'wood' : 200,'iron' : 50,'time' : 60}
eficient_smelting = {'wood' : 200,'iron' : 100,'time' : 60}

counter = {'no_resource': 60}

p_researching = False
timer = 0

def show_research_blank(interface):
    interface.window.draw_text("Research:", 1090, 280, size=12, bold=True, color=(0, 0, 0))
    interface.research_bar_idle_small.draw()
    interface.window.draw_text("Time left:", 1090, 345, size=12, bold=True, color=(0, 0, 0))

def research_informations_small(interface):
    if interface.pt == True:
        draw_research_bar_small(interface, 'Pack Tactics')
        interface.window.draw_text("Pack Tactics", 1165, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(pack_tactics['time']), 1158, 345, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 345, size=12, bold=True, color=(224, 224, 220))
    elif interface.ds == True:
        draw_research_bar_small(interface,'double saw')
        interface.window.draw_text("Double Saw", 1165, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(double_saw['time']), 1158, 345, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 345, size=12, bold=True, color=(224, 224, 220))
    elif interface.hp == True:
        draw_research_bar_small(interface,'hardened picks')
        interface.window.draw_text("Hardened Picks", 1161, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(hardened_picks['time']), 1158, 345, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 345, size=12, bold=True, color=(224, 224, 220))
    elif interface.es == True:
        draw_research_bar_small(interface,'eficient smelting')
        interface.window.draw_text("Efficient Smelting", 1153, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(eficient_smelting['time']), 1158, 345, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 345, size=12, bold=True, color=(224, 224, 220))
        
def draw_research_bar_small(interface,p):
    if p == 'Pack Tactics':
        if 45 < pack_tactics['time'] and pack_tactics['time'] <= 60:
            interface.research_bar_idle_small.draw()
        elif 30 < pack_tactics['time'] and pack_tactics['time'] <= 45:
            interface.research_bar_2_small.draw()
        elif 15 < pack_tactics['time'] and pack_tactics['time']/4 <= 30:
            interface.research_bar_3_small.draw()
        elif 0 <= pack_tactics['time'] and pack_tactics['time']/4 < 15:
            interface.research_bar_4_small.draw()
    if p == 'double saw':
        if 45 < double_saw['time'] and double_saw['time'] <= 60:
            interface.research_bar_idle_small.draw()
        elif 30 < double_saw['time'] and double_saw['time'] <= 45:
            interface.research_bar_2_small.draw()
        elif 15 < double_saw['time'] and double_saw['time']/4 <= 30:
            interface.research_bar_3_small.draw()
        elif 0 <= double_saw['time'] and double_saw['time']/4 < 15:
            interface.research_bar_4_small.draw()
    if p == 'hardened picks':
        if 45 < hardened_picks['time'] and hardened_picks['time'] <= 60:
            interface.research_bar_idle_small.draw()
        elif 30 < hardened_picks['time'] and hardened_picks['time'] <= 45:
            interface.research_bar_2_small.draw()
        elif 15 < hardened_picks['time'] and hardened_picks['time']/4 <= 30:
            interface.research_bar_3_small.draw()
        elif 0 <= hardened_picks['time'] and hardened_picks['time']/4 < 15:
            interface.research_bar_4_small.draw()
    if p == 'eficient smelting':
        if 45 < eficient_smelting['time'] and eficient_smelting['time'] <= 60:
            interface.research_bar_idle_small.draw()
        elif 30 < eficient_smelting['time'] and eficient_smelting['time'] <= 45:
            interface.research_bar_2_small.draw()
        elif 15 < eficient_smelting['time'] and eficient_smelting['time']/4 <= 30:
            interface.research_bar_3_small.draw()
        elif 0 <= eficient_smelting['time'] and eficient_smelting['time']/4 < 15:
            interface.research_bar_4_small.draw()

def informations(nome,interface):
    if nome == 'Pack Tactics':
        interface.window.draw_text("Pack Tactics",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("200 Wood, 100 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("By learning how to corner their",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("preys and waiting for the right",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("moment to strike, Kobolds are",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("now able to take down foes",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("easier.",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases Tower damage.",  240, 455, size=15, bold=True, color=(0, 0, 0))         
    if nome == 'Double Saw':
        interface.window.draw_text("Double Saw",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 200 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Cooperative methods of wood",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("cutting turns feeble kobolds",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("on capable lumber jackers.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases wood",  244, 425, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("production rate on Wood",  242, 440, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("cutter's camps.",  242, 455, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Hardened Picks':
        interface.window.draw_text("Hardened Picks",  255, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("200 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Well-thought crafting",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("techniques creates stronger",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("tools with higher productivity.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases Iron production",  244, 425, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("rate on mines.",  244, 440, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Eficient Smelting':
        interface.window.draw_text("Efficient Smelting",  250, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("200 Wood, 100 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Constant observations, together",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("with try and error, made kobolds",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("able to understand iron fusion",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("point properly.",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increase iron",  244, 440, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("production rate on mines.",  244, 455, size=15, bold=True, color=(0, 0, 0)) 

def popout_perma(interface,nome):
    interface.background_cost_menu.draw()
    interface.botao_jogo_close_amarelo.draw()
    if interface.clickjogo.is_over_object(interface.botao_jogo_close_amarelo) and interface.clickjogo.is_button_pressed(True):
        if nome == 'Pack Tactics':
            interface.exibir_menu_research_pack_tactics = False
        if nome == 'Double Saw':
            interface.exibir_menu_research_double_saw = False
        if nome == 'Hardened Picks':
            interface.exibir_menu_research_hardened_picks = False
        if nome == 'Eficient Smelting':
            interface.exibir_menu_research_eficient_smelting = False
    informations(nome,interface)
    if (interface.pt == True and pack_tactics['time']>=0) or (interface.ds == True and double_saw['time']>=0) or (interface.hp == True and hardened_picks['time']>=0) or (interface.es == True and eficient_smelting['time']>=0):
        already_researching(interface)
    elif nome =='Pack Tactics':
        if interface.pt_end == True:
            already_researched(interface)
        elif (Match.wood - pack_tactics['wood'] >= 0) and (Match.iron - pack_tactics['iron'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Double Saw':
        if interface.ds_end == True:
            already_researched(interface)
        elif (Match.wood - double_saw['wood'] >= 0) and (Match.iron - double_saw['iron'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Hardened Picks':
        if interface.hp_end == True:
            already_researched(interface)
        elif (Match.wood - hardened_picks['wood'] >= 0) and (Match.iron - hardened_picks['iron'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Eficient Smelting':
        if interface.es_end == True:
            already_researched(interface)
        elif (Match.wood - eficient_smelting['wood'] >= 0) and (Match.iron - eficient_smelting['iron'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
        if nome == 'Pack Tactics':
            interface.pt = True
            interface.ds = False
            interface.hp = False
            interface.es = False
            interface.exibir_menu_research_pack_tactics = False
        if nome == 'Double Saw':
            interface.pt = False
            interface.ds = True
            interface.hp = False
            interface.es = False
            interface.exibir_menu_research_double_saw = False
        if nome == 'Hardened Picks':
            interface.pt = False
            interface.ds = False
            interface.hp = True
            interface.es = False
            interface.exibir_menu_research_hardened_picks = False
        if nome == 'Eficient Smelting':
            interface.pt = False
            interface.ds = False
            interface.hp = False
            interface.es = True
            interface.exibir_menu_research_eficient_smelting = False
        if interface.pt == True:
            check_for_resources('Pack Tactics', interface)
            if interface.gate == False:
                interface.pt = False
        if interface.ds == True:
            check_for_resources('Double Saw', interface)
            if interface.gate == False:
                interface.ds = False
        if interface.hp == True:
            check_for_resources('Hardened Picks', interface)
            if interface.gate == False:
                interface.hp = False
        if interface.es == True:
            check_for_resources('Eficient Smelting', interface)
            if interface.gate == False:
                interface.es = False


def popout(interface,nome):
    interface.background_cost_menu.draw()
    informations(nome,interface)
        
def check_for_resources(nome,interface):
    if nome == 'Pack Tactics':
        if (Match.wood - pack_tactics['wood'] >= 0) and (Match.iron - pack_tactics['iron'] >= 0): 
            Match.wood -= pack_tactics['wood']
            Match.iron -= pack_tactics['iron']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Double Saw':
        if (Match.wood - double_saw['wood'] >= 0) and (Match.iron - double_saw['iron'] >= 0):
            Match.wood -= double_saw['wood']
            Match.iron -= double_saw['iron']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Hardened Picks':
        if (Match.wood - hardened_picks['wood'] >= 0) and (Match.iron - hardened_picks['iron'] >= 0):
            Match.wood -= hardened_picks['wood']
            Match.iron -= hardened_picks['iron']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Eficient Smelting':
        if (Match.wood - eficient_smelting['wood'] >= 0) and (Match.iron - eficient_smelting['iron'] >= 0):
            Match.wood -= eficient_smelting['wood']
            Match.iron -= eficient_smelting['iron']
            interface.gate = True
        else:
            interface.gate = False

def researching(interface):
    if interface.pt == True and interface.ds == False and interface.hp == False and interface.es == False:
        research_progress('Pack Tactics', interface)

    if interface.pt == False and interface.ds == True and interface.hp == False and interface.es == False:
        research_progress('double saw', interface)

    if interface.pt == False and interface.ds == False and interface.hp == True and interface.es == False:
        research_progress('hardened picks', interface)

    if interface.pt == False and interface.ds == False and interface.hp == False and interface.es == True:
        research_progress('eficient smelting', interface)


def research_progress(nome, interface):
        interface.timer +=1
        if nome == 'Pack Tactics':
            if interface.timer == 60:
                interface.timer = 0
                if pack_tactics['time'] > 0:
                    pack_tactics['time'] -= 1
                else:
                    research_end('Pack Tactics', interface)
        if nome == 'double saw':
            if interface.timer == 60:
                interface.timer = 0
                if double_saw['time'] > 0:
                    double_saw['time'] -= 1
                else:
                    research_end('double saw', interface)
        if nome == 'hardened picks':
            if interface.timer == 60:
                interface.timer = 0
                if hardened_picks['time'] > 0:
                    hardened_picks['time'] -= 1
                else:
                    research_end('hardened picks', interface)
        if nome == 'eficient smelting':
            if interface.timer == 60:
                interface.timer = 0
                if eficient_smelting['time'] > 0:
                    eficient_smelting['time'] -= 1
                else:
                    research_end('eficient smelting', interface)

def research_end(nome, interface):
    if nome == 'Pack Tactics':
        if interface.pt == True:
            interface.pt = False
        if interface.pt_end == False:
            interface.pt_end = True
    if nome == 'double saw':
        if interface.ds == True:
            interface.ds = False
        if interface.ds_end == False:
            interface.ds_end = True
    if nome == 'hardened picks':
        if interface.hp == True:
            interface.hp = False
        if interface.hp_end == False:
            interface.hp_end = True
    if nome == 'eficient smelting':
        if interface.es == True:
            interface.es = False
        if interface.es_end == False:
            interface.es_end = True


def already_researching(interface):
    interface.window.draw_text("Already",  345, 545, size=24, bold=True, color=(255,215,0))
    interface.window.draw_text("researching",  325, 575, size=24, bold=True, color=(255,215,0))

def already_researched(interface):
    interface.window.draw_text("Already",  345, 545, size=24, bold=True, color=(75,183,32))
    interface.window.draw_text("researched",  325, 575, size=24, bold=True, color=(75,183,32))

def no_resources(interface):
    interface.window.draw_text("Not enough",  330, 545, size=24, bold=True, color=(183,20,20))
    interface.window.draw_text("resources",  340, 575, size=24, bold=True, color=(183,20,20))

def draw_research_bar(interface,p):
    if p == 'Pack Tactics':
        if 45 < pack_tactics['time'] and pack_tactics['time'] <= 60:
            interface.research_bar_idle.draw()
        elif 30 < pack_tactics['time'] and pack_tactics['time'] <= 45:
            interface.research_bar_2.draw()
        elif 15 < pack_tactics['time'] and pack_tactics['time']/4 <= 30:
            interface.research_bar_3.draw()
        elif 0 <= pack_tactics['time'] and pack_tactics['time']/4 < 15:
            interface.research_bar_4.draw()
    if p == 'double saw':
        if 45 < double_saw['time'] and double_saw['time'] <= 60:
            interface.research_bar_idle.draw()
        elif 30 < double_saw['time'] and double_saw['time'] <= 45:
            interface.research_bar_2.draw()
        elif 15 < double_saw['time'] and double_saw['time']/4 <= 30:
            interface.research_bar_3.draw()
        elif 0 <= double_saw['time'] and double_saw['time']/4 < 15:
            interface.research_bar_4.draw()
    if p == 'hardened picks':
        if 45 < hardened_picks['time'] and hardened_picks['time'] <= 60:
            interface.research_bar_idle.draw()
        elif 30 < hardened_picks['time'] and hardened_picks['time'] <= 45:
            interface.research_bar_2.draw()
        elif 15 < hardened_picks['time'] and hardened_picks['time']/4 <= 30:
            interface.research_bar_3.draw()
        elif 0 <= hardened_picks['time'] and hardened_picks['time']/4 < 15:
            interface.research_bar_4.draw()
    if p == 'eficient smelting':
        if 45 < eficient_smelting['time'] and eficient_smelting['time'] <= 60:
            interface.research_bar_idle.draw()
        elif 30 < eficient_smelting['time'] and eficient_smelting['time'] <= 45:
            interface.research_bar_2.draw()
        elif 15 < eficient_smelting['time'] and eficient_smelting['time']/4 <= 30:
            interface.research_bar_3.draw()
        elif 0 <= eficient_smelting['time'] and eficient_smelting['time']/4 < 15:
            interface.research_bar_4.draw()

def desenhar_menu_vermelho(interface):
    interface.barra_botoes2_jogo.draw()
    interface.botao_jogo_close.draw()
    interface.taticas_de_matilha.draw()
    interface.serrote_duplo.draw()
    interface.hardened_picks.draw()
    interface.eficient_smelting.draw()


