
from effects.effectsmanager import EffectsManager
from settings import SimulationMode
from buildings.buildingmanager import BuildingManager
from interface.buildingmode import BuildingMode
from interface.debug_interface import DebugInterface
from interface.framerate import Framerate
from interface.gameinterface import Gameinterface
from mapa.tilemap import Tilemap
from mapa.tileset import Tileset
from movables.movablesmanager import MovablesManager
from world import World
import movables.pathfinder as pathfinder


class Game: 
    def __init__(self, settings, gameWindow):
        self.s = settings      
        self.gameWindow = gameWindow
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

        #movablesmanager: gerencia os personagens
        self.movables_manager = MovablesManager(self,self.world)    

        #interface do jogo
        self.gameinterface = Gameinterface(settings,gameWindow)

        #interface com botoes de teste
        self.debuginterface = DebugInterface(settings, gameWindow, self)

        #interface de construção de construções
        self.building_mode_interface = BuildingMode(self)

        #effects manager: gerencia e desenha os efeitos (dano, etc)
        self.effects_manager = EffectsManager()

        #inicia o modulo de pathfinding
        pathfinder.setup(self.world)

    #loop principal
    def update(self, delta_time):  

        #gera os caminhos no módulo de pathfinding
        pathfinder.update(delta_time)

        #limpa a janela     
        self.gameWindow.set_background_color([128,128,128])     

        #escreve a imagem do mapa na janela
        self.tilemap.draw(self.gameWindow, self.world) 

        #escreve a imagem dos objetos na janela
        self.buildings_manager.draw(self.gameWindow, self.world)  

        #escreve a imagem das criaturas na tela
        self.movables_manager.update(self.world, delta_time) 
        
        match self.simulation_mode:
            case SimulationMode.RUNNING:

                #escreve a interface na tela
                self.gameinterface.update(delta_time)

                #escreve a interface de testes na tela
                self.debuginterface.update(delta_time)

            case SimulationMode.BUILDING:
                #executa o modo de construção, escrevendo a silhueta da construção na tela
                self.building_mode_interface.update(delta_time)

        self.effects_manager.update(delta_time)

        #atualiza a janela e rendeniza tudo
        self.gameWindow.set_title(self.s.gameApplicationName + self.framerate.get_text(delta_time))
        #ideal < 16ms = 60fps





        