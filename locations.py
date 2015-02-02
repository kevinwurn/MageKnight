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
LOCATION_MONASTERY = 9
# Conquerable Locations
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
    def __init__(self):
        super().__init__()

class LocationInteractable(Location):
    def __init__(self):
        super().__init__()
        
class LocationConquerable(Location):
    is_conquered = None
    def __init__(self):
        super().__init__()
        self.is_conquered = False

class LocationMultipleConquerable(Location):
    is_conquered = None
    def __init__(self):
        super().__init__()
        self.is_conquered = []

class LocationRampagingEnemy(Location):
    def __init__(self):
        super().__init__()

class Locations(object):
    location_collection = None
     
    def __init__(self, board_type):
        self.location_collection = []

        # fill location collection with placeholder locations
        for i in range(7):
            self.location_collection.append(Location())