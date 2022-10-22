# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import sqrt

import pygame
from PPlay.sprite import Sprite
from PPlay.window import Window
from effects.effectsmanager import EffectsManager
from interface.icons import text_icon


class SmokeDamage:
    def __init__(self, x, y):
        self.duration = 1000
        self.animation = Sprite("assets\smoke.png", 5)        
        self.animation.set_total_duration(self.duration)
        self.animation.set_position(x, y) 
        self.timer = 0
        
        
    def update(self, delta_time):
        self.animation.update()
        self.animation.draw()
        self.timer += delta_time*1000   

class FloatingIconText:
    def __init__(self, x, y,  icon, text):
        self.duration = 2000
        self.surf  = text_icon(icon, text, (0, 230,20))
        self.timer = 0
        self.speed = 30
        self.x = x
        self.y = y
        
        
    def update(self, delta_time):
        self.timer += delta_time*1000 
        self.y -= delta_time*self.speed  
        Window.screen.blit(self.surf, (self.x, self.y))


class Fireball:
    def __init__(self, x, y, target_creature):
        self.duration = 10000
        self.timer = 0
        self.animation = Sprite("assets\\fireball.png", 2)        
        self.animation.set_total_duration(200)
        self.animation.set_position(x, y) 
        self.x = x
        self.y = y
        self.speed = 150
        self.target_creature = target_creature
        self.damage = 400
        
        
    def update(self, delta_time):
        tarX = self.target_creature.x
        tarY = self.target_creature.y

        #para que seja destruida
        if abs(tarX - self.x) <= 0.9:
            if abs(tarY - self.y) <= 0.9:
                self.timer = self.duration = 10000
                self.target_creature.take_damage(self.damage)
                return

        #move a bola de fogo
        dirX = tarX - self.x; 
        dirY = tarY - self.y; 
        dirT = sqrt(dirX*dirX + dirY*dirY)

        if dirT != 0: 
            dirX = dirX/dirT
            dirY = dirY/dirT
            self.x += dirX*delta_time*self.speed                   
            self.y += dirY*delta_time*self.speed

        self.animation.set_position(self.x, self.y) 
        self.animation.update()
        self.animation.draw()

class Lifebar:

    #gera um unico background a ser usado por todas as barras
    background = None
    def __init__(self, owner):        
        self.owner = owner
        self.max = owner.max_integrity
        self.surf = pygame.Surface([32, 8])
        self.screen = self.owner.game.gameWindow.get_screen()
        self.duration = 2000
        self.timer = 0

        if Lifebar.background == None:
            Lifebar.background = pygame.Surface([32, 6])
            Lifebar.background.fill((125,0,75))

    def update(self, delta_time):       

        self.timer += delta_time*1000   

        factor = self.owner.integrity/self.max

        self.surf.blit(Lifebar.background, [0,0])
        
        pygame.draw.rect(self.surf, (0, 200, 50), (1, 1, round(28*factor), 4),)
        self.screen.blit(self.surf, (self.owner.x, self.owner.y))

    def renew(self):
        #se o timer ja tiver transcorrido:
        if self.timer > self.duration:
            self.timer = 0
            self.owner.game.effects_manager.effects.append(self)
            return

        #se o timer ainda nao transcorreu
        self.timer = 0
        return


        

