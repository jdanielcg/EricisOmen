# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from settings import Settings


def border_maker(cell, world):
    u = cell.u
    v = cell.v
    left =  can_be_dominated(world.cells[v][u-1])
    right = can_be_dominated(world.cells[v][u+1])
    up =    can_be_dominated(world.cells[v-1][u])
    down =  can_be_dominated(world.cells[v+1][u])

    ul =    can_be_dominated(world.cells[v-1][u-1])
    ur =    can_be_dominated(world.cells[v-1][u+1])
    dl =    can_be_dominated(world.cells[v+1][u-1])
    dr =    can_be_dominated(world.cells[v+1][u+1])

    if  left and right and up and down:
        if not ul:
            return 167
        if not ur:
            return 166
        if not dl:
            return 146
        if not dr:
            return 145
        else:
            return 208
    #casos de 3 lados
    elif up and left and down:
        return 209
    elif up and right and down:
        return 207
    elif left and right and up:
        return 229
    elif left and right and down:
        return 187
    #casos de 2 lados
    elif up and left:
        return 230
    elif up and right:
        return 228
    elif down and right:
        return 186
    elif down and left:
        return 188
    #ignorando casos de 1 lados 
    else:
        return 208


def can_be_dominated(cell):
    return ((cell.tile_code == 0 or cell.tile_code == 1 or cell.tile_code == 2 or
            cell.tile_code == 3 or cell.tile_code == 4 or cell.tile_code == 5) and (
            cell.dominion_level > Settings.dominion_threshold))
