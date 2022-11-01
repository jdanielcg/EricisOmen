
resources = {"food": 30000,"wood": 30000,"stone": 20000,"gold": 5000}
income = {"food": 5,"wood": 4,"stone":2,"gold":1}
outcome = {"food": 3,"wood": 5,"stone":1,"gold":0}
Balance = {"food": income['food'] - outcome['food'],"wood": income['wood'] - outcome['wood'], "stone": income['stone'] - outcome['stone'], "gold": income['gold'] - outcome['gold']}

def show_resources(interface):
    interface.show_resources.draw()
    interface.window.draw_text("Food:", 1090, 155, size=24, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(resources['food']), 1190, 156, size=24, bold=True, color=(224, 224, 220))
    interface.window.draw_text("Wood:", 1090, 180, size=24, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(resources['wood']), 1190, 181, size=24, bold=True, color=(224, 224, 220))
    interface.window.draw_text("Stone:", 1090, 205, size=24, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(resources['stone']), 1190, 207, size=24, bold=True, color=(224, 224, 220))
    interface.window.draw_text("Gold:", 1090, 230, size=24, bold=True, color=(0, 0, 0))
    interface.window.draw_text(str(resources['gold']), 1190, 232, size=24, bold=True, color=(224, 224, 220))

def change_resources(resources,Balance,counter):
    counter +=1
    if counter > 60:
        counter = 0
        if resources['food'] > 0:
            resources['food'] += (Balance['food'])
        if resources['wood'] > 0:
            resources['wood'] += (Balance['wood'])
        if resources['stone'] > 0:
            resources['stone'] += (Balance['stone'])
        if resources['gold'] > 0:
            resources['gold'] += (Balance['gold'])
    return counter

def stocked(janelajogo):
    janelajogo.draw_text("Stocked:", 30, 195, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("Food:", 30, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(resources['food']), 65, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("Wood:", 105, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(resources['wood']), 145, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("Stone:", 187, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(resources['stone']), 227, 220, size=12, bold=True, color=(224, 224, 220))
    janelajogo.draw_text("Gold:", 275, 220, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text(str(resources['gold']), 310, 220, size=12, bold=True, color=(224, 224, 220))

def input(janelajogo):
    janelajogo.draw_text("Income:", 30, 245, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("Food:", 30, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 67, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(income['food']), 80, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("Wood:", 105, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 147, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(income['wood']), 160, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("Stone:", 187, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 227, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(income['stone']), 242, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text("Gold:", 275, 270, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('+', 310, 270, size=12, bold=True, color=(75,183,32))
    janelajogo.draw_text(str(income['gold']), 325, 270, size=12, bold=True, color=(75,183,32))

def output(janelajogo):
    janelajogo.draw_text("Outcome:", 30, 295, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("Food:", 30, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 67, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(outcome['food']), 80, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("Wood:", 105, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 147, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(outcome['wood']), 160, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("Stone:", 187, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 228, 319, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(outcome['stone']), 242, 320, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text("Gold:", 275, 320, size=12, bold=True, color=(0, 0, 0))
    janelajogo.draw_text('-', 310, 318, size=12, bold=True, color=(236, 88, 0))
    janelajogo.draw_text(str(outcome['gold']), 325, 320, size=12, bold=True, color=(236, 88, 0))

def balance(janelajogo):
    janelajogo.draw_text("Balance:", 30, 345, size=17, bold=True, color=(0, 0, 0))
    janelajogo.draw_text("Food:", 30, 370, size=12, bold=True, color=(0, 0, 0))

    if Balance['food'] >= 0:
        janelajogo.draw_text(str(Balance['food']), 80, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Balance['food']), 80, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("Wood:", 105, 370, size=12, bold=True, color=(0, 0, 0))
    if Balance['wood'] >= 0:
        janelajogo.draw_text(str(Balance['wood']), 160, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Balance['wood']), 160, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("Stone:", 187, 370, size=12, bold=True, color=(0, 0, 0))
    if Balance['stone'] >= 0:
        janelajogo.draw_text(str(Balance['stone']), 242, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Balance['stone']), 242, 370, size=12, bold=True, color=(236, 88, 0))

    janelajogo.draw_text("Gold:", 275, 370, size=12, bold=True, color=(0, 0, 0))
    if Balance['gold'] >= 0:
        janelajogo.draw_text(str(Balance['gold']), 325, 370, size=12, bold=True, color=(75,183,32))
    else:
        janelajogo.draw_text(str(Balance['gold']), 325, 370, size=12, bold=True, color=(236, 88, 0))



      