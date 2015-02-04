import game
import cards

# Interactable Locations
LOCATION_CRYSTAL_MINE_GREEN = 0
LOCATION_CRYSTAL_MINE_RED = 1
LOCATION_CRYSTAL_MINE_WHITE = 2
LOCATION_CRYSTAL_MINE_BLUE = 3
LOCATION_CRYSTAL_MINE_BLUE_GREEN = 4
LOCATION_CRYSTAL_MINE_RED_WHITE = 5
LOCATION_CRYSTAL_MINE_FOUR_COLORS = 6
LOCATION_MAGICAL_GLADE = 7
LOCATION_VILLAGE = 8
# Conquerable Locations
LOCATION_MONASTERY = 9
LOCATION_KEEP = 10
LOCATION_MAGE_TOWER = 11
LOCATION_DUNGEON = 12
LOCATION_TOMB = 13
LOCATION_MONSTER_DEN = 14
LOCATION_SPAWNING_GROUNDS = 15
LOCATION_ANCIENT_RUINS = 18
# Multiple Conquerable Locations
LOCATION_MAZE = 16
LOCATION_LABYRINTH = 17
LOCATION_CITY_GREEN = 19
LOCATION_CITY_RED = 20
LOCATION_CITY_WHITE = 21
LOCATION_CITY_BLUE = 22
# Rampaging Enemy Locations
LOCATION_DRACONUM = 23
LOCATION_ORCS = 24

# Placeholder location
class Location(object):
    type = None
    game_engine = None
    tile_board_zone = None
    hex_board_zone = None
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__()
        self.game_engine = new_game_engine
        self.tile_board_zone = new_tile_board_zone
        self.hex_board_zone = new_hex_board_zone
        
# Location Prototypes
class LocationInteractable(Location):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class LocationConquerable(Location):
    player_conquerer = None
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class LocationMultipleConquerable(Location):
    player_conquerers = None
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
        self.player_conquerers = []
class LocationRampagingEnemy(Location):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)

# Interactable Locations
class Location_Crystal_Mine_Green(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self):
        self.game_engine.current_player.num_green_crystals += 1
        return True
class Location_Crystal_Mine_Red(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self):
        self.game_engine.current_player.num_red_crystals += 1
        return True
class Location_Crystal_Mine_White(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self):
        self.game_engine.current_player.num_white_crystals += 1
        return True
class Location_Crystal_Mine_Blue(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self):
        self.game_engine.current_player.num_blue_crystals += 1
        return True
class Location_Crystal_Mine_Blue_Green(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self, crystal):
        if crystal == game.CRYSTAL_GREEN:
            self.game_engine.current_player.num_green_crystals += 1
            return True
        elif crystal == game.CRYSTAL_BLUE:
            self.game_engine.current_player.num_blue_crystals += 1
            return True
        return False
class Location_Crystal_Mine_Red_White(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self, crystal):
        if crystal == game.CRYSTAL_RED:
            self.game_engine.current_player.num_red_crystals += 1
            return True
        elif crystal == game.CRYSTAL_WHITE:
            self.game_engine.current_player.num_white_crystals += 1
            return True
        return False
class Location_Crystal_Mine_Four_Colors(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact(self, crystal):
        if crystal == game.CRYSTAL_RED:
            self.game_engine.current_player.num_red_crystals += 1
            return True
        elif crystal == game.CRYSTAL_WHITE:
            self.game_engine.current_player.num_white_crystals += 1
            return True
        elif crystal == game.CRYSTAL_GREEN:
            self.game_engine.current_player.num_green_crystals += 1
            return True
        elif crystal == game.CRYSTAL_BLUE:
            self.game_engine.current_player.num_blue_crystals += 1
            return True
        return False
class Location_Magical_Glade(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
    def interact_start_turn(self):
        if self.game_engine.current_player.location_tile == self.tile_board_zone and \
            self.game_engine.current_player.location_hex == self.hex_board_zone:
            if self.game_engine.time_of_day == game.TIME_DAY:
                self.game_engine.current_player.num_gold_crystals += 1
                return True
            elif self.game_engine.time_of_day == game.TIME_NIGHT:
                self.game_engine.current_player.num_black_tokens += 1
                return True
        return False
    # if destroy_from_hand, search hand and destroy 1 wound.
    # destroy 1 wound card from discard pile if can't find any in hand
    def interact(self, destroy_from_hand):
        if destroy_from_hand:
            for card in self.game_engine.current_player.hand:
                if type(card) == cards.Wound_Card:
                    self.game_engine.current_player.hand.remove(card)
                    self.trashed_cards.append(card)
                    return True
        for card in self.game_engine.current_player.deed_discard_pile:
            if type(card) == cards.Wound_Card:
                self.game_engine.current_player.deed_discard_pile.remove(card)
                self.trashed_cards.append(card)
                return True
        return False        
        
class location_Village(LocationInteractable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
        
# Conquerable Locations
class Location_Monastery(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Keep(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Mage_Tower(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Dungeon(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Tomb(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Monster_Den(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Spawning_Grounds(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Ancient_Ruins(LocationConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
        
# Multiple Conquerable Locations
class Location_Maze(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Labyrinth(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_City_Green(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_City_Red(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_City_White(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_City_Blue(LocationMultipleConquerable):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
        
# Rampaging Enemy Locations
class Location_Draconum(LocationRampagingEnemy):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)
class Location_Orcs(LocationRampagingEnemy):
    def __init__(self, new_game_engine, new_tile_board_zone, new_hex_board_zone):
        super().__init__(new_game_engine, new_tile_board_zone, new_hex_board_zone)


class Locations(object):
    tile_board_zone = None
    location_collection = None
    game_engine = None
     
    def __init__(self, new_game_engine, new_tile_board_zone):
        self.location_collection = []
        self.tile_board_zone = new_tile_board_zone
        self.game_engine = new_game_engine

        # fill location collection with placeholder locations
        for i in range(7):
            self.location_collection.append(Location(self.game_engine, self.tile_board_zone, i))