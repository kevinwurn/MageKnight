import pygame
import game
import actions
import cards

# constats for players
ARYTHREA = 40
PLAYER_MAX_HAND_SIZE = 5
PLAYER_ARMOR = 2
PLAYER_MAX_UNITS = 1

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
CARD_ASSET_ACTION_TYPE_ADVANCED = 30
CARD_ASSET_ACTION_TYPE_NON_ADVANCED = 31 

# pass around mainly for battling monsters.  Allowing for future development to assign individual assets to monsters 
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
    game_engine = None
    name = None
    armor = None
    hand_limit = None
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
    deed_discard = None
    trashed_cards = None
    hand = None
    card_assets = None
    triggers = None
    skills = None
    skills_offer = None
    influence = None
    move = None
    reputation = None
    fame = None
    level_up = None
    units = None
    location_tile_num = None
    location_hex_num = None
    
    def __init__(self, new_game_engine):
        super().__init__()
        self.game_engine = new_game_engine
        self.armor = PLAYER_ARMOR
        self.hand_limit = PLAYER_MAX_HAND_SIZE
        self.num_red_crystals = 0
        self.num_blue_crystals = 0 
        self.num_white_crystals = 0
        self.num_green_crystals = 0
        self.num_red_tokens = 0
        self.num_blue_tokens = 0
        self.num_white_tokens = 0
        self.num_green_tokens = 0
        self.deed_deck = []
        self.deed_discard = []
        self.trashed_cards = []
        self.hand = []
        self.card_assets = []
        self.triggers = []
        self.skills = []
        self.skills_offer = []
        self.influence = 0
        self.move = 0
        self.reputation = ReputationTracker() 
        self.fame = FameTracker()
        self.max_units = PLAYER_MAX_UNITS
        self.units = [PLAYER_MAX_UNITS]
        self.location_tile_num = 0
        self.location_hex_num = 6
        
    def start_turn(self):
        # process triggers = add magical_glade.interact_start()
        for i in range(self.hand_limit):
            card = self.draw()
            if card:
                self.hand.append(card)
            else:
                print("end round")
                return False
        
        
    def end_turn(self):
        #cleanup
        self.num_red_tokens = 0
        self.num_blue_tokens = 0
        self.num_white_tokens = 0
        self.num_green_tokens = 0
        if self.game_engine.time_of_day == game.TIME_DAY:
            self.game_engine.time_of_day = game.TIME_NIGHT
            self.num_gold_crystals = 0
        elif self.game_engine.time_of_day == game.TIME_NIGHT:
            self.game_engine.time_of_day = game.TIME_DAY
            self.num_black_crystals = 0
        self.trashed_cards = []
        #draw cards to hand limit
        self.card_assets = []
        #process triggers - add level_up trigger
        #reset skills
        self.influence = 0
        if self.level_up == True:
            self.level_up
            self.level_up = False
        
    def level_up(self):
        if self.fame.level == 1 or self.fame.level == 2:
            self.armor = PLAYER_ARMOR
            self.hand_limit = PLAYER_MAX_HAND_SIZE
            self.max_units = PLAYER_MAX_UNITS
            # if level 2
            # draw advanced action from advanced actions offer
            # draw two skills from skils offer and choose one skill
        elif self.fame.level == 3 or self.fame.level == 4:
            self.armor = PLAYER_ARMOR + 1
            self.hand_limit = PLAYER_MAX_HAND_SIZE
            self.max_units = PLAYER_MAX_UNITS + 1
            # if level 4
            # draw advanced action from advanced actions offer
            # draw two skills from skils offer and choose one skill
        elif self.fame.level == 5 or self.fame.level == 6:
            self.armor = PLAYER_ARMOR + 1
            self.hand_limit = PLAYER_MAX_HAND_SIZE + 1
            self.max_units = PLAYER_MAX_UNITS + 2
            # if level 6
            # draw advanced action from advanced actions offer
            # draw two skills from skils offer and choose one skill
        elif self.fame.level == 7 or self.fame.level == 8:
            self.armor = PLAYER_ARMOR + 2
            self.hand_limit = PLAYER_MAX_HAND_SIZE + 1
            self.max_units = PLAYER_MAX_UNITS + 3
            # if level 8
            # draw advanced action from advanced actions offer
            # draw two skills from skils offer and choose one skill
        elif self.fame.level == 9 or self.fame.level == 10:
            self.armor = PLAYER_ARMOR + 2
            self.hand_limit = PLAYER_MAX_HAND_SIZE + 2
            self.max_units = PLAYER_MAX_UNITS + 4
            # if level 10
            # draw advanced action from advanced actions offer
            # draw two skills from skils offer and choose one skill        

    def draw(self):
        if self.deed_deck:
            card = self.deed_deck.pop()
            return card
        return False

class Arythrea(Player):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Arythrea"
        list_of_cards = actions.Actions(self.game_engine).actions_collection
        for card in list_of_cards:
            self.deed_deck.append(card)