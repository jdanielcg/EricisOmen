from PPlay.window import*
from PPlay.sprite import*


import interface.resources as resources
import interface.research as research
import interface.reports as reports




class Interface:
    def __init__(self,window):
        #dimensões
        self.janela_largura = 1280
        self.janela_altura = 720

        #janela
        self.window = window


        #pegando a entrada do usuário
        self.clickjogo = self.window.get_mouse()
        self.teclado = self.window.get_keyboard()

        #titulo
        self.titulo = Sprite("assets\Titulo.png")
        self.titulo.set_position(1280/2 - 280, 50)

        #botao play
        self.play = Sprite("assets\Buttons\play.png")
        self.play.set_position(1280/2 - 120, 250)

        #botao settings
        self.settings = Sprite("assets\Buttons\settings.png")
        self.settings.set_position(1280/2 - 120, 350)

        #botao exit
        self.exit = Sprite("assets\Buttons\exit.png")
        self.exit.set_position(1280/2 - 120 , 450)

        #botao help
        self.help = Sprite("assets\Buttons\help.png")
        self.help.set_position(1260 - 70 , 630)

        #botao music
        self.music = Sprite("assets\Buttons\music.png")
        self.music.set_position(1260 - 150, 630)

        #botao quit
        self.quit = Sprite("assets\Buttons\quit.png")
        self.quit.set_position(1280/2 - 120, 570)

        #creditos
        self.creditos = Sprite("assets\creditos.png")
        self.creditos.set_position(1280/2 - 280 , 550)

        #portal level
        self.portal_level_counter = 1
        self.portal_level_percent = 0

        #-> jogo
        #botao menu jogo
        self.menu_jogo = Sprite("assets\Buttons\menu_jogo.png")
        self.menu_jogo.set_position(12,12)
        self.exibir_menu_jogo = False
        #barra botoes jogo
        self.barra_botoes_jogo = Sprite("assets\Buttons\Barra_botoes_jogo.png")
        self.barra_botoes_jogo.set_position(self.janela_largura/2 - 340,7)
        self.p_barra_botoes_jogo = True
        #portal level
        self.portal_level = Sprite("assets\Buttons\portal_level.png")
        self.portal_level.set_position(self.janela_largura/2 + 450, 12)
        #botao jogo construct
        self.botao_jogo_construct = Sprite("assets\Buttons\Botao_jogo_construct.png")
        self.botao_jogo_construct.set_position(self.janela_largura/2 - 265, 20)
        self.p_construct = True
        self.exibir_menu_construct = False
        #botao jogo resources
        self.show_resources = Sprite("assets\Buttons\show_resources.png")
        self.show_resources.set_position(1070, 130)
        self.botao_jogo_resources = Sprite("assets\Buttons\Botao_jogo_resources.png")
        self.botao_jogo_resources.set_position(self.janela_largura/2 - 165, 20)
        self.p_resources = True
        self.resources_counter = 0
        self.exibir_menu_resources = False

        #botao jogo research
            #controle de pesquisa
        self.pt, self.pt_end = False, False
        self.ds, self.ds_end = False, False
        self.hp, self.hp_end = False, False
        self.es, self.es_end = False, False
        self.gate = False
        self.lock_pt, self.lock_ds, self.lock_hp, self.lock_es = False, False, False, False
            #fim
            #exibição de janelas
        self.exibir_menu_research_pack_tactics = False
        self.exibir_menu_research_double_saw = False
        self.exibir_menu_research_hardened_picks = False
        self.exibir_menu_research_eficient_smelting = False
            #fim
        self.botao_jogo_research = Sprite("assets\Buttons\Botao_jogo_research.png")
        self.botao_jogo_research.set_position(self.janela_largura/2 - 65, 20)
        self.p_research = True
        self.research_in_progress = False
        self.timer = 0
        self.exibir_menu_research = False
        #-> botao taticas de matilha
        self.taticas_de_matilha = Sprite("assets\Buttons\Taticas_de_matilha.png")
        self.taticas_de_matilha.set_position(25, self.janela_altura/2 - 165)
        #-> botao serrote duplo
        self.serrote_duplo = Sprite("assets\Buttons\Serrote_duplo.png")
        self.serrote_duplo.set_position(190, self.janela_altura/2 - 165)
        #-> botao hardened picks
        self.hardened_picks = Sprite("assets\Buttons\Hardened_picks.png")
        self.hardened_picks.set_position(25, self.janela_altura/2 - 110)
        #-> botao eficient smelting
        self.eficient_smelting = Sprite("assets\Buttons\Eficient_smelting.png")
        self.eficient_smelting.set_position(190, self.janela_altura/2 - 110)
        #--> botao in progress
        self.in_progress = Sprite("assets\Buttons\Research_in_progress.png")
        self.in_progress.set_position(self.janela_largura/2 + 120, self.janela_altura/2 + 230)
        #-->botao already researched
        self.research_done = Sprite("assets\Buttons\Research_done.png")
        #-> Research bar
        self.research_bar_idle = Sprite("assets\Buttons\Research_bar_1.png")
        self.research_bar_2 = Sprite("assets\Buttons\Research_bar_2.png")
        self.research_bar_3 = Sprite("assets\Buttons\Research_bar_3.png")
        self.research_bar_4 = Sprite("assets\Buttons\Research_bar_4.png")
        self.research_bar_idle.set_position(30, 230)
        self.research_bar_2.set_position(30, 230)
        self.research_bar_3.set_position(30, 230)
        self.research_bar_4.set_position(30, 230)

        #-> Research bar small
        self.research_bar_idle_small = Sprite("assets\Buttons\Research_bar_idle_small.png")
        self.research_bar_2_small = Sprite("assets\Buttons\Research_bar_2_small.png")
        self.research_bar_3_small = Sprite("assets\Buttons\Research_bar_3_small.png")
        self.research_bar_4_small = Sprite("assets\Buttons\Research_bar_4_small.png")
        self.research_bar_idle_small.set_position(1090, 300)
        self.research_bar_2_small.set_position(1090, 300)
        self.research_bar_3_small.set_position(1090, 300)
        self.research_bar_4_small.set_position(1090, 300)

        #botao jogo reports
        self.botao_jogo_reports = Sprite("assets\Buttons\Botao_jogo_reports.png")
        self.botao_jogo_reports.set_position(self.janela_largura/2 + 35, 20)
        self.p_reports = True
        self.exibir_menu_reports = False
        #botao jogo options
        self.botao_jogo_options = Sprite("assets\Buttons\Botao_jogo_options.png")
        self.botao_jogo_options.set_position(self.janela_largura/2 + 135, 20)
        self.p_options = True
        self.exibir_menu_options = False
        #botao jogo close
        self.botao_jogo_close = Sprite("assets\Buttons\Botao_close.png")
        self.botao_jogo_close.set_position(140, self.janela_altura/2 - 210)
        #botao jogo close amarelo
        self.botao_jogo_close_amarelo = Sprite("assets\Buttons\Botao_close.png")
        self.botao_jogo_close_amarelo.set_position(self.janela_largura/2 - 190, self.janela_altura/2 + 236)
        #barra botoes2 jogo
        self.barra_botoes2_jogo = Sprite("assets\Buttons\Barra_botoes2_jogo.png")
        self.barra_botoes2_jogo.set_position(20,self.janela_altura/2 - 220)
        self.p_barra_botoes2_jogo = True
        #barra background cost menu
        self.background_cost_menu = Sprite("assets\Buttons\Background_cost_menu.png")
        self.background_cost_menu.set_position(self.janela_largura/2 - self.background_cost_menu.width/2 + 40, self.janela_altura/2 - self.background_cost_menu.height/2 + 40)
        #botao next
        self.botao_next = Sprite("assets\Buttons\Botao_next.png")
        self.botao_next.set_position(self.janela_largura/2 + 120, self.janela_altura/2 + 230)
        
    def update(self,delta_time):
        self.menu_jogo.draw()
        self.portal_level.draw()

        #barra direita:
        resources.show_resources(self)
        research.show_research_blank(self)
        research.research_informations_small(self)
        
        #progressão de pesquisa:
        research.researching(self)


        #atualização dos recursos:
        self.resources_counter = resources.change_resources(resources.resources,resources.Balance, self.resources_counter)

            #escrever as coisas dentro do visor portal level
        self.window.draw_text("Portal Level: ", self.janela_largura/2 + 470, 23, size=20, bold=True, color=(0, 0, 0))
        self.window.draw_text(str(self.portal_level_counter), self.janela_largura/2 + 595, 23.5, size=20, bold=True, color=(0, 0, 0))
        self.window.draw_text(str(self.portal_level_percent), self.janela_largura/2 + 482, 47, size=17, bold=True, color=(0, 0, 0))
        self.window.draw_text("% Chance of", self.janela_largura/2 + 493, 48, size=17, bold=True, color=(0, 0, 0))
        self.window.draw_text("spawning Ericis", self.janela_largura/2 + 474, 68, size=17, bold=True, color=(0, 0, 0))
            #fim


        
        if self.clickjogo.is_over_object(self.menu_jogo) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_jogo = True
        if self.exibir_menu_jogo:
            #fechar o menu azul
            if self.teclado.key_pressed("ESC"):
                self.exibir_menu_jogo = False
                
            self.barra_botoes_jogo.draw()
            self.botao_jogo_construct.draw()
            self.botao_jogo_resources.draw()
            self.botao_jogo_research.draw()
            self.botao_jogo_reports.draw()
            self.botao_jogo_options.draw()

            

        #menu construct
        if self.clickjogo.is_over_object(self.botao_jogo_construct) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_construct = True
        if self.exibir_menu_construct:               
            self.barra_botoes2_jogo.draw()
            
            #fechar o menu construct
            self.botao_jogo_close.draw()
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_construct = False
            #fim

        #menu resources
        if self.clickjogo.is_over_object(self.botao_jogo_resources) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_resources = True
        if self.exibir_menu_resources:
            self.barra_botoes2_jogo.draw()
            self.botao_jogo_close.draw()

            #resources
            resources.stocked(self.window)
            resources.input(self.window)
            resources.output(self.window)
            resources.balance(self.window)
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_resources = False

        #menu research
        if self.clickjogo.is_over_object(self.botao_jogo_research) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_research = True
        if self.exibir_menu_research:

            #desenhar o menu vermelho:
            research.desenhar_menu_vermelho(self)


            #inicializar uma pesquisa (NÃO É A PROGResSÃO DA PesQUISA):
            #taticas de matilha:
            if self.clickjogo.is_over_object(self.taticas_de_matilha):
                research.popout(self, 'Pack Tactics')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_research_pack_tactics = True
            if self.exibir_menu_research_pack_tactics:
                research.popout_perma(self,'Pack Tactics')  
                


            #serrote duplo:
            if self.clickjogo.is_over_object(self.serrote_duplo):
                research.popout(self,'Double Saw')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_research_double_saw = True
            if self.exibir_menu_research_double_saw:
                research.popout_perma(self,'Double Saw')

            #hardened picks:
            if self.clickjogo.is_over_object(self.hardened_picks):
                research.popout(self,'Hardened Picks')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_research_hardened_picks = True
            if self.exibir_menu_research_hardened_picks:
                research.popout_perma(self,'Hardened Picks')

            #Eficient Smelting:
            if self.clickjogo.is_over_object(self.eficient_smelting):
                research.popout(self,'Eficient Smelting')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_research_eficient_smelting = True
            if self.exibir_menu_research_eficient_smelting:
                research.popout_perma(self,'Eficient Smelting')
            
            #fechar
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_research = False
                    

        #menu reports
        if self.clickjogo.is_over_object(self.botao_jogo_reports) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_reports = True
        if self.exibir_menu_reports:
            reports.redesenhar_menu_vermelho(self.barra_botoes2_jogo,self.botao_jogo_close)

            #research
            reports.research_informations(self)

            #fechar                                  
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_reports = False

                
        #menu options
        if self.clickjogo.is_over_object(self.botao_jogo_options) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_options = True
        if self.exibir_menu_options:              
            self.barra_botoes2_jogo.draw()
            self.botao_jogo_close.draw()

        #fechar                                  
        if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_options = False