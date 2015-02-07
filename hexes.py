import game

HEX_PLAIN = 0
HEX_HILL = 1
HEX_FOREST = 2
HEX_WASTELAND = 3
HEX_DESERT = 4
HEX_SWAMP = 5
HEX_LAKE = 6
HEX_MOUNTAIN = 7
HEX_CITY = 8

# base hex placeholder
class Hex(object):
    type = None
    polygon = None
    hex_zone = None
    
    def __init__(self, number):
        super().__init__()
        self.hex_zone = number
# base generic non placeholder class   
class HexNonPlaceholder(Hex):
    def __init__(self, number):
        super().__init__(number)
    
class Hex_Plain(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_PLAIN
    @property
    def movement_cost(self):
        return 2
class Hex_Hill(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_HILL
    @property
    def movement_cost(self):
        return 3
class Hex_Forest(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_FOREST
    def movement_cost(self, time_of_day):
        if time_of_day == game.TIME_DAY:
            return 3
        elif time_of_day == game.TIME_NIGHT:
            return 5
class Hex_Wasteland(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_WASTELAND
    @property
    def movement_cost(self):
        return 4
class Hex_Desert(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_DESERT
    def movement_cost(self, time_of_day):
        if time_of_day == game.TIME_DAY:
            return 5
        elif time_of_day == game.TIME_NIGHT:
            return 3        
class Hex_Swamp(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_SWAMP
    @property
    def movement_cost(self):
        return 5
class Hex_Lake(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_LAKE
    @property
    def movement_cost(self):
        return None
class Hex_Mountain(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_MOUNTAIN
    @property
    def movement_cost(self):
        return None
class Hex_City(HexNonPlaceholder):
    def __init__(self, number):
        super().__init__(number)
        self.type = HEX_CITY
    @property
    def movement_cost(self):
        return 2

class Hexes(object):
    hex_collection = None

    def __init__(self):
        self.hex_collection = []
        for i in range(7):
            self.hex_collection.append(Hex(i))