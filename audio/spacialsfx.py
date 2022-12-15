



from os import path
from audio.audiomanager import AudioManager
from match import Match
import math
import pygame

from camera import Camera
from settings import Settings


class SpacialSFX():

    library = {}
    started = False

    def Setup():
        pygame.mixer.init()
        SpacialSFX.library = {  
                                "pick":"pick.ogg",
                                "chop":"15Hitonwood.wav",
                                "enemyhit":"swing.wav",
                                "allyhit":"swing3.wav",
                                "dead":"51Flee02.wav",
                                "portalcrack":"DragonStomp Snow (2).wav",
                                "build":"GPPutDown1.wav",
                                "demolish":"GPDamage5.wav",
                                "firehit": "03fruit.wav", #"04Fire.wav",
                                "stonehit":"61Hit03.wav",
                                "frozenhit":"bubble.wav",
                                "towershot":"cloth.wav",
                                "poisontrap" : "bite-small2.wav",
                                "wavestart":"GPBeginTurn1.wav",

                                "explosion":"explode.ogg",   
                                "explosion2" : "18Thunder.wav",                             
                                "spitfire" :"DragonBreath (7).wav", #"DragonBreath (1).wav",
                                "endgame" : "AstralDragon (9).wav",
                                "dragon":"DragonFlight (3).wav", #"DragonBreathing (10).wav",
                                 }

    def __init__(self, filename, x, y, real_delta_time = False, max_volume = False, loop = False, given_length = 0.0) -> None:
        if not SpacialSFX.started:
            SpacialSFX.Setup()

        self.file = None
        self.max_volue = max_volume
        self.loop = loop
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
            self.sound.play(loops= 0 if not loop else -1)
            self.length = self.sound.get_length()
            AudioManager.spacialSFXs.append(self)
        if given_length > 0.0:
            self.length = given_length


    def update(self, delta_time):
        if self.sound == None:
            return
        if delta_time <=  0.0 and self.real_delta_time == False:
            return
        if delta_time <= 0.0 and self.real_delta_time == True:
            delta_time = Match.game.gameWindow.delta_time()

        self.timer += delta_time


        volume = 1
        if self.max_volue:
            volume = 1
        else:
            volume = min(1, 200/math.dist(self.pos, Camera.center()))

        #print(volume, "  ", math.dist(self.pos, Camera.center()))
     
        self.sound.set_volume(volume*Settings.audio_volume)