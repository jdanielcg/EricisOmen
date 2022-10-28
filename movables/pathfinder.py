# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import dist
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from settings import Settings

from world import World


#modulo que gerencia o pathfinding
creatures_needing_path = []
grid : Grid = None
worldref = World()
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

def update(delta_time):   
    if len(creatures_needing_path) > 0:
        skipped = 0
        generated = 0
        
        creature = creatures_needing_path.pop(0)           
            
        if worldref.cells[creature.v][creature.u].walkable == False:
            skipped +=1
        else:
            generated +=1
            generate_path(creature)            
        
        #print("path requests: ", len(creatures_needing_path),"skipped (stuck):", skipped, "generated paths: ", generated)              
        

def closest_goal(creature) -> Node:
    if len(creature.game.world.attack_possible_positions) == None:
        return None
    
    dist_closest = 100000000
    dist_from = 0
    closest = None

    for cell in creature.game.world.attack_possible_positions:
        dist_from = dist(cell.location, (creature.u, creature.v))
        if dist_from < dist_closest:
            dist_closest = dist_from
            closest = cell.node

    return closest

def generate_path(creature):   
    origin = grid.node(creature.u, creature.v)
    goal = closest_goal(creature)
    if goal == None:
        return


    #marca o no atual da criatura como andavel
    old_status = grid.node(creature.u, creature.v).walkable
    grid.node(creature.u, creature.v).walkable = True

    if not (creature.u == goal.x and creature.v == goal.y):       
        grid.cleanup()        
        path, runs = finder.find_path(origin, goal, grid)
        path.reverse()
        if len(path) == 0:
            print("pathfinding didn't find a path")
        else:
            path.pop()
        creature.path = path

    #restaura o status anterior do no
    grid.node(creature.u, creature.v).walkable = old_status
    
    #print('operations:', runs, 'path length:', len(path))
    
def generate_grid():
    gridmap = []
    for n in range(len(worldref.cells[0])):
        line = []
        for m in range(len(worldref.cells[0])):
            line.append(0)
        gridmap.append(line)    
    return Grid(len(worldref.cells[0]), len(worldref.cells[0]), gridmap)  

def bind_nodes_to_cells():        
    for u in range(grid.width):
        for v in range(grid.height):
            worldref.cells[v][u].node = grid.node(u,v)

def setup(world):
    global worldref, grid
    worldref = world
    grid = generate_grid()
    bind_nodes_to_cells()