import pygame

# constants for the Trackers
REPUTATION_TRACKER_END = 15
FAME_TRACKER_END = 120

# constants for the Battle Assets
CARD_ASSET_TYPE_BLOCK = 0
CARD_ASSET_TYPE_ATTACK = 1
CARD_ASSET_TYPE_RANGED_ATTACK = 2
CARD_ASSET_TYPE_SIEGE_ATTACK = 3
CARD_ASSET_TYPE_MOVE = 4
CARD_ASSET_TYPE_INFLUENCE = 5
ELEMENT_PHYSICAL = 10
ELEMENT_FIRE = 11
ELEMENT_COLD = 12
ELEMENT_COLD_FIRE = 13
CRYSTAL_NONE = 20
CRYSTAL_RED = 21
CRYSTAL_BLUE = 22
CRYSTAL_WHITE = 23
CRYSTAL_GREEN = 24
CRYSTAL_GOLD = 25
CRYSTAL_BLACK = 26
CARD_ASSET_ACTION_TYPE_ADVANCED = 30
CARD_ASSET_ACTION_TYPE_NON_ADVANCED = 31 

class CardAsset(object):
    source_id = None
    type = None
    action_type = None
    element = None
    amount = None
    crystal_type = None

    def __init__(self, new_source_id, new_type, new_action_type, new_element, new_amount, new_crystal_type):
        self.source_id = new_source_id
        self.type = new_type
        self.action_type = new_action_type
        self.element = new_element
        self.amount = new_amount
        self.crystal_type = new_crystal_type

class ReputationTracker(object):
    reputation = None
    tracker = None
    @property
    def influence_adjustment(self):
        return self.tracker[self.location]
    
    def __init__(self):
        self.reputation = 7
        self.tracker = [None]*REPUTATION_TRACKER_END
        self.tracker[0] = "X"
        self.tracker[1] = -5
        self.tracker[2] = -3
        self.tracker[3] = -2
        self.tracker[4] = -1
        self.tracker[5] = -1
        self.tracker[6] = 0
        self.tracker[7] = 0 
        self.tracker[8] = 0
        self.tracker[9] = 1
        self.tracker[10] = 1 
        self.tracker[11] = 2
        self.tracker[12] = 2
        self.tracker[13] = 3
        self.tracker[14] = 5
    def increase_reputation(self, points):
        if self.location + points < REPUTATION_TRACKER_END:
            self.reputation += points
    def decrease_reputation(self, points):
        if self.reputation - points < 0:
            self.reputation -= points

class FameTracker(object):
    fame = None
    tracker = None
    @property
    def level(self):
        return self.tracker[self.fame]
    
    def __init__(self):
        self.fame = 0
        self.tracker = [None]*FAME_TRACKER_END
        for i in range(2):
            self.tracker[i] = 1
        for i in range(3, 7):
            self.tracker[i] = 2
        for i in range(8, 14):
            self.tracker[i] = 3
        for i in range(15, 23):
            self.tracker[i] = 4
        for i in range(24, 34):
            self.tracker[i] = 5
        for i in range(35, 47):
            self.tracker[i] = 6
        for i in range(48, 62):
            self.tracker[i] = 7
        for i in range(63, 79):
            self.tracker[i] = 8
        for i in range(80, 98):
            self.tracker[i] = 9
        for i in range(99, 119):
            self.tracker[i] = 10
    def increase_fame(self, points):
        if self.fame + points < FAME_TRACKER_END:
            self.fame += points
    def decrease_fame(self, points):
        if self.reputation - points < 0:
            self.reputation -= points

class Player(pygame.sprite.Sprite):
    name = None
    armor = None
    num_cards = None
    num_red_crystals = None
    num_blue_crystals = None
    num_white_crystals = None
    num_green_crystals = None
    num_gold_crystals = None
    num_black_crystals = None
    num_red_tokens = None
    num_blue_tokens = None
    num_white_tokens = None
    num_green_tokens = None
    num_gold_tokens = None
    num_black_tokens = None
    deed_deck = None
    hand = None
    card_assets = None
    skills = None
    influence = None
    move = None
    reputation = None
    fame = None
    level_up = None
    units = None
    
    def __init__(self):
        super().__init__()
        self.armor = 2
        self.num_cards = 5
        self.num_red_crystals = 0
        self.num_blue_crystals = 0 
        self.num_white_crystals = 0
        self.num_green_crystals = 0
        self.num_red_tokens = 0
        self.num_blue_tokens = 0
        self.num_white_tokens = 0
        self.num_green_tokens = 0
        self.deed_deck = []
        self.hand = [self.num_cards]
        self.card_assets = []
        self.skills = []
        self.influence = 0
        self.move = 0
        self.reputation = ReputationTracker() 
        self.fame = FameTracker()
        self.level_up = False 
        self.max_units = 1
        self.units = [self.max_units]

class Arythrea(Player):
    def __init__(self):
        super().__init__()
        self.name = "Arythrea"