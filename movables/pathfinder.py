# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from world import World


#modulo que gerencia o pathfinding
creatures_needing_path = []
grid : Grid = None
worldref = World()

def update(delta_time):   
    for creature in creatures_needing_path:
        generate_path(creature)
        creatures_needing_path.remove(creature)


def generate_path(creature):      

    goal = grid.node(10, 10)
    origin = grid.node(creature.u, creature.v)
    if not (creature.u == goal.x and creature.v == goal.y):
        update_grid()
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