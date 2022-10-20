# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                        RAMON SANTOS         ║ 
# ╚═════════════════════════════════════════════╝

from pygame import Vector2
from PPlay.sprite import *



class CharAnimationController:

    def __init__(self, creature):        
        self.creature = creature
        

        #cima
        self.walking_up = Sprite("assets\movables\Kobold\wup.png", 9)
        self.up_idle = Sprite("assets\movables\Kobold\\up.png")
        self.walking_up.set_total_duration(1000)
        self.up_idle.set_total_duration(1000)

        #baixo
        self.walking_down = Sprite("assets\movables\Kobold\wdown.png", 9)
        self.down_idle = Sprite("assets\movables\Kobold\down.png")        
        self.walking_down.set_total_duration(1000)
        self.down_idle.set_total_duration(1000)

        #esquerda
        self.walking_left = Sprite("assets\movables\Kobold\wleft.png", 9)
        self.left_idle = Sprite("assets\movables\Kobold\left.png")
        self.walking_left.set_total_duration(1000)
        self.left_idle.set_total_duration(1000)

        #direita
        self.walking_right = Sprite("assets\movables\Kobold\wright.png", 9)
        self.right_idle = Sprite("assets\movables\Kobold\\right.png")
        self.walking_right.set_total_duration(1000)
        self.right_idle.set_total_duration(1000)

        #morto               
        self.dead = Sprite("assets\movables\Kobold\dead.png")       
        self.dead.set_total_duration(1000)
        self.is_dead = False

        #começo
        self.current_sprite = self.down_idle
        self.direction = [0,0]
        self.last_direction = [0,0]
        
    #usada para controlar a direção do movimento
    def set_dir(self,vec):
        self.direction = vec

    def set_dead(self):
        self.is_dead = True
        self.current_sprite = self.dead        
        
    def update(self, delta_time):              
        
        if not self.is_dead:
            if self.direction[1] < 0:
                self.current_sprite = self.walking_up
            elif self.direction[1] > 0:
                self.current_sprite = self.walking_down
            elif self.direction[0] < 0:
                self.current_sprite = self.walking_left
            elif self.direction[0] > 0:
                self.current_sprite = self.walking_right
            else:
                #o personagem está parado
                #vamos escolher a direção idle com base na ultima direção
                if self.last_direction[1] < 0:
                    self.current_sprite = self.up_idle
                elif self.last_direction[1] > 0:
                    self.current_sprite = self.down_idle
                elif self.last_direction[0] < 0:
                    self.current_sprite = self.left_idle
                elif self.last_direction[0] > 0:
                    self.current_sprite = self.right_idle
                else:
                    self.current_sprite = self.down_idle

            #atualiza a "ultima" direção se a atual for diferente de 0
            if abs(self.direction[0]) + abs(self.direction[1]) > 0.5:
                self.last_direction[0] = self.direction[0]
                self.last_direction[1] = self.direction[1]

            self.direction[0] = 0
            self.direction[1] = 0

        self.current_sprite.set_position(self.creature.x, self.creature.y) 
        self.current_sprite.update()
        self.current_sprite.draw()