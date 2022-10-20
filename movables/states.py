# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import sqrt
from effects.effects import SmokeDamage
from settings import Settings
import movables.pathfinder as pathfinder

import typing

if typing.TYPE_CHECKING:
    from movables.creatures import Creature

class IdleState:
    def __init__(self, creature : "Creature") -> None:        
        self.creature = creature

    def update(self, delta_time):
        #tentar atacar
        attakable_target = self.creature.get_attackable_target()
        if attakable_target != None:                
            self.creature.state = AtkState(self.creature, attakable_target)
        
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
                self.creature.state = AtkState(self.creature, attakable_target)


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

class AtkState:
    def __init__(self, creature : "Creature", attakable_target) -> None:        
        self.creature = creature
        self.atktarget = attakable_target
        self.timer = 2.0
        self.atkinterval = 2.0

    def update(self, delta_time):
        #check attack
        building = self.creature.game.world.cells[self.atktarget[0]][self.atktarget[1]].building
        if building != None:
            if building.integrity > 0:
                self.timer += delta_time
                if self.timer >= self.atkinterval:
                    self.timer = 0
                    building.integrity -= self.creature.damage
                    print("damage")
                    self.creature.game.effects_manager.effects.append(SmokeDamage(
                        self.atktarget[1]*Settings.tilesize, self.atktarget[0]*Settings.tilesize))
                return



        
        #se falhar, ficar idle e avisar ao pathfinder
        self.creature.state = IdleState(self.creature)
        pathfinder.creatures_needing_path.append(self.creature)