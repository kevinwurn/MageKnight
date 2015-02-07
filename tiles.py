import math
import random
import pygame
import board
import hexes
import locations

TILE_START_WEDGE = 0
TILE_GREEN_1 = 1
TILE_GREEN_2 = 2
TILE_GREEN_3 = 3
TILE_GREEN_4 = 4
TILE_GREEN_5 = 5
TILE_GREEN_6 = 6
TILE_GREEN_7 = 7
TILE_GREEN_8 = 8
TILE_GREEN_9 = 9
TILE_GREEN_10 = 10
TILE_GREEN_11 = 11
TILE_GREEN_12 = 12
TILE_GREEN_13 = 13
TILE_GREEN_14 = 14
TILE_BROWN_1 = 21
TILE_BROWN_2 = 22
TILE_BROWN_3 = 23
TILE_BROWN_4 = 24
TILE_BROWN_5_GREEN_CITY = 25
TILE_BROWN_6_BLUE_CITY = 26
TILE_BROWN_7_WHITE_CITY = 27
TILE_BROWN_8_RED_CITY = 28
TILE_BROWN_9 = 29
TILE_BROWN_10 = 20

# Placeholder tile
class Tile(pygame.sprite.Sprite):
    tile_board_zone = None
    type = None
    relative_path_filename = None
    hexes = None
    location_collection = None
    token_collection = None
    def __init__(self):
        super().__init__()
        self.hexes = hexes.Hexes()    

class TileNonPlaceholder(Tile):
    _game_engine = None
    walls = None
    city_level = None
    def __init__(self, new_game_engine):
        super().__init__()
        self._game_engine = new_game_engine
        self.walls = Walls()
        self.location_collection = locations.Locations(self._game_engine, None)
        self.token_collection = []
        self.city_level = 0
    # need to skew image to be a little taller and skinnier
    def _fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (115,137))
    def set_board_location(self, x, y):
        h = (math.sin(math.radians(30))*board.BOARD_HEX_WIDTH)
        self.rect.x = x - board.BOARD_HEX_WIDTH + 1
        self.rect.y = y - 2*board.BOARD_HEX_WIDTH + h/2-4
        
class Walls(object):
    wall_collection = None
    def __init__(self):
        self.wall_collection = []
    def add_wall(self, num_hex_1, num_hex_2):
        self.wall_collection.append(Wall(num_hex_1, num_hex_2))
    def return_if_cross_wall(self, num_hex_1, num_hex_2):
        if self.wall_collection:
            for w in self.wall_collection:
                if w.num_hex_1 == num_hex_1 and w.num_hex_2 == num_hex_2:
                    return True
                elif w.num_hex_1 == num_hex_2 and w.num_hex_2 == num_hex_1:
                    return True
        return False
class Wall(object):
    _num_hex_1 = None
    _num_hex_2 = None
    def __init__(self, new_num_hex_1, new_num_hex_2):
        self._num_hex_1 = new_num_hex_1
        self._num_hex_2 = new_num_hex_2

class Tile_Start_Wedge(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_START_WEDGE
        self.hexes.number = 0
        self.hexes.hex_collection[0] = hexes.Hex_Lake(0)
        self.hexes.hex_collection[1] = hexes.Hex_Lake(1)
        self.hexes.hex_collection[2] = hexes.Hex_Lake(2)
        self.hexes.hex_collection[3] = hexes.Hex_Plain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Plain(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_start_wedge.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_1(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_1
        self.hexes.hex_collection[0] = hexes.Hex_Plain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Forest(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Lake(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Forest(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_1.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_2(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_2
        self.hexes.hex_collection[0] = hexes.Hex_Plain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Plain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Hill(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Hill(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_2.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_3(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_3
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Plain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Plain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Hill(4)
        self.hexes.hex_collection[5] = hexes.Hex_Hill(5)
        self.hexes.hex_collection[6] = hexes.Hex_Forest(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_3.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_4(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_4
        self.hexes.hex_collection[0] = hexes.Hex_Plain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Hill(2)
        self.hexes.hex_collection[3] = hexes.Hex_Desert(3)
        self.hexes.hex_collection[4] = hexes.Hex_Desert(4)
        self.hexes.hex_collection[5] = hexes.Hex_Mountain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Desert(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_4.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_5(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_5
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Forest(1)
        self.hexes.hex_collection[2] = hexes.Hex_Forest(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Plain(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Lake(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_5.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_6(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_6
        self.hexes.hex_collection[0] = hexes.Hex_Forest(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Hill(2)
        self.hexes.hex_collection[3] = hexes.Hex_Mountain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Hill(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_6.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_7(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_7
        self.hexes.hex_collection[0] = hexes.Hex_Plain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Plain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Lake(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Forest(5)
        self.hexes.hex_collection[6] = hexes.Hex_Swamp(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_7.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_8(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_8
        self.hexes.hex_collection[0] = hexes.Hex_Swamp(0)
        self.hexes.hex_collection[1] = hexes.Hex_Swamp(1)
        self.hexes.hex_collection[2] = hexes.Hex_Forest(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Swamp(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_8.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_9(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_9
        self.hexes.hex_collection[0] = hexes.Hex_Plain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Wasteland(1)
        self.hexes.hex_collection[2] = hexes.Hex_Plain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Wasteland(3)
        self.hexes.hex_collection[4] = hexes.Hex_Mountain(4)
        self.hexes.hex_collection[5] = hexes.Hex_Wasteland(5)
        self.hexes.hex_collection[6] = hexes.Hex_Mountain(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_9.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_10(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_10
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Hill(2)
        self.hexes.hex_collection[3] = hexes.Hex_Hill(3)
        self.hexes.hex_collection[4] = hexes.Hex_Forest(4)
        self.hexes.hex_collection[5] = hexes.Hex_Plain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Mountain(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_10.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_11(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_11
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Lake(1)
        self.hexes.hex_collection[2] = hexes.Hex_Plain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Hill(3)
        self.hexes.hex_collection[4] = hexes.Hex_Lake(4)
        self.hexes.hex_collection[5] = hexes.Hex_Lake(5)
        self.hexes.hex_collection[6] = hexes.Hex_Plain(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_11.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_12(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_12
        self.hexes.hex_collection[0] = hexes.Hex_Mountain(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Hill(2)
        self.hexes.hex_collection[3] = hexes.Hex_Mountain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Swamp(4)
        self.hexes.hex_collection[5] = hexes.Hex_Hill(5)
        self.hexes.hex_collection[6] = hexes.Hex_Plain(6)
        self.walls.add_wall(1, 6)
        self.walls.add_wall(2, 6)
        self.walls.add_wall(5, 6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_12.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_13(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_13
        self.hexes.hex_collection[0] = hexes.Hex_Forest(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Swamp(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Hill(4)
        self.hexes.hex_collection[5] = hexes.Hex_Lake(5)
        self.hexes.hex_collection[6] = hexes.Hex_Forest(6)
        self.walls.add_wall(3, 4)
        self.walls.add_wall(4, 6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_13.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_14(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_GREEN_14
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Plain(1)
        self.hexes.hex_collection[2] = hexes.Hex_Desert(2)
        self.hexes.hex_collection[3] = hexes.Hex_Desert(3)
        self.hexes.hex_collection[4] = hexes.Hex_Plain(4)
        self.hexes.hex_collection[5] = hexes.Hex_Wasteland(5)
        self.hexes.hex_collection[6] = hexes.Hex_Plain(6)
        self.walls.add_wall(4, 6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_green_14.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_1(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_1
        self.hexes.hex_collection[0] = hexes.Hex_Desert(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Hill(2)
        self.hexes.hex_collection[3] = hexes.Hex_Mountain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Desert(4)
        self.hexes.hex_collection[5] = hexes.Hex_Desert(5)
        self.hexes.hex_collection[6] = hexes.Hex_Desert(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_1.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_2(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_2
        self.hexes.hex_collection[0] = hexes.Hex_Swamp(0)
        self.hexes.hex_collection[1] = hexes.Hex_Swamp(1)
        self.hexes.hex_collection[2] = hexes.Hex_Forest(2)
        self.hexes.hex_collection[3] = hexes.Hex_Lake(3)
        self.hexes.hex_collection[4] = hexes.Hex_Swamp(4)
        self.hexes.hex_collection[5] = hexes.Hex_Hill(5)
        self.hexes.hex_collection[6] = hexes.Hex_Lake(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_2.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_3(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_3
        self.hexes.hex_collection[0] = hexes.Hex_Wasteland(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Wasteland(2)
        self.hexes.hex_collection[3] = hexes.Hex_Mountain(3)
        self.hexes.hex_collection[4] = hexes.Hex_Wasteland(4)
        self.hexes.hex_collection[5] = hexes.Hex_Hill(5)
        self.hexes.hex_collection[6] = hexes.Hex_Wasteland(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_3.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_4(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_4
        self.hexes.hex_collection[0] = hexes.Hex_Wasteland(0)
        self.hexes.hex_collection[1] = hexes.Hex_Wasteland(1)
        self.hexes.hex_collection[2] = hexes.Hex_Wasteland(2)
        self.hexes.hex_collection[3] = hexes.Hex_Hill(3)
        self.hexes.hex_collection[4] = hexes.Hex_Hill(4)
        self.hexes.hex_collection[5] = hexes.Hex_Wasteland(5)
        self.hexes.hex_collection[6] = hexes.Hex_Mountain(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_4.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_5_Green_City(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_5_GREEN_CITY
        self.hexes.hex_collection[0] = hexes.Hex_Swamp(0)
        self.hexes.hex_collection[1] = hexes.Hex_Forest(1)
        self.hexes.hex_collection[2] = hexes.Hex_Lake(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Swamp(4)
        self.hexes.hex_collection[5] = hexes.Hex_Swamp(5)
        self.hexes.hex_collection[6] = hexes.Hex_City(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_5_green_city.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_6_Blue_City(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_6_BLUE_CITY
        self.hexes.hex_collection[0] = hexes.Hex_Lake(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Mountain(2)
        self.hexes.hex_collection[3] = hexes.Hex_Forest(3)
        self.hexes.hex_collection[4] = hexes.Hex_Plain(4)
        self.hexes.hex_collection[5] = hexes.Hex_Lake(5)
        self.hexes.hex_collection[6] = hexes.Hex_City(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_6_blue_city.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_7_White_City(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_7_WHITE_CITY
        self.hexes.hex_collection[0] = hexes.Hex_Lake(0)
        self.hexes.hex_collection[1] = hexes.Hex_Lake(1)
        self.hexes.hex_collection[2] = hexes.Hex_Wasteland(2)
        self.hexes.hex_collection[3] = hexes.Hex_Wasteland(3)
        self.hexes.hex_collection[4] = hexes.Hex_Plain(4)
        self.hexes.hex_collection[5] = hexes.Hex_Forest(5)
        self.hexes.hex_collection[6] = hexes.Hex_City(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_7_white_city.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_8_Red_City(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_8_RED_CITY
        self.hexes.hex_collection[0] = hexes.Hex_Desert(0)
        self.hexes.hex_collection[1] = hexes.Hex_Wasteland(1)
        self.hexes.hex_collection[2] = hexes.Hex_Desert(2)
        self.hexes.hex_collection[3] = hexes.Hex_Desert(3)
        self.hexes.hex_collection[4] = hexes.Hex_Hill(4)
        self.hexes.hex_collection[5] = hexes.Hex_Desert(5)
        self.hexes.hex_collection[6] = hexes.Hex_City(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_8_red_city.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_9(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_9
        self.hexes.hex_collection[0] = hexes.Hex_Desert(0)
        self.hexes.hex_collection[1] = hexes.Hex_Desert(1)
        self.hexes.hex_collection[2] = hexes.Hex_Wasteland(2)
        self.hexes.hex_collection[3] = hexes.Hex_Hill(3)
        self.hexes.hex_collection[4] = hexes.Hex_Hill(4)
        self.hexes.hex_collection[5] = hexes.Hex_Mountain(5)
        self.hexes.hex_collection[6] = hexes.Hex_Plain(6)
        self.walls.add_wall(0, 5)
        self.walls.add_wall(0, 6)
        self.walls.add_wall(1, 6)
        self.walls.add_wall(2, 6)
        self.walls.add_wall(2, 3)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_9.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_10(TileNonPlaceholder):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.type = TILE_BROWN_10
        self.hexes.hex_collection[0] = hexes.Hex_Hill(0)
        self.hexes.hex_collection[1] = hexes.Hex_Hill(1)
        self.hexes.hex_collection[2] = hexes.Hex_Forest(2)
        self.hexes.hex_collection[3] = hexes.Hex_Swamp(3)
        self.hexes.hex_collection[4] = hexes.Hex_Lake(4)
        self.hexes.hex_collection[5] = hexes.Hex_Forest(5)
        self.hexes.hex_collection[6] = hexes.Hex_Swamp(6)
    def load(self):
        self.relative_path_filename = "assets/images/tiles/tile_brown_10.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()

class Tiles(object):
    _game_engine = None
    tile_collection = None
    max_size_tile_collection = None
    green_deck = None
    brown_deck = None
     
    def __init__(self, new_game_engine):
        self._game_engine = new_game_engine
        self.tile_collection = []
        self.green_deck = []
        self.brown_deck = []
        self.tile_group = pygame.sprite.Group()
        self.max_size_tile_collection = board.get_num_board_zones()

        # build starting tile
        tile = Tile_Start_Wedge(self._game_engine)
        tile.load()
        self.tile_collection.append(tile)
        self._game_engine.sprite_collection.append(tile)
        self._game_engine.tile_group.add(tile)
            
        # fill tile collection with placeholder tiles
        for i in range(self.max_size_tile_collection):
            self.tile_collection.append(Tile())
            
        # build green deck
        green_tiles_total = []
        brown_tiles_city_total = []
        brown_tiles_non_city_total = []
        green_tiles_total.append(Tile_Green_1(self._game_engine))
        green_tiles_total.append(Tile_Green_2(self._game_engine))
        green_tiles_total.append(Tile_Green_3(self._game_engine))
        green_tiles_total.append(Tile_Green_4(self._game_engine))
        green_tiles_total.append(Tile_Green_5(self._game_engine))
        green_tiles_total.append(Tile_Green_6(self._game_engine))
        green_tiles_total.append(Tile_Green_7(self._game_engine))
        green_tiles_total.append(Tile_Green_8(self._game_engine))
        green_tiles_total.append(Tile_Green_9(self._game_engine))
        green_tiles_total.append(Tile_Green_10(self._game_engine))
        green_tiles_total.append(Tile_Green_11(self._game_engine))
        green_tiles_total.append(Tile_Green_12(self._game_engine))
        green_tiles_total.append(Tile_Green_13(self._game_engine))
        green_tiles_total.append(Tile_Green_14(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_1(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_2(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_3(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_4(self._game_engine))
        brown_tiles_city_total.append(Tile_Brown_5_Green_City(self._game_engine))
        brown_tiles_city_total.append(Tile_Brown_6_Blue_City(self._game_engine))
        brown_tiles_city_total.append(Tile_Brown_7_White_City(self._game_engine))
        brown_tiles_city_total.append(Tile_Brown_8_Red_City(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_9(self._game_engine))
        brown_tiles_non_city_total.append(Tile_Brown_10(self._game_engine))
        
        #shuffle all decks
        random.shuffle(green_tiles_total) 
        random.shuffle(brown_tiles_city_total)
        random.shuffle(brown_tiles_non_city_total)
        
        #also add tiles to game engine sprite collection
        for i in range(self._game_engine.num_green_tiles):
            tile = green_tiles_total.pop()
            self.green_deck.append(tile)
        for i in range(self._game_engine.num_brown_non_city_tiles):
            tile = brown_tiles_non_city_total.pop()
            self.brown_deck.append(tile)
        for i in range(self._game_engine.num_brown_city_tiles):
            tile = brown_tiles_city_total.pop()
            self.brown_deck.append(tile)
        #shuffle brown deck one more time
        random.shuffle(self.brown_deck)

    # draw from green_deck then brown_deck when green_deck empty
    def draw(self):
        tile = None
        # if no green tiles left draw from brown tiles.  if no brown tiles, then return None
        if self.green_deck:
            tile = self.green_deck.pop()
        elif self.brown_deck:
            tile = self.brown_deck.pop()
        return tile