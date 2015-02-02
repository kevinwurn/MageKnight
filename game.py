import player
import board

GAME_TYPE_SOLO = 0
TIME_DAY = 0
TIME_NIGHT = 1
BATTLE_PHASE_RANGED_SIEGED = 0
BATTLE_PHASE_BLOCK = 1
BATTLE_PHASE_ASSIGN_DAMAGE = 2
BATTLE_PHASE_ATTACK = 3

class Game(object):
    game_type = None
    num_rounds = None
    time_of_day = None
    arythrea = None
    num_green_tiles = None
    num_brown_non_city_tiles = None
    num_brown_city_tiles = None
    city_levels = None
    battle_phase = None

    def __init__(self, screen):
        self.game_type = GAME_TYPE_SOLO
        if self.game_type == GAME_TYPE_SOLO:
            self.num_rounds = 6
            self.arythrea = player.Arythrea()
            self.num_green_tiles = 7
            self.num_brown_non_city_tiles = 2
            self.num_brown_city_tiles = 2
            self.city_levels = [None]*2
            self.city_levels[0] = 5
            self.city_levels[1] = 8
            self.time_of_day = TIME_DAY