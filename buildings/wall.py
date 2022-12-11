
def is_wall(cell):
    if cell == None:
        return False
    if cell.building == None:
        return False
    if cell.building.info.name != "wall":
        return False
    return True    

        
def wall_side_checker(cell, world):
    u = cell.u
    v = cell.v
    left =  is_wall(world.cells[v][u-1])
    right = is_wall(world.cells[v][u+1])
    up =    is_wall(world.cells[v-1][u])
    down =  is_wall(world.cells[v+1][u])
    ul =    is_wall(world.cells[v-1][u-1])
    ur =    is_wall(world.cells[v-1][u+1])
    dl =    is_wall(world.cells[v+1][u-1])
    dr =    is_wall(world.cells[v+1][u+1])

    if  left and right and up and down:
        if not ul:
            return 24
        if not ur:
            return 24
        if not dl:
            return 24
        if not dr:
            return 24
        else:
            return 24
    #casos de 3 lados
    elif up and left and down:
        return 24
    elif up and right and down:
        return 24
    elif left and right and up:
        return 24
    elif left and right and down:
        return 24
    #casos de 2 lados
    elif up and left:
        return 16
    elif up and right:
        return 14
    elif down and right:
        return 0
    elif down and left:
        return 2
    elif down and up:
        return 10
    elif left and right:
        return 22
    #casos de 1 lados 
    elif left:
        return 23
    elif right:
        return 21
    elif up:
        return 17
    elif down:
        return 3
    else:
        return 24