import pygame
from PPlay.sprite import*

class SpriteButton():

    def __init__(self, gamewindow, func, pos = (0,0), filename = ""):
        self.mouse = gamewindow.get_mouse()                               
        self.func = func

        #controla se o botão foi pressionado
        self.cliked = False

        #cria e posiciona o sprite
        self.sprite = Sprite("assets\Buttons\\" + filename)      
        self.sprite.set_position(pos[0],pos[1])        

  
    def update(self):
        #highlight: controle para mudar cor do botão, não implementado 
        highlight = False
        if self.mouse.is_over_object(self.sprite):
            highlight = True            
            if self.mouse.is_button_pressed(True):
                if not self.cliked:                    
                    self.cliked = True
            #a ação ocorre ao soltar o botão, evitando erros
            elif self.cliked:
                #executa a função apontada na criação do botão
                self.func()
                self.cliked = False
        else:
            highlight = False            
            self.cliked = False

        #desenha o botão
        #surf = self.sprite if not highlight else self.sprite
        self.sprite.draw()
        

            


