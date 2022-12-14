# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from math import sqrt
from os import path
from types import DynamicClassAttribute

import pygame
from PPlay.sprite import Sprite
from PPlay.window import Window
from camera import Camera
from effects.effectsmanager import EffectsManager
from interface.icons import text_icon
from match import Match


class SmokeDamage:
    def __init__(self, x, y, damage_type = None):
        self.duration = 1000
        self.x = x
        self.y = y

        self.animation = Sprite("assets\smoke.png", 5)   


        if damage_type == "fire":
            self.animation = Sprite("assets\\fire.png", 5)               
        elif damage_type == "poison":
            self.animation = Sprite("assets\\poison.png", 5) 
            self.duration = 500  
        elif damage_type == "ice":
            self.animation = Sprite("assets\\ice.png", 5)    


        self.animation.set_total_duration(self.duration)
        self.animation.set_position(x, y) 
        self.timer = 0        
        
    def update(self, delta_time):
        self.animation.set_position(self.x - Camera.dx, self.y - Camera.dy) 
        self.animation.update()
        self.animation.draw()
        self.timer += delta_time*1000  

class EricisFire:
    def __init__(self, cell = None):
        self.duration = 2000
        
        self.x = 0
        self.y = 0
        if cell != None:
            self.x = cell.x
            self.y = cell.y

        self.target_cell = cell

        self.animation = Sprite("assets\explosion.png", 12)        


        self.animation.set_total_duration(self.duration)
        self.animation.set_position(self.x, self.y) 
        self.timer = 0        
        
    def update(self, delta_time):
        delta_time = Match.game.gameWindow.delta_time()
        self.animation.set_position(self.x - Camera.dx, self.y - Camera.dy) 
        self.animation.update()
        self.animation.draw()
        self.timer += delta_time*1000 

        #transformar o tile
        if self.timer > 700 and self.target_cell != None:
            self.target_cell.dominion_level = 50
            self.target_cell = None
            Camera.set_shake()

class EricisBirth:
    def __init__(self, x, y, function = None):
        self.duration = 2000
        self.x = x
        self.y = y
        self.function = function

        self.animation = Sprite("assets\\birth.png", 16)     

        self.animation.set_total_duration(self.duration)
        self.animation.set_position(x, y) 
        self.timer = 0        
        
    def update(self, delta_time):
        delta_time = Match.game.gameWindow.delta_time()
        self.animation.set_position(self.x - Camera.dx, self.y - Camera.dy) 
        self.animation.update()
        self.animation.draw()
        self.timer += delta_time*1000 
        if self.timer > 1500 and self.function != None:
            self.function()  
            self.function = None

class Ericis:
    def __init__(self, x, y):
        self.duration = 500
        self.x = x
        self.y = y

        
        base_path = path.join("assets", "movables", "eri")
        self.animation = Sprite(path.join(base_path,"eridown.png"), 3)          

        self.animation.set_total_duration(self.duration)        
        self.animation.set_position(x, y) 
        self.duration = 1000000
        self.timer = 0        
        
    def update(self, delta_time):
        delta_time = Match.game.gameWindow.delta_time()
        self.animation.set_position(self.x - Camera.dx, self.y - Camera.dy) 
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
        Window.screen.blit(self.surf, (self.x - Camera.dx, self.y- Camera.dy))


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
                self.target_creature.take_damage(self.damage, "fire")
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

        self.animation.set_position(self.x- Camera.dx, self.y - Camera.dy) 
        self.animation.update()
        self.animation.draw()

class Stoneball:
    def __init__(self, x, y, target_creature):
        self.duration = 10000
        self.timer = 0
        self.animation = Sprite("assets\\stoneball.png", 1)        
        self.animation.set_total_duration(200)
        self.animation.set_position(x, y) 
        self.x = x
        self.y = y
        self.speed = 100
        self.target_creature = target_creature
        self.damage = 200
        
        
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

        self.animation.set_position(self.x- Camera.dx, self.y - Camera.dy) 
        self.animation.update()
        self.animation.draw()

class Iceball:
    def __init__(self, x, y, target_creature):
        self.duration = 10000
        self.timer = 0
        self.animation = Sprite("assets\\iceball.png", 2)        
        self.animation.set_total_duration(200)
        self.animation.set_position(x, y) 
        self.x = x
        self.y = y
        self.speed = 250
        self.target_creature = target_creature
        self.damage = 600
        
        
    def update(self, delta_time):
        tarX = self.target_creature.x
        tarY = self.target_creature.y

        #para que seja destruida
        if abs(tarX - self.x) <= 0.9:
            if abs(tarY - self.y) <= 0.9:
                self.timer = self.duration = 10000
                self.target_creature.take_damage(self.damage, "ice")
                self.target_creature.slow_down()
                return

        #move a bola de gelo
        dirX = tarX - self.x; 
        dirY = tarY - self.y; 
        dirT = sqrt(dirX*dirX + dirY*dirY)

        if dirT != 0: 
            dirX = dirX/dirT
            dirY = dirY/dirT
            self.x += dirX*delta_time*self.speed                   
            self.y += dirY*delta_time*self.speed

        self.animation.set_position(self.x- Camera.dx, self.y - Camera.dy) 
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
        self.screen.blit(self.surf, (self.owner.x - Camera.dx, self.owner.y - Camera.dy))

    def renew(self):
        #se o timer ja tiver transcorrido:
        if self.timer > self.duration:
            self.timer = 0
            self.owner.game.effects_manager.effects.append(self)
            return

        #se o timer ainda nao transcorreu
        self.timer = 0
        return


        

