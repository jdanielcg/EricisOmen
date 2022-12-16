# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: RAMON SANTOS         ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from PPlay.window import*
from PPlay.sprite import*
from interface.icons import text_icon
from settings import Settings


import interface.resources as resources
import interface.research as research
import interface.reports as reports
import interface.buildings as buildings
import interface.options as options

from match import Match

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


        #-> jogo
        #moldura botoes
        self.moldura_botoes = Sprite("assets\Buttons\moldura_botoes.png")
        self.moldura_botoes.set_position(7,9)
        self.p_barra_botoes_jogo = True

        #breach bar frame
        self.breach_bar_frame = Sprite("assets\Buttons\Breach_bar_frame.png")
        self.breach_bar_frame.set_position(245,653.5)
        #minimap frame
        self.minimap_frame = Sprite("assets\Buttons\Minimap_frame.png")
        self.minimap_frame.set_position(1057,500)

        #->botao jogo construct
        self.botao_jogo_construct = Sprite("assets\Buttons\Botao_jogo_construct.png")
        self.botao_jogo_construct.set_position(20, 21)
        self.p_construct = True
        self.exibir_menu_construct = False
        #botao construct menu
        self.botao_construct_direita = Sprite("assets\Buttons\Botao_construct_direita.png")
        self.botao_construct_direita.set_position(110, 217)
        self.botao_construct_esquerda = Sprite("assets\Buttons\Botao_construct_esquerda.png")
        self.botao_construct_esquerda.set_position(40, 217)
        self.botao_demolish = Sprite("assets\Buttons\Botao_demolish.png")
        self.botao_demolish.set_position(50,590)
        #exibição de janelas
        self.construct_page = 1
        self.exibir_menu_construct_barracks = False
        self.exibir_menu_construct_warehouse = False
        self.exibir_menu_construct_fire_tower = False
        self.exibir_menu_construct_frost_tower = False
        self.exibir_menu_construct_rock_tower = False
        self.exibir_menu_construct_poison_trap = False
        self.exibir_menu_construct_fire_trap = False
        self.exibir_menu_construct_wall = False
        self.exibir_menu_construct_obelisk = False
        self.exibir_menu_construct_mining_camp = False
        self.exibir_menu_construct_woodcamp = False
        #botao barracks
        self.botao_barracks = Sprite("assets\Buttons\Botao_barracks.png")
        self.botao_barracks.set_position(20, 250)        
        #botao warehouse
        self.botao_warehouse = Sprite("assets\Buttons\Botao_warehouse.png")
        self.botao_warehouse.set_position(20, 300)
        #botao firetower
        self.botao_firetower = Sprite("assets\Buttons\Botao_firetower.png")
        self.botao_firetower.set_position(20, 350)
        #botao frosttower
        self.botao_frosttower = Sprite("assets\Buttons\Botao_frosttower.png")
        self.botao_frosttower.set_position(20, 400)
        #botao rocktower
        self.botao_rocktower = Sprite("assets\Buttons\Botao_rocktower.png")
        self.botao_rocktower.set_position(20, 450)
        #botao poisontrap
        self.botao_poisontrap = Sprite("assets\Buttons\Botao_poisontrap.png")
        self.botao_poisontrap.set_position(20, 500)
        #botao firetrap
        self.botao_firetrap = Sprite("assets\Buttons\Botao_firetrap.png")
        self.botao_firetrap.set_position(20, 250)
        #botao wall
        self.botao_wall = Sprite("assets\Buttons\Botao_wall.png")
        self.botao_wall.set_position(20, 300)
        #botao obelisk
        self.botao_obelisk = Sprite("assets\Buttons\Botao_obelisk.png")
        self.botao_obelisk.set_position(20, 350)
        #botao miningcamp
        self.botao_miningcamp = Sprite("assets\Buttons\Botao_miningcamp.png")
        self.botao_miningcamp.set_position(20, 400)
        #botao woodcamp
        self.botao_woodcamp = Sprite("assets\Buttons\Botao_woodcamp.png")
        self.botao_woodcamp.set_position(20, 450)

        #botao jogo resources
        self.show_resources = Sprite("assets\Buttons\show_resources.png")
        self.show_resources.set_position(1072, 9)
        self.botao_jogo_resources = Sprite("assets\Buttons\Botao_jogo_resources.png")
        self.p_resources = True
        self.resources_counter = 0
        self.exibir_menu_resources = False

        #botao jogo research
            #controle de pesquisa
        self.pt, self.pt_end = False, False
        self.ds, self.ds_end = False, False
        self.wp, self.wp_end = False, False
        self.es, self.es_end = False, False
        self.gate = False
        self.lock_pt, self.lock_ds, self.lock_wp, self.lock_es = False, False, False, False
            #fim
            #exibição de janelas
        self.exibir_menu_research_pack_tactics = False
        self.exibir_menu_research_double_saw = False
        self.exibir_menu_research_warpainting = False
        self.exibir_menu_research_eficient_smelting = False
            #fim
        self.botao_jogo_research = Sprite("assets\Buttons\Botao_jogo_research.png")
        self.botao_jogo_research.set_position(20, 70)
        self.p_research = True
        self.research_in_progress = False
        self.timer = 0
        self.exibir_menu_research = False
        #-> botao taticas de matilha
        self.taticas_de_matilha = Sprite("assets\Buttons\Taticas_de_matilha.png")
        self.taticas_de_matilha.set_position(20, 220)
        #-> botao warpainting
        self.warpainting = Sprite("assets\Buttons\Botao_warpainting.png")
        self.warpainting.set_position(20, 270)
        #-> botao serrote duplo
        self.serrote_duplo = Sprite("assets\Buttons\Serrote_duplo.png")
        self.serrote_duplo.set_position(20, 320)
        #-> botao eficient smelting
        self.eficient_smelting = Sprite("assets\Buttons\Eficient_smelting.png")
        self.eficient_smelting.set_position(20, 370)
        #--> botao in progress
        self.in_progress = Sprite("assets\Buttons\Research_in_progress.png")
        self.in_progress.set_position(self.janela_largura/2 + 120, self.janela_altura/2 + 230)
        #-->botao already researched
        self.research_done = Sprite("assets\Buttons\Research_done.png")


        #-> Research bar small
        self.research_bar_idle_small = Sprite("assets\Buttons\Research_bar_idle_small.png")
        self.research_bar_2_small = Sprite("assets\Buttons\Research_bar_2_small.png")
        self.research_bar_3_small = Sprite("assets\Buttons\Research_bar_3_small.png")
        self.research_bar_4_small = Sprite("assets\Buttons\Research_bar_4_small.png")        
        self.research_bar_idle_small.set_position(1095, 220)
        self.research_bar_2_small.set_position(1095, 220)
        self.research_bar_3_small.set_position(1095, 220)
        self.research_bar_4_small.set_position(1095, 220)

        self.show_resources.image.blit(text_icon("book",  "RESEARCH:", (255, 255,255), large = True),(20, 180))
        



        #-> botao jogo options
        self.botao_jogo_options = Sprite("assets\Buttons\Botao_jogo_options.png")
        self.botao_jogo_options.set_position(20, 119)
        self.p_options = True
        self.exibir_menu_options = False
        #botoes de alterar volume
        self.botao_sound_direita = Sprite("assets\Buttons\Botao_construct_direita.png")
        self.botao_sound_direita.set_position(105, 285)
        self.botao_sound_esquerda = Sprite("assets\Buttons\Botao_construct_esquerda.png")
        self.botao_sound_esquerda.set_position(40, 285)
        self.is_playing_music = True
        self.volume_level = round(Settings.audio_volume*10)
        #volume level 1
        self.volume_level_1 = Sprite("assets\Buttons\Volume_level_1.png")
        self.volume_level_1.set_position(40, 250)
        #volume level 2
        self.volume_level_2 = Sprite("assets\Buttons\Volume_level_2.png")
        self.volume_level_2.set_position(40, 250)
        #volume level 3
        self.volume_level_3 = Sprite("assets\Buttons\Volume_level_3.png")
        self.volume_level_3.set_position(40, 250)
        #volume level 4
        self.volume_level_4 = Sprite("assets\Buttons\Volume_level_4.png")
        self.volume_level_4.set_position(40, 250)
        #volume level 5
        self.volume_level_5 = Sprite("assets\Buttons\Volume_level_5.png")
        self.volume_level_5.set_position(40, 250)
        #volume level 6
        self.volume_level_6 = Sprite("assets\Buttons\Volume_level_6.png")
        self.volume_level_6.set_position(40, 250)
        #volume level 7
        self.volume_level_7 = Sprite("assets\Buttons\Volume_level_7.png")
        self.volume_level_7.set_position(40, 250)
        #volume level 8
        self.volume_level_8 = Sprite("assets\Buttons\Volume_level_8.png")
        self.volume_level_8.set_position(40, 250)
        #volume level 9
        self.volume_level_9 = Sprite("assets\Buttons\Volume_level_9.png")
        self.volume_level_9.set_position(40, 250)
        #volume level 10
        self.volume_level_10 = Sprite("assets\Buttons\Volume_level_10.png")
        self.volume_level_10.set_position(40, 250)

        #fullscreen
        self.checkbox_fullscreen_true = Sprite("assets\Buttons\Checkbox_true.png")
        self.checkbox_fullscreen_false = Sprite("assets\Buttons\Checkbox_false.png")
        self.checkbox_fullscreen = Sprite("assets\Buttons\Checkbox.png")
        self.checkbox_fullscreen_true.set_position(52, 355)
        self.checkbox_fullscreen_false.set_position(52, 355)
        self.p_fullscreen = False


        #botao options restart
        self.botao_jogo_restart = Sprite("assets\Buttons\Botao_restart.png")
        self.botao_jogo_restart.set_position(50, 555)

        #botao options quit
        self.botao_jogo_quit = Sprite("assets\Buttons\Botao_quit.png")
        self.botao_jogo_quit.set_position(50, 585)

        #barra botao quit
        self.barra_botao_quit = Sprite("assets\Buttons\portal_level.png")
        self.barra_botao_quit.set_position(175,545)
        self.p_quit = False
        #botao barra quit quit
        self.botao_barra_quit_quit = Sprite("assets\Buttons\Botao_quit.png")
        self.botao_barra_quit_quit.set_position(265,593)
        #barra botao quit close
        self.botao_barra_quit_close = Sprite("assets\Buttons\Botao_close.png")
        self.botao_barra_quit_close.set_position(181,593)

        #botao jogo close
        self.botao_jogo_close = Sprite("assets\Buttons\Botao_close.png")
        self.botao_jogo_close.set_position(50, 190)
        #botao jogo close amarelo
        self.botao_jogo_close_amarelo = Sprite("assets\Buttons\Botao_close.png")
        self.botao_jogo_close_amarelo.set_position(240, 560)
        #barra botoes2 jogo
        self.barra_botoes2_jogo = Sprite("assets\Buttons\Barra_botoes2_jogo.png")
        self.barra_botoes2_jogo.set_position(7,180)
        self.p_barra_botoes2_jogo = True
        #barra background cost menu
        self.background_cost_menu = Sprite("assets\Buttons\Background_cost_menu.png")
        self.background_cost_menu.set_position(170, 182)
        #botao next
        self.botao_next = Sprite("assets\Buttons\Botao_next.png")
        self.botao_next.set_position(340, 560)

        #attack
        self.IsAttacking = True
        self.AttackTimer = 0
        self.counter_next_wave = 0
        
    def update(self,delta_time):
        self.moldura_botoes.draw()
        self.botao_jogo_construct.draw()
        self.botao_jogo_research.draw()
        self.botao_jogo_options.draw()
        self.breach_bar_frame.draw()
        self.minimap_frame.draw()

        #barra direita:
        resources.show_resources(self)
        research.show_research_blank(self)
        research.research_informations_small(self)
        reports.next_wave(self)
        
        #progressão de pesquisa:
        research.researching(self)


        #atualização dos recursos:
        self.resources_counter = resources.check_limits(self)
            
        #menu construct
        if self.clickjogo.is_over_object(self.botao_jogo_construct) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_construct = True
        if self.exibir_menu_construct:               
            self.barra_botoes2_jogo.draw()
            buildings.show_menu_construct(self)

            #Barracks:
            if self.clickjogo.is_over_object(self.botao_barracks) and self.construct_page == 1:
                buildings.popout(self, 'Barracks')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_barracks = True
            if self.exibir_menu_construct_barracks:
                buildings.popout_perma(self,'Barracks')

            #Warehouse:
            if self.clickjogo.is_over_object(self.botao_warehouse) and self.construct_page == 1:
                buildings.popout(self, 'Warehouse')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_warehouse = True
            if self.exibir_menu_construct_warehouse:
                buildings.popout_perma(self,'Warehouse')

            #Fire_tower:
            if self.clickjogo.is_over_object(self.botao_firetower) and self.construct_page == 1:
                buildings.popout(self, 'Fire_tower')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_fire_tower = True
            if self.exibir_menu_construct_fire_tower:
                buildings.popout_perma(self,'Fire_tower')

            #Frost_tower:
            if self.clickjogo.is_over_object(self.botao_frosttower) and self.construct_page == 1:
                buildings.popout(self, 'Frost_tower')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_frost_tower = True
            if self.exibir_menu_construct_frost_tower:
                buildings.popout_perma(self,'Frost_tower')

            #Rock_tower:
            if self.clickjogo.is_over_object(self.botao_rocktower) and self.construct_page == 1:
                buildings.popout(self, 'Rock_tower')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_rock_tower = True
            if self.exibir_menu_construct_rock_tower:
                buildings.popout_perma(self,'Rock_tower')

            #Poison_trap:
            if self.clickjogo.is_over_object(self.botao_poisontrap) and self.construct_page == 1:
                buildings.popout(self, 'Poison_trap')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_poison_trap = True
            if self.exibir_menu_construct_poison_trap:
                buildings.popout_perma(self,'Poison_trap')

            #Fire_trap:
            if self.clickjogo.is_over_object(self.botao_firetrap) and self.construct_page == 2:
                buildings.popout(self, 'Fire_trap')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_fire_trap = True
            if self.exibir_menu_construct_fire_trap:
                buildings.popout_perma(self,'Fire_trap')

            #Wall:
            if self.clickjogo.is_over_object(self.botao_wall) and self.construct_page == 2:
                buildings.popout(self, 'Wall')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_wall = True
            if self.exibir_menu_construct_wall:
                buildings.popout_perma(self,'Wall')

            #Obelisk:
            if self.clickjogo.is_over_object(self.botao_obelisk) and self.construct_page == 2:
                buildings.popout(self, 'Obelisk')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_obelisk = True
            if self.exibir_menu_construct_obelisk:
                buildings.popout_perma(self,'Obelisk')

            #Mining_camp:
            if self.clickjogo.is_over_object(self.botao_miningcamp) and self.construct_page == 2:
                buildings.popout(self, 'Mining_camp')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_mining_camp = True
            if self.exibir_menu_construct_mining_camp:
                buildings.popout_perma(self,'Mining_camp')

            #Wood_camp:
            if self.clickjogo.is_over_object(self.botao_woodcamp) and self.construct_page == 2:
                buildings.popout(self, 'Wood_camp')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_construct_woodcamp = True
            if self.exibir_menu_construct_woodcamp:
                buildings.popout_perma(self,'Wood_camp')
            
            
            #fechar o menu construct
            self.botao_jogo_close.draw()
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_construct = False
            #fim

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

            #Warpainting:
            if self.clickjogo.is_over_object(self.warpainting):
                research.popout(self,'Warpainting')
                if self.clickjogo.is_button_pressed(True):
                    self.exibir_menu_research_warpainting = True
            if self.exibir_menu_research_warpainting:
                research.popout_perma(self,'Warpainting')

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

        
        #menu options
        if self.clickjogo.is_over_object(self.botao_jogo_options) and self.clickjogo.is_button_pressed(True):
            self.exibir_menu_options = True
        if self.exibir_menu_options:              
            self.barra_botoes2_jogo.draw()
            self.botao_jogo_close.draw()
            options.music_level(self)
            options.fullscreen(self)
            options.exit(self)

            #fechar                                  
            if self.clickjogo.is_over_object(self.botao_jogo_close) and self.clickjogo.is_button_pressed(True):
                self.exibir_menu_options = False