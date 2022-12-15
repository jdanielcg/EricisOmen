
import os
from pygame import mixer

from match import Match
from settings import Settings

class AudioManager():


    spacialSFXs = []

    fadetimer = -1
    next_music = None

    musictracks = [ os.path.join("assets","audio","loop3.ogg"), #battle
                    os.path.join("assets","audio","135_loop_2.ogg"), #menu
                    os.path.join("assets","audio","Hell's battle 2 (loop).ogg"), #game
                    os.path.join("assets","audio","135_loop_2.ogg"), #victory
    ]
           

    def update(delta_time):
        for audio in AudioManager.spacialSFXs:
            audio.update(delta_time)
            if audio.timer > audio.length:
                audio.sound.stop()
                AudioManager.spacialSFXs.remove(audio)


        #music change
        mixer.music.set_volume(Settings.audio_volume*Settings.audio_volume)

        if AudioManager.fadetimer > 0.0:
            AudioManager.fadetimer -= Match.game.gameWindow.delta_time()
            if AudioManager.fadetimer <= 0.0:
                AudioManager.fadetimer = -1
                if AudioManager.next_music != None:
                    AudioManager.next()


    def setup():
        mixer.init()
        mixer.music.load(AudioManager.musictracks[1])        
        mixer.music.set_volume(Settings.audio_volume)
        mixer.music.play(-1)                

    def change_music(index):
        if index < len(AudioManager.musictracks):
            AudioManager.next_music = AudioManager.musictracks[index]          
            mixer.music.fadeout(2900)
            AudioManager.fadetimer = 3.0
            #mixer.music.play(-1) 

    def next():
        mixer.music.load(AudioManager.next_music)  
        mixer.music.set_volume(Settings.audio_volume)
        mixer.music.play(-1)
        AudioManager.next_music = None