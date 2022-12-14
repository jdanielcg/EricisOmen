# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝


from match import Match


class EffectsManager:
    effects = []
    def __init__(self):
        pass
        
    def update(self, delta_time):        
        for effect in EffectsManager.effects:
            effect.update(delta_time)
            if effect.timer >= effect.duration:
                EffectsManager.effects.remove(effect)

