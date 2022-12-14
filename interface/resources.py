from interface.buildings import buildings_counter, buildings_capacity
from interface.icons import text_icon
from match import Match

def show_resources(interface):
    interface.show_resources.draw()

    
    Match.game.screen.blit(text_icon("wood",    "  {: <7d}/{: >7d}".format(Match.wood,Match.max_stock), large = True),(1090, 30))
    Match.game.screen.blit(text_icon("iron",    "  {: <7d}/{: >7d}".format(Match.iron,Match.max_stock), large = True),(1090, 65))
    Match.game.screen.blit(text_icon("soldier", "  {: <7d}/{: >7d}".format(len(Match.allies),Match.max_population), large = True),(1090, 100))
    Match.game.screen.blit(text_icon("aether",  "  {: <7d}/{: >7d}".format(Match.aether,Match.max_aether), large = True),(1090, 135))

def check_limits(interface):
    interface.resources_counter +=1
    if interface.resources_counter > 60:
        interface.resources_counter = 0
        if Match.wood > Match.max_stock:
            Match.wood = Match.max_stock
        if Match.wood < 0:
            Match.wood = 0
        
        if Match.iron > Match.max_stock:
            Match.iron = Match.max_stock
        if Match.iron < 0:
            Match.iron = 0        
       
        if Match.aether > Match.max_aether:
            Match.aether = Match.max_aether
        if Match.aether < 0:
            Match.aether = 0
        
    return interface.resources_counter