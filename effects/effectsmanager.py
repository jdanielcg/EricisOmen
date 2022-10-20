# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


class EffectsManager:
    def __init__(self):

        self.effects = []

        
    def update(self, delta_time):
        for effect in self.effects:
            effect.update(delta_time)
            if effect.timer >= effect.duration:
                self.effects.remove(effect)

