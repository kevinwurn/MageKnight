import pygame
import player
import advanced_actions
import spells
import artifacts
import units

TIME_DAY = 0
TIME_NIGHT = 1

# phases of battle
BATTLE_PHASE_RANGED_SIEGED = 0
BATTLE_PHASE_BLOCK = 1
BATTLE_PHASE_ASSIGN_DAMAGE = 2
BATTLE_PHASE_ATTACK = 3

# constants for Elements
ELEMENT_PHYSICAL = 10
ELEMENT_FIRE = 11
ELEMENT_COLD = 12
ELEMENT_COLD_FIRE = 13

# constants for Crystals
CRYSTAL_NONE = 20
CRYSTAL_RED = 21
CRYSTAL_BLUE = 22
CRYSTAL_WHITE = 23
CRYSTAL_GREEN = 24
CRYSTAL_GOLD = 25
CRYSTAL_BLACK = 26

class Game(object):
    num_rounds = None
    current_round = None
    time_of_day = None
    arythrea = None
    num_green_tiles = None
    num_brown_non_city_tiles = None
    num_brown_city_tiles = None
    city_levels = None
    battle_phase = None
    chosen_player = None
    advanced_actions_offer = None
    monestary_advanced_actions_offer = None
    advanced_actions_discard = None
    spells_offer = None
    spells_discard = None
    artifacts_offer = None
    artifacts_discard = None
    units_grey_offer = None
    units_grey_discard = None
    units_gold_offer = None
    units_gold_discard = None
    sprite_collection = None
    tile_group = None
    token_group = None
    card_group = None
    player_group = None

    def __init__(self, screen):
        self.num_rounds = 6
        self.current_round = 1
        self.num_green_tiles = 7
        self.num_brown_non_city_tiles = 2
        self.num_brown_city_tiles = 2
        self.city_levels = [None]*2
        self.city_levels[0] = 5
        self.city_levels[1] = 8
        self.time_of_day = TIME_DAY
        self.advanced_actions_offer = advanced_actions.AdvancedActions()
        self.monestary_advanced_actions_offer = advanced_actions.AdvancedActions()
        self.advanced_actions_discard = []
        self.spells_offer = spells.Spells()
        self.spells_discard = []
        self.artifacts_offer = artifacts.Artifacts()
        self.artifacts_discard = []
        self.units_grey_offer = units.GreyUnits
        self.units_grey_discard = []
        self.units_gold_offer = units.GoldUnits
        self.units_gold_discard = []
        self.sprite_collection = []
        self.tile_group = pygame.sprite.Group()
        self.token_group = pygame.sprite.Group()
        self.card_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        
    def setup(self):
        # setup all of the offers
        # crap... forgot about tokens... will need to add token offers to game class as well
        # common skill area
        print("setup")
        if self.chosen_player == player.ARYTHREA:
            self.arythrea.draw_hand()

    
    def start_round(self):
        # don't forget to choose tactics first
        # roll mana die
        # change offers
        print("start round")
        if self.chosen_player == player.ARYTHREA:
            self.arythrea.draw_hand()

    def start_turn(self):
        if self.chosen_player == player.ARYTHREA:
            self.arythrea.draw_hand()                