
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
            return 7
        if not ur:
            return 9
        if not dl:
            return 27
        if not dr:
            return 29
        else:
            return 33
    #casos de 3 lados
    elif up and left and down:
        return 39
    elif up and right and down:
        return 34
    elif left and right and up:
        return 37
    elif left and right and down:
        return 36
    #casos de 2 lados
    elif up and left:
        return 22
    elif up and right:
        return 20
    elif down and right:
        return 0
    elif down and left:
        return 2
    elif down and up:
        return 13
    elif left and right:
        return 31
    #casos de 1 lados 
    elif left:
        return 32
    elif right:
        return 30
    elif up:
        return 23
    elif down:
        return 3
    else:
        return 33