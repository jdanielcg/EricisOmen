# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from settings import Settings

from world import World


#modulo que gerencia o pathfinding
creatures_needing_path = []
grid : Grid = None
worldref = World()

def update(delta_time):   
    if len(creatures_needing_path) > 0:
        skipped = 0
        generated = 0
        iteration = 0
        creature = None
        update_grid()        
        for creature in creatures_needing_path:            
            if worldref.cells[creature.v][creature.u].walkable == False:
                skipped +=1
            else:
                generated +=1
                generate_path(creature)            
            iteration += 1
        #print("path requests: ", len(creatures_needing_path),
        #    "skipped (stuck):", skipped, "generated paths: ", generated, " iterations : ", iteration)        
        creatures_needing_path.clear()




def generate_path(creature):      

    goal = grid.node(Settings.breach_center[0], Settings.breach_center[1] -1)
    origin = grid.node(creature.u, creature.v)
    if not (creature.u == goal.x and creature.v == goal.y):        
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(goal, origin, grid)
        creature.path = path
        grid.cleanup()
    
    #print('operations:', runs, 'path length:', len(path))
    
def generate_grid():
    gridmap = []
    for n in range(len(worldref.cells[0])):
        line = []
        for m in range(len(worldref.cells[0])):
            line.append(0)
        gridmap.append(line)    
    return Grid(len(worldref.cells[0]), len(worldref.cells[0]), gridmap)  

def update_grid():
    walkable = True
    for w in range(grid.width):
        for h in range(grid.height):
            walkable = False
            if worldref.cells[h][w].walkable:
                walkable = True
            grid.node(w,h).walkable = walkable


def setup(world):
    global worldref, grid
    worldref = world
    grid = generate_grid()