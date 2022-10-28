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
        self.wait_timer = 1
        self.wait_time = 1

    def update(self, delta_time):
        self.wait_timer += delta_time
        #verifica o tempo parado
        if self.wait_timer < self.wait_time:
            return
        self.wait_timer = 0

        #tentar atacar
        attakable_cell_target = self.creature.get_attackable_target()
        if attakable_cell_target != None:                
            self.creature.state = AtkState(self.creature, attakable_cell_target)
            return
        
        #tentar pegar novo caminho                        
        if len(self.creature.path) != 0:            
            self.creature.state = WalkingState(self.creature)
            return 
        
        #se nao tem caminho, solicita um novo, se possivel     
        if pathfinder.creatures_needing_path.count(self.creature) == 0:
            pathfinder.creatures_needing_path.append(self.creature)


class WalkingState:
    def __init__(self, creature: "Creature") -> None:        
        self.creature = creature        

    def get_next_target(self) -> bool:
        #seleciona um novo no/alvo caminho                    
        if len(self.creature.path) != 0:
            self.creature.target_uv = self.creature.path.pop()

            #verifica se o novo caminho é possivel
            next_cell = self.creature.game.world.cells[self.creature.target_uv[1]][self.creature.target_uv[0]]
            if not next_cell.vacant:
                #caso nao seja, exclui o caminho e o no                
                self.creature.target_uv = None
                self.creature.path.clear()
                return False

            return True
        else:
            return False

    def update(self, delta_time):
        #verifica se tem um alvo
        if self.creature.target_uv == None:
            #tentar pegar novo caminho, se não conseguir, verifica transição  
            if not self.get_next_target():
                self.verify_transition()
                return

        tarX = self.creature.target_uv[0]*Settings.tilesize
        tarY = self.creature.target_uv[1]*Settings.tilesize

        #verificar se chegou
        if abs(tarX - self.creature.x) <= 0.9:
            if abs(tarY - self.creature.y) <= 0.9:
                self.creature.x = tarX
                self.creature.y = tarY
                self.creature.target_uv = None
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
            #tentar atacar
            attakable_target = self.creature.get_attackable_target()
            if attakable_target != None:                
                self.creature.state = AtkState(self.creature, attakable_target)
                return

            #se falhar, ficar idle
            self.creature.state = IdleState(self.creature)
            return
            


class AtkState:
    def __init__(self, creature : "Creature", attakable_target) -> None:        
        self.creature = creature
        self.atktarget = attakable_target
        self.timer = 2.0
        self.atkinterval = 2.0

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer < self.atkinterval:
            return
            
        #verificar se possivel atacar
        if self.creature.is_enemy:
            building = self.atktarget.building
            if building != None:
                if building.integrity > 0:
                    self.timer = 0
                    building.integrity -= self.creature.damage
                    print("damage")
                    self.creature.game.effects_manager.effects.append(SmokeDamage(
                        self.atktarget.x, self.atktarget.y))
                    return
        #a criatura é aliada  e buscará atacar um inimigo
        else:
            enemy = self.atktarget.creature
            if enemy != None:
                if enemy.is_enemy and enemy.is_dead == False:
                    self.timer = 0
                    enemy.take_damage(self.creature.damage)
                    return
        
        #se falhar, ficar idle 
        self.creature.state = IdleState(self.creature)        