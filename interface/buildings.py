from match import Match
from settings import SimulationMode
buildings_counter = {
    "warehouse": 0,
    "barrack": 0,
    "obelisk": 0
}

buildings_capacity = {
    "wood": 150,
    "iron": 100,
    "soldiers": 20,
    "aether": 100
}

barracks_cost = {'wood': 50}
warehouse_cost = {'wood': 50}
fire_tower_cost = {'wood': 50, 'iron': 50}
frost_tower_cost = {'wood': 50, 'iron': 50}
rock_tower_cost = {'wood': 50, 'iron': 50}
poison_trap_cost = {'wood': 50, 'iron': 50}
fire_trap_cost = {'wood': 50, 'iron': 50}
wall_cost = {'wood': 50, 'iron': 50}
obelisk_cost = {'aether': 100}
mining_camp_cost = {'wood': 50}
wood_camp_cost = {'wood': 50}

def show_menu_construct(interface):
    interface.botao_construct_direita.draw()
    interface.botao_construct_esquerda.draw()
    
    if interface.p_construct == True:
        interface.botao_barracks.draw()
        interface.botao_warehouse.draw()
        interface.botao_firetower.draw()
        interface.botao_frosttower.draw()
        interface.botao_rocktower.draw()
        interface.botao_poisontrap.draw()
        interface.botao_firetrap.draw()
        if interface.clickjogo.is_over_object(interface.botao_construct_direita) and interface.clickjogo.is_button_pressed(True):
            interface.construct_page = 2
            interface.p_construct = False
    if interface.p_construct == False:
        interface.botao_wall.draw()
        interface.botao_obelisk.draw()
        interface.botao_miningcamp.draw()
        interface.botao_woodcamp.draw()
        if interface.clickjogo.is_over_object(interface.botao_construct_esquerda) and interface.clickjogo.is_button_pressed(True):
           interface.construct_page = 1
           interface.p_construct = True

def popout_perma(interface,nome):
    interface.background_cost_menu.draw()
    interface.botao_jogo_close_amarelo.draw()
    informations(interface, nome)
    if interface.clickjogo.is_over_object(interface.botao_jogo_close_amarelo) and interface.clickjogo.is_button_pressed(True):
        if nome == 'Barracks':
            interface.exibir_menu_construct_barracks = False
        if nome == 'Warehouse':
            interface.exibir_menu_construct_warehouse = False
        if nome == 'Fire_tower':
            interface.exibir_menu_construct_fire_tower = False
        if nome == 'Frost_tower':
            interface.exibir_menu_construct_frost_tower = False
        if nome == 'Rock_tower':
            interface.exibir_menu_construct_rock_tower = False
        if nome == 'Poison_trap':
            interface.exibir_menu_construct_poison_trap = False
        if nome == 'Fire_trap':
            interface.exibir_menu_construct_fire_trap = False
        if nome == 'Wall':
            interface.exibir_menu_construct_wall = False
        if nome == 'Obelisk':
            interface.exibir_menu_construct_obelisk = False
        if nome == 'Mining_camp':
            interface.exibir_menu_construct_mining_camp = False
        if nome == 'Wood_camp':
            interface.exibir_menu_construct_woodcamp = False
    if nome =='Barracks':
        if (Match.wood - barracks_cost['wood'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("dormitory")                
        else:
            no_resources(interface)
    elif nome =='Warehouse':
        if (Match.wood - warehouse_cost['wood'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("stockpile")
        else:
            no_resources(interface)
    elif nome =='Fire_tower':
        if (Match.wood - fire_tower_cost['wood'] >= 0 and Match.iron - fire_tower_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("firetower")
        else:
            no_resources(interface)
    elif nome =='Frost_tower':
        if (Match.wood - frost_tower_cost['wood'] >= 0 and Match.iron - frost_tower_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("icetower")
        else:
            no_resources(interface)
    elif nome =='Rock_tower':
        if (Match.wood - rock_tower_cost['wood'] >= 0 and Match.iron - rock_tower_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("stonetower")
        else:
            no_resources(interface)
    elif nome =='Poison_trap':
        if (Match.wood - poison_trap_cost['wood'] >= 0 and Match.iron - poison_trap_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("poisontrap")
        else:
            no_resources(interface)
    elif nome =='Fire_trap':
        if (Match.wood - fire_trap_cost['wood'] >= 0 and Match.iron - fire_trap_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("firetrap")
        else:
            no_resources(interface)
    elif nome =='Wall':
        if (Match.wood - wall_cost['wood'] >= 0 and Match.iron - wall_cost['iron'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("wall")
        else:
            no_resources(interface)
    elif nome =='Obelisk':
        if (Match.aether - obelisk_cost['aether'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("obelisk")
        else:
            no_resources(interface)
    elif nome =='Mining_camp':
        if (Match.wood - mining_camp_cost['wood'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("miningcamp")
        else:
            no_resources(interface)
    elif nome =='Wood_camp':
        if (Match.wood - wood_camp_cost['wood'] >= 0):
            interface.botao_next.draw()
            if interface.clickjogo.is_over_object(interface.botao_next) and interface.clickjogo.is_button_pressed(True):
                Match.game.building_mode_interface.start("lumbercamp")
        else:
            no_resources(interface)
        

def popout(interface,nome):
    interface.background_cost_menu.draw()
    informations(interface,nome)

def informations(interface,nome):
    if nome == 'Barracks':
        interface.window.draw_text("Barracks",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("An cozy place for",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("kobolds to rest and",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("recover from their",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("wounds.",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases Soldiers max capacity.",  240, 455, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Warehouse':
        interface.window.draw_text("Warehouse",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A makeshift place for",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("kobolds store",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("resources.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increases Wood and Iron",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("max capacity.",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Fire_tower':
        interface.window.draw_text("Fire Tower",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A defensive tower that",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("shoots fireballs at",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("approaching enemies.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Deals medium damage.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Frost_tower':
        interface.window.draw_text("Frost Tower",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A defensive tower that",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("shoots ice balls at",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("approaching enemies.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Deals low damage.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Slow down enemies.",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Rock_tower':
        interface.window.draw_text("Rock Tower",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A defensive tower that",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("shoots boulders at",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("approaching enemies.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Deals low damage.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Poison_trap':
        interface.window.draw_text("Poison trap",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A clever mechanism that",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("releases poisonous gas",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("into a surrounding area",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("when triggered.",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Deals low damage per second.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Slow down enemies.",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Fire_trap':
        interface.window.draw_text("Fire trap",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A clever mechanism that",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("ignites a surrounding",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("area when triggered",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Deals medium damage per second.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Wall':
        interface.window.draw_text("Wall",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("50 Wood, 50 Iron",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A defensive perimeter",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("that forces enemies to",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("break through before",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("crossing",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Blocks enemies movements.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Obelisk':
        interface.window.draw_text("Obelisk",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Aether: 100",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A holy inscripted shrine",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("containing wards to worship",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Ericis.",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increase Aether max capacity.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Expands corrupted zone.",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Mining_camp':
        interface.window.draw_text("Mining camp",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Wood: 50",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A place to house miners and",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("mining equipments. It destroys",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("surrounding boulders for",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("resources.",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increase Iron income.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))
    if nome == 'Wood_camp':
        interface.window.draw_text("Wood camp",  270, 220, size=20, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Wood: 50",  255, 280, size=16, bold=True, color=(0, 0, 0))
        interface.window.draw_text("A place to house choppers and",  242, 345, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("lumber equipments. It destroys",  242, 360, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("surrounding trees for",  242, 375, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("resources.",  242, 390, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  242, 405, size=12, bold=True, color=(0, 0, 0))
        interface.window.draw_text("Increase Wood income.",  240, 455, size=15, bold=True, color=(0, 0, 0))
        interface.window.draw_text("",  240, 505, size=15, bold=True, color=(0, 0, 0))

def no_resources(interface):
    interface.window.draw_text("Not enough",  330, 545, size=24, bold=True, color=(183,20,20))
    interface.window.draw_text("resources",  340, 575, size=24, bold=True, color=(183,20,20))
    