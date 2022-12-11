# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

from camera import Camera
from effects.effectsmanager import EffectsManager
from effects.endingcinematic import Ending
from effects.loseendingcinematic import LostEnding
from interface.interface import Interface
from movables.waver import Waver
from settings import Settings, SimulationMode
from buildings.buildingmanager import BuildingManager
from interface.buildingmode import BuildingMode
from interface.debug_interface import DebugInterface
from interface.framerate import Framerate

from mapa.tilemap import Tilemap
from mapa.tileset import Tileset
from movables.movablesmanager import MovablesManager
from world import World
import movables.pathfinder as pathfinder


class Game: 
    def __init__(self, settings, gameWindow):
        self.s = settings      
        self.gameWindow = gameWindow
        self.screen = gameWindow.get_screen()
        self.framerate = Framerate()

        #stores the current simulation mode
        self.simulation_mode = SimulationMode.RUNNING

        #world: gerencia a representação lógica do mundo, é onde estão as células (cell)
        self.world = World() 

        #tilemap: gerencia a representação visual do mapa fixo, apartir das cells
        #uma cell representa um tile
        self.tilemap = Tilemap(Tileset("edit_terrain.png",(32, 32)))    

        #buildings_manager: gerencia a representação visual dos objetos, construcao, etc
        self.buildings_manager = BuildingManager(self, "edit_terrain.png")
        self.buildings_manager.build_base()

        #movablesmanager: gerencia os personagens
        self.movables_manager = MovablesManager(self,self.world)    

        #interface do jogo
        self.gameinterface = Interface(gameWindow)

        #interface com botoes de teste
        self.debuginterface = DebugInterface(settings, gameWindow, self)

        #interface de construção de construções
        self.building_mode_interface = BuildingMode(self)

        #effects manager: gerencia e desenha os efeitos (dano, etc)
        self.effects_manager = EffectsManager()

        #inicia o modulo de pathfinding
        pathfinder.setup(self.world)

        #seleciona a posição inicial da camera
        Camera.set_view_from_center(Settings.breach_center[0], Settings.breach_center[1])

        #controla as animações e creditos ao fim da partida
        self.endgame_cinematic = Ending(self)

        #controla as animações de fim de jogo ao perder
        self.losegame_cinematic = LostEnding(self)

        #inicializa o controle da geração de inimigos
        Waver.setup(self)

    #loop principal
    def update(self, delta_time):  

        Camera.update(delta_time)
        Waver.update(delta_time)

        #atualiza o estado do mapa:
        self.world.update(delta_time)      

        #limpa a janela     
        self.gameWindow.set_background_color([128,128,128])     

        #escreve a imagem do mapa na janela
        self.tilemap.draw(self.gameWindow, self.world) 

        #gera os caminhos no módulo de pathfinding
        pathfinder.update(delta_time)

        #escreve a imagem dos objetos na janela        
        self.buildings_manager.update(self.gameWindow, self.world, delta_time)  

        #escreve a imagem das criaturas na tela
        self.movables_manager.update(self.world, delta_time) 
        
        match self.simulation_mode:
            case SimulationMode.RUNNING:

                #escreve a interface na tela
                #self.gameinterface.update(delta_time)

                #escreve a interface de testes na tela
                self.debuginterface.update(delta_time)                

            case SimulationMode.BUILDING:
                #executa o modo de construção, escrevendo a silhueta da construção na tela
                self.building_mode_interface.update(delta_time)   

            case SimulationMode.ENDING:
                #executa as animações de fim de jogo      
                self.endgame_cinematic.update(delta_time)

            case SimulationMode.LOSE:
                #executa as animações de fim de jogo      
                self.losegame_cinematic.update(delta_time)

        self.effects_manager.update(delta_time)

        #atualiza a janela e rendeniza tudo
        self.gameWindow.set_title(self.s.gameApplicationName + self.framerate.get_text(delta_time))
        #ideal < 16ms = 60fps





        