


class AudioManager():


    spacialSFXs = []

    def update(delta_time):
        for audio in AudioManager.spacialSFXs:
            audio.update(delta_time)
            if audio.timer > audio.length:
                AudioManager.spacialSFXs.remove(audio)