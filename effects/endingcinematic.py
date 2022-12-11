from camera import Camera
from effects.effectsmanager import EffectsManager
from settings import Settings
from effects.effects import EricisBirth, Ericis

class Ending():
    def __init__(self, game):
        self.game = game

        self.start = False

    def start_end(self):
        Camera.set_view_from_center(Settings.breach_center[0], Settings.breach_center[1])

        #centraliza a camera na fenda

        #cria lista de tiles

        ox = Settings.breach_center[0] * Settings.tilesize
        oy = Settings.breach_center[1] * Settings.tilesize

        EffectsManager.effects.append(EricisBirth(ox, oy, self.birth_ericis))

    def birth_ericis(self):
        ox = Settings.breach_center[0] * Settings.tilesize
        oy = Settings.breach_center[1] * Settings.tilesize

        EffectsManager.effects.append(Ericis(ox, oy))



    def update(self, delta_time):
        if self.start == False:
            self.start = True
            self.start_end()

        #pega um tile da lista, explode

        #desenha uma tela preta, fazendo o fadeuot do jogo

        #ericis de um lado ao outro, creditos rolam