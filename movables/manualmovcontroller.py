from pygame import Vector2 
import pygame

class ManualMovController:
    def __init__(self, gamewindow, animation_controller):
        self.animation_cotroller = animation_controller
        self.gamewindow = gamewindow
        self.direction = Vector2(0,0)
        self.keyboard = gamewindow.get_keyboard()

    def update(self, delta_time):        

        self.direction.x = 0
        self.direction.y = 0
        
        #para fazer o boneco se movimentar
        if self.keyboard.key_pressed("W"):
            self.direction.y = -1            
        elif self.keyboard.key_pressed("S"):
            self.direction.y = 1            
        elif self.keyboard.key_pressed("D"):
            self.direction.x = 1            
        elif self.keyboard.key_pressed("A"):
            self.direction.x = -1

        self.animation_cotroller.direction = Vector2(self.direction.x, self.direction.y)
        self.animation_cotroller.update(delta_time)
    
    

            
        

