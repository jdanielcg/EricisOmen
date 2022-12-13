from interface.buildings import buildings_counter, buildings_capacity
from match import Match

def show_resources(interface):
    interface.show_resources.draw()

    interface.window.draw_text("Wood:", 1100, 153, size=18, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(Match.wood), 1180, 155, size=15, bold=True, color=(224, 224, 220))
    interface.window.draw_text('/', 1210, 153, size=18, bold=True, color=(224, 224, 220))
    interface.window.draw_text(str(Match.max_wood), 1219, 155, size=15, bold=True, color=(224, 224, 220))

    interface.window.draw_text("Iron:", 1100, 178, size=18, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(Match.iron), 1180, 179, size=15, bold=True, color=(224, 224, 220))
    interface.window.draw_text('/', 1210, 178, size=18, bold=True, color=(224, 224, 220))
    interface.window.draw_text(str(Match.max_iron), 1219, 179, size=15, bold=True, color=(224, 224, 220))

    interface.window.draw_text("Soldiers:", 1100, 203, size=18, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(Match.soldiers), 1190, 204, size=15, bold=True, color=(224, 224, 220))
    interface.window.draw_text('/', 1210, 203, size=18, bold=True, color=(224, 224, 220))
    interface.window.draw_text(str(Match.max_soldiers), 1219, 204, size=15, bold=True, color=(224, 224, 220))

    interface.window.draw_text("Aether:", 1100, 228, size=18, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(Match.aether), 1180, 229, size=15, bold=True, color=(224, 224, 220))
    interface.window.draw_text('/', 1210, 228, size=18, bold=True, color=(224, 224, 220))
    interface.window.draw_text(str(Match.max_aether), 1219, 229, size=15, bold=True, color=(224, 224, 220))

def change_resources(interface):
    interface.resources_counter +=1
    if interface.resources_counter > 60:
        interface.resources_counter = 0
        if Match.wood > 0 and Match.wood <= Match.max_wood:
            Match.wood += (Match.Balance['wood'])
            if Match.wood > Match.max_wood:
                Match.wood = Match.max_wood
            if Match.wood < 0:
                Match.wood = 0
        if Match.iron > 0 and Match.iron <= Match.max_iron:
            Match.iron += (Match.Balance['iron'])
            if Match.iron > Match.max_iron:
                Match.iron = Match.max_iron
            if Match.iron < 0:
                Match.iron = 0
        if Match.soldiers > 0 and Match.soldiers <= Match.max_soldiers:
            Match.soldiers += (Match.Balance['soldiers'])
            if Match.soldiers > Match.max_soldiers:
                Match.soldiers = Match.max_soldiers
            if Match.soldiers < 0:
                Match.soldiers = 0
        if Match.aether > 0 and Match.aether <= Match.max_aether:
            Match.aether += (Match.Balance['aether'])
            if Match.aether > Match.max_aether:
                Match.aether = Match.max_aether
            if Match.aether < 0:
                Match.aether = 0
    return interface.resources_counter

def change_max_resources(Match): 
    #trocar manualmente aqui o max resource do if, pq por algum motivo tá bugando se tentar acessar o dic
    if Match.max_wood != (500 + (buildings_capacity['wood'] * buildings_counter['warehouse'])): #500 = Match.max_wood
        Match.max_wood = Match.max_wood + (buildings_capacity['wood'] * buildings_counter['warehouse'])

    if Match.max_iron != (300 + (buildings_capacity['iron'] * buildings_counter['warehouse'])): #300 = Match.max_iron
        Match.max_iron = Match.max_iron + (buildings_capacity['iron'] * buildings_counter['warehouse'])

    if Match.max_soldiers != (50 + (buildings_capacity['soldiers'] * buildings_counter['barrack'])): #50 = Match.max_soldiers
        Match.max_soldiers = Match.max_soldiers + (buildings_capacity['soldiers'] * buildings_counter['barrack'])

    if Match.max_aether != (100 + (buildings_capacity['aether'] * buildings_counter['obelisk'])): #100 = Match.max_aether
        Match.max_aether = Match.max_aether + (buildings_capacity['aether'] * buildings_counter['obelisk'])
    



def stocked(janelajogo):
    janelajogo.draw_text("Stocked:", 30, 195, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("wood:", 30, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(Match.wood), 65, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("iron:", 105, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(Match.iron), 145, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("soldiers:", 187, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(Match.soldiers), 227, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("aether:", 275, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(Match.aether), 310, 220, size=12, bold=True, color=(224, 224, 220))

def input(janelajogo):
    janelajogo.draw_text("Income:", 30, 245, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("wood:", 30, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 67, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(Match.income['wood']), 80, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("iron:", 105, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 147, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(Match.income['iron']), 160, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("soldiers:", 187, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 227, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(Match.income['soldiers']), 242, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("aether:", 275, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 310, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(Match.income['aether']), 325, 270, size=12, bold=True, color=(75,183,32))

def output(janelajogo):
    janelajogo.draw_text("Outcome:", 30, 295, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("wood:", 30, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 67, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(Match.outcome['wood']), 80, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("iron:", 105, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 147, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(Match.outcome['iron']), 160, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("soldiers:", 187, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 228, 319, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(Match.outcome['soldiers']), 242, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("aether:", 275, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 310, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(Match.outcome['aether']), 325, 320, size=12, bold=True, color=(236, 88, 0))

def Balance(janelajogo):
    janelajogo.draw_text("Balance:", 30, 345, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("wood:", 30, 370, size=12, bold=True, color=(0, 0, 0))

    if Match['wood'] >= 0:
        janelajogo.draw_text(str(Match['wood']), 80, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Match['wood']), 80, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("iron:", 105, 370, size=12, bold=True, color=(0, 0, 0))
    if Match['iron'] >= 0:
        janelajogo.draw_text(str(Match['iron']), 160, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Match['iron']), 160, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("soldiers:", 187, 370, size=12, bold=True, color=(0, 0, 0))
    if Match['soldiers'] >= 0:
        janelajogo.draw_text(str(Match['soldiers']), 242, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Match['soldiers']), 242, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("aether:", 275, 370, size=12, bold=True, color=(0, 0, 0))
    if Match['aether'] >= 0:
        janelajogo.draw_text(str(Match['aether']), 325, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Match['aether']), 325, 370, size=12, bold=True, color=(236, 88, 0))



      