# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from pygame import Surface
from PPlay.sprite import*

class TextButton:
    font = None

    def __init__(self, gamewindow, func, pos = (0,0), text = ""):
        self.mouse = gamewindow.get_mouse()                               
        self.func = func
        self.pos = pos
        self.screen = gamewindow.get_screen()
        self.highlight = False

        #inicializa a fonte
        if TextButton.font == None:
            TextButton.font = pygame.font.SysFont("bahnschrift semibold", 20, False, False)

        #cria a surface com o texto escrito
        font_surface = TextButton.font.render(text, True, (255,240,255))

        
        font_rect = font_surface.get_rect()       
        self.back_surf = Surface([font_rect.width + 10, font_rect.height+10])
        self.back_surf_high = Surface([font_rect.width + 10, font_rect.height+10])
        self.back_surf.fill((100,0 ,70))
        self.back_surf_high.fill((200,100,170))
        self.back_surf.blit(font_surface, [5,5])
        self.back_surf_high.blit(font_surface, [5,5])

        self.x = pos[0]
        self.y = pos[1]
        self.width = self.back_surf.get_rect().width
        self.height = self.back_surf.get_rect().height

        #controla se o botão foi pressionado
        self.cliked = False    

  
    def update(self):
        #highlight: controle para mudar cor do botão, não implementado 
        self.highlight = False
        if self.mouse.is_over_object(self):
            self.highlight = True            
            if self.mouse.is_button_pressed(True):
                if not self.cliked:                    
                    self.cliked = True
            #a ação ocorre ao soltar o botão, evitando erros
            elif self.cliked:
                #executa a função apontada na criação do botão
                self.func()
                self.cliked = False
        else:
            self.highlight = False            
            self.cliked = False

        #desenha o botão
        self.screen.blit(self.back_surf if not self.highlight else self.back_surf_high, self.pos)
        

            


