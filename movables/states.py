from math import sqrt
#from movables.creatures import Creature
from settings import Settings
import movables.pathfinder as pathfinder

import typing

if typing.TYPE_CHECKING:
    from movables.creatures import Creature

class IdleState:
    def __init__(self, creature : "Creature") -> None:        
        self.creature = creature

    def update(self, delta_time):
        #check attack
        
        #tentar pegar novo caminho                        
        if len(self.creature.path) != 0:            
            self.creature.state = WalkingState(self.creature)
            return 
        
        pathfinder.creatures_needing_path.append(self.creature)


class WalkingState:
    def __init__(self, creature: "Creature") -> None:        
        self.creature = creature
        self.targetUV = None

    def update(self, delta_time):
        if (self.verify_transition()) : return

        tarX = self.targetUV[0]*Settings.tilesize
        tarY = self.targetUV[1]*Settings.tilesize

        #verificar se chegou
        if abs(tarX - self.creature.x) <= 0.9:
            if abs(tarY - self.creature.y) <= 0.9:
                self.creature.x = tarX
                self.creature.y = tarY
                if len(self.creature.path) == 0:
                    self.targetUV = None
                else:
                    self.targetUV = self.creature.path.pop()
                return

        #calcular direção
        dirX = tarX - self.creature.x; 
        dirY = tarY - self.creature.y; 
        dirT = sqrt(dirX*dirX + dirY*dirY)
        if dirT == 0: return
        dirX = dirX/dirT
        dirY = dirY/dirT

        #movimentar
        if abs(dirX) == 1:
            self.creature.x += dirX*delta_time*self.creature.speed
        elif abs(dirY) == 1:
            self.creature.y += dirY*delta_time*self.creature.speed

        #atualiza o animation controller
        self.creature.anim_controller.set_dir([dirX, dirY])

        #movement print debug
        #print(dirX*delta_time*self.creature.speed, "   ", dirY*delta_time*self.creature.speed, "   ",
        #int(self.creature.x), "    ", int(self.creature.y))

            
    def verify_transition(self):
        if self.targetUV == None:
            #tentar atacar
            attakable_target = self.creature.get_attackable_target()
            if attakable_target != None:                
                return True


            #tentar pegar novo caminho                        
            if len(self.creature.path) != 0:
                self.targetUV = self.creature.path.pop()
                return True

            #se falhar, ficar idle e avisar ao pathfinder
            self.creature.state = IdleState(self.creature)
            pathfinder.creatures_needing_path.append(self.creature)
            return True
            
        else:
            return False