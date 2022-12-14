



from os import path
from audio.audiomanager import AudioManager
from match import Match
import math
import pygame

from camera import Camera


class SpacialSFX():

    library = {}
    started = False

    def Setup():
        pygame.mixer.init()
        SpacialSFX.library = {  "bubble":"bubble.wav",
                                "pick":"pickaxe.wav" }

    def __init__(self, filename, x, y, real_delta_time = False) -> None:
        if not SpacialSFX.started:
            SpacialSFX.Setup()

        self.file = None
        self.pos = (x,y)
        self.sound = None
        self.real_delta_time = real_delta_time
        self.timer = 0.0
        self.length = 2.0

        soundfile = SpacialSFX.library.get(filename, None)
        if soundfile == None:
            self.sound = None
        else:
            self.sound = pygame.mixer.Sound(path.join("assets","audio",soundfile))
            self.sound.play()
            self.length = self.sound.get_length()
            AudioManager.spacialSFXs.append(self)


    def update(self, delta_time):
        if self.sound == None:
            return
        if delta_time <=  0.0 and self.real_delta_time == False:
            return
        if delta_time <= 0.0 and self.real_delta_time == True:
            delta_time = Match.game.gameWindow.delta_time()

        self.timer += delta_time


        volume = min(1, 200/math.dist(self.pos, Camera.center()))
        #print(volume, "  ", math.dist(self.pos, Camera.center()))
     
        self.sound.set_volume(volume)