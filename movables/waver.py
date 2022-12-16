# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: RAMON SANTOS         ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

import random
from audio.audiomanager import AudioManager
from audio.spacialsfx import SpacialSFX
from movables.creatures import Creature
from settings import Settings


class Waver:
    
    game = None

    current_wave = 0

    interval = 60.0
    enemies_desired_number = 0
    enemies_max_number = 30

    timer = 0.0
    generate_timer = 0.0

    current_enemies = []
    enemies_to_spawn = []

   

    def setup(game):
        Waver.game = game        
        Waver.interval = 60.0
        Waver.enemies_desired_number = 5
        Waver.enemies_max_number = 30    
        Waver.timer = 0.0   
        Waver.current_wave = 0 
        Waver.current_enemies = []        
        Waver.is_attacking = False

        Waver.generate_timer = 0.0

        Waver.start_attack()

        
    
    def start_attack():
        Waver.timer = 0.0
        Waver.is_attacking = True
        Waver.current_wave += 1
        Waver.enemies_desired_number = min(Waver.current_wave*5, Waver.enemies_max_number)
        print("Wave ", Waver.current_wave, " started with ", Waver.enemies_desired_number, "enemies.")

        #clear old enemies
        for enemy in Waver.current_enemies:
            if enemy in Waver.game.world.creatures:
                Waver.game.world.creatures.remove(enemy)
        Waver.current_enemies = []

        Waver.enemies_to_spawn = Waver.suffle_enemies(Waver.current_wave)

        if Waver.current_wave > 1:
            SpacialSFX("wavestart",0, 0, max_volume= True) 
            AudioManager.change_music(0)

    def generate_one_enemy():
        if len(Waver.game.world.creatures) < Settings.max_creatures:
            for pos in Settings.enemy_spawns:                           
                cell = Waver.game.world.cells[pos[1]][pos[0]]
                if cell.vacant and len(Waver.enemies_to_spawn) > 0:   
                    strength = (Waver.current_wave/10.0 + 1)    
                    if strength > 2:
                        strength = 2         
                    creature = Waver.enemies_to_spawn.pop()(pos, strength)
                    Waver.current_enemies.append(creature)
                    Waver.game.world.creatures.append(creature)
                    break

    def make_maceman(pos, strength):
        return Creature(Waver.game, pos, is_enemy = True, folder = "maceman",
                 aether = 100*strength, damage = 200*strength,
                 speed= 7.5*strength, max_integrity= 5000*strength)

    def make_pickman(pos, strength):
        return Creature(Waver.game, pos, is_enemy = True, folder = "pickman",
                 aether = 35*strength, damage = 400*strength,
                 speed= 10.0*strength, max_integrity= 1000*strength)

    def make_spearman(pos, strength):
        return Creature(Waver.game, pos, is_enemy = True, folder = "spearman",
                 aether = 20* strength, damage = 100*strength,
                 speed= 15.0*strength, max_integrity= 500*strength)

    def make_swordman(pos, strength):
        return Creature(Waver.game, pos, is_enemy = True, folder = "swordman",
                 aether = 25* strength, damage = 200*strength,
                 speed= 15.0*strength, max_integrity= 700*strength)

    def make_minotaur(pos, strength):
        return Creature(Waver.game, pos, is_enemy = True, folder = "minotaur",
                 aether = 80* strength, damage = 500*strength,
                 speed= 20.0*strength, max_integrity= 2000*strength)

    def make_kobold(pos, strength = 1):
        return Creature(Waver.game, pos, is_enemy = False, folder = "kobold",
                 aether = 0* strength, damage = 1000*strength,
                 speed= 25.0*strength, max_integrity= 2000*strength)

    def make_emissary(pos, strength = 1):
        return Creature(Waver.game, pos, is_enemy = False, folder = "emissary",
                 aether = 0* strength, damage = 10000*strength,
                 speed= 25.0*strength, max_integrity= 20000*strength)

    def suffle_enemies(current_wave):
        tierlist = []
        if current_wave <= 1:
            tierlist = [Waver.make_pickman, Waver.make_spearman]
        elif current_wave <= 2:
            tierlist = [Waver.make_pickman, Waver.make_spearman,Waver.make_spearman, Waver.make_maceman]
        elif current_wave <= 3:
            tierlist = [Waver.make_pickman, Waver.make_spearman, Waver.make_maceman, Waver.make_swordman]
        elif current_wave >= 4:
            tierlist = [Waver.make_pickman, Waver.make_swordman, Waver.make_minotaur]
        else:
            tierlist = [Waver.make_spearman]

        #para testes
        #tierlist = [Waver.make_maceman, Waver.make_swordman, Waver.make_minotaur]

        return random.choices(tierlist, k=Waver.enemies_desired_number )

    
    def finish_wave():
        Waver.timer = 0.0
        Waver.is_attacking = False
        AudioManager.change_music(2)

    def update(delta_time):
        if not Waver.is_attacking:
            Waver.timer += delta_time
            if Waver.timer > Waver.interval:                
                Waver.start_attack()
        else:
            if len(Waver.current_enemies) < Waver.enemies_desired_number:
                Waver.generate_timer += delta_time
                if Waver.generate_timer > 0.3:
                    Waver.generate_timer = 0.0
                    Waver.generate_one_enemy()
            elif len(Waver.current_enemies) == Waver.enemies_desired_number:
                #vamos verificar se estão todos mortos
                all_dead = True
                for enemy in Waver.current_enemies:
                    if not enemy.is_dead:
                        all_dead = False
                        break
                if all_dead:
                    Waver.finish_wave()
            
