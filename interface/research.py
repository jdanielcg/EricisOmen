import interface.resources as resources


janela_largura = 1280
janela_altura = 720

pack_tactics = {'food' : 50,'wood' : 200,'stone' : 100,'gold' : 50,'time' : 60}
double_saw = {'food' : 100,'wood' : 50,'stone' : 200,'gold' : 50,'time' : 60}
hardened_picks = {'food' : 200,'wood' : 200,'stone' : 50,'gold' : 50,'time' : 60}
eficient_smelting = {'food' : 200,'wood' : 200,'stone' : 100,'gold' : 25,'time' : 60}

counter = {'no_resource': 60}

p_researching = False
timer = 0

def show_research_blank(interface):
    interface.window.draw_text("Researching:", 1090, 280, size=12, bold=True, color=(0, 0, 0))
    interface.research_bar_idle_small.draw()
    interface.window.draw_text("Time left:", 1090, 335, size=12, bold=True, color=(0, 0, 0))

def research_informations_small(interface):
    if interface.pt == True:
        draw_research_bar_small(interface, 'Pack Tactics')
        interface.window.draw_text("Pack Tactics", 1175, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(pack_tactics['time']), 1158, 335, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 335, size=12, bold=True, color=(224, 224, 220))
    elif interface.ds == True:
        draw_research_bar_small(interface,'double saw')
        interface.window.draw_text("Double Saw", 1175, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(double_saw['time']), 1158, 335, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 335, size=12, bold=True, color=(224, 224, 220))
    elif interface.hp == True:
        draw_research_bar_small(interface,'hardened picks')
        interface.window.draw_text("Hardened Picks", 1171, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(hardened_picks['time']), 1158, 335, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 335, size=12, bold=True, color=(224, 224, 220))
    elif interface.es == True:
        draw_research_bar_small(interface,'eficient smelting')
        interface.window.draw_text("Eficient Smelting", 1168, 280, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text(str(eficient_smelting['time']), 1158, 335, size=12, bold=True, color=(224, 224, 220))
        interface.window.draw_text('seconds', 1175, 335, size=12, bold=True, color=(224, 224, 220))
        
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
        interface.window.draw_text("Pack Tactics",  620, 170, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Food, 200 Wood, 100 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("By learning how to corner their preys and waiting for the right moment to strike,",  454, 275, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Kobolds are now able to take down larger preys on Hunting Camps. Increases",  454, 290, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Food production rate.",  454, 305, size=12, bold=True, color=(0, 0, 0))         
    if nome == 'Double Saw':
        interface.window.draw_text("Double Saw",  620, 170, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("100 Food, 50 Wood, 200 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Cooperative methods of wood cutting turns feeble kobolds on capable lumber",  454, 275, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("jackers. Increases Wood production rate on Woodcutter's camp.",  454, 290, size=12, bold=True, color=(0, 0, 0))
    if nome == 'Hardened Picks':
        interface.window.draw_text("Hardened Picks",  610, 170, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("200 Food, 200 Wood, 50 Stone, 50 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Well-thought crafting techniques creates stronger tools with higher productivity.",  454, 275, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases Stone production rate on quarries.",  454, 290, size=12, bold=True, color=(0, 0, 0))
    if nome == 'Eficient Smelting':
        interface.window.draw_text("Eficient Smelting",  610, 170, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("200 Food, 200 Wood, 100 Stone, 25 Gold",  550, 227, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Understanding that gold melts faster and shapes easier than iron, Kobolds now",  454, 275, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("handle it more carefully than other metals. Increase Gold production rate on",  454, 290, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("mines.",  454, 305, size=12, bold=True, color=(0, 0, 0))  

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
        elif (resources.resources['food'] - pack_tactics['food'] >= 0) and (resources.resources['wood'] - pack_tactics['wood'] >= 0) and (resources.resources['stone'] - pack_tactics['stone']) >= 0 and (resources.resources['gold'] - pack_tactics['gold'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Double Saw':
        if interface.ds_end == True:
            already_researched(interface)
        elif (resources.resources['food'] - double_saw['food'] >= 0) and (resources.resources['wood'] - double_saw['wood'] >= 0) and (resources.resources['stone'] - double_saw['stone']) >= 0 and (resources.resources['gold'] - double_saw['gold'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Hardened Picks':
        if interface.hp_end == True:
            already_researched(interface)
        elif (resources.resources['food'] - hardened_picks['food'] >= 0) and (resources.resources['wood'] - hardened_picks['wood'] >= 0) and (resources.resources['stone'] - hardened_picks['stone']) >= 0 and (resources.resources['gold'] - hardened_picks['gold'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    elif nome =='Eficient Smelting':
        if interface.es_end == True:
            already_researched(interface)
        elif (resources.resources['food'] - eficient_smelting['food'] >= 0) and (resources.resources['wood'] - eficient_smelting['wood'] >= 0) and (resources.resources['stone'] - eficient_smelting['stone']) >= 0 and (resources.resources['gold'] - eficient_smelting['gold'] >= 0):
            interface.botao_next.draw()
        else:
            no_resources(interface)
    if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
        if nome == 'Pack Tactics':
            interface.pt = True
            interface.ds = False
            interface.hp = False
            interface.es = False
        if nome == 'Double Saw':
            interface.pt = False
            interface.ds = True
            interface.hp = False
            interface.es = False
        if nome == 'Hardened Picks':
            interface.pt = False
            interface.ds = False
            interface.hp = True
            interface.es = False
        if nome == 'Eficient Smelting':
            interface.pt = False
            interface.ds = False
            interface.hp = False
            interface.es = True
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
        if (resources.resources['food'] - pack_tactics['food'] >= 0) and (resources.resources['wood'] - pack_tactics['wood'] >= 0) and (resources.resources['stone'] - pack_tactics['stone']) >= 0 and (resources.resources['gold'] - pack_tactics['gold'] >= 0): 
            resources.resources['food'] -= pack_tactics['food']
            resources.resources['wood'] -= pack_tactics['wood']
            resources.resources['stone']  -= pack_tactics['stone']
            resources.resources['gold']  -= pack_tactics['gold']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Double Saw':
        if (resources.resources['food'] - double_saw['food'] >= 0) and (resources.resources['wood'] - double_saw['wood'] >= 0) and (resources.resources['stone'] - double_saw['stone']) >= 0 and (resources.resources['gold'] - double_saw['gold'] >= 0):
            resources.resources['food'] -= double_saw['food']
            resources.resources['wood'] -= double_saw['wood']
            resources.resources['stone']  -= double_saw['stone']
            resources.resources['gold']  -= double_saw['gold']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Hardened Picks':
        if (resources.resources['food'] - hardened_picks['food'] >= 0) and (resources.resources['wood'] - hardened_picks['wood'] >= 0) and (resources.resources['stone'] - hardened_picks['stone']) >= 0 and (resources.resources['gold'] - hardened_picks['gold'] >= 0):
            resources.resources['food'] -= hardened_picks['food']
            resources.resources['wood'] -= hardened_picks['wood']
            resources.resources['stone']  -= hardened_picks['stone']
            resources.resources['gold']  -= hardened_picks['gold']
            interface.gate = True
        else:
            interface.gate = False
    if nome == 'Eficient Smelting':
        if (resources.resources['food'] - eficient_smelting['food'] >= 0) and (resources.resources['wood'] - eficient_smelting['wood'] >= 0) and (resources.resources['stone'] - eficient_smelting['stone']) >= 0 and (resources.resources['gold'] - eficient_smelting['gold'] >= 0):
            resources.resources['food'] -= eficient_smelting['food']
            resources.resources['wood'] -= eficient_smelting['wood']
            resources.resources['stone']  -= eficient_smelting['stone']
            resources.resources['gold']  -= eficient_smelting['gold']
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
    interface.window.draw_text("Already researching",  janela_largura/2 - 20, janela_altura/2 + 240, size=24, bold=True, color=(109,113,46))

def already_researched(interface):
    interface.window.draw_text("Already researched",  janela_largura/2 - 20, janela_altura/2 + 241, size=24, bold=True, color=(75,183,32))

def no_resources(interface):
    interface.window.draw_text("Not enough resources",  janela_largura/2 - 20, janela_altura/2 + 240, size=24, bold=True, color=(183,20,20))

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


