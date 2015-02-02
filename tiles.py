import math
import os
import random
import pygame
import hexes
import board

current_folder = os.path.dirname(os.path.abspath(__file__))
TILE_START_WEDGE = 'A'
TILE_START_OPEN = 'B'
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
TILE_BROWN_5_GREEN_CASTLE = 25
TILE_BROWN_6_BLUE_CASTLE = 26
TILE_BROWN_7_WHITE_CASTLE = 27
TILE_BROWN_8_RED_CASTLE = 28
TILE_BROWN_9 = 29
TILE_BROWN_10 = 20

# Placeholder tile
class Tile(pygame.sprite.Sprite):
    type = None
    hexes = None
    location_collection = None
    token_collection = None
    def __init__(self):
        super().__init__()
        self.hexes = hexes.Hexes()    

# normal tile is scanned at 320x335 resize image need to skew image to be a little taller and skinnier
class TileNonPlaceholder(Tile):
    def __init__(self):
        super().__init__()
        self.locations = []
        self.tokens = []
    def fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (117,140))
    def set_location(self, x, y):
        h = (math.sin(math.radians(30))*board.BOARD_HEX_WIDTH)
        self.rect.x = x - board.BOARD_HEX_WIDTH
        self.rect.y = y - 2*board.BOARD_HEX_WIDTH + h/2-6

class Tile_Start_Wedge(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_START_WEDGE
        self.hexes.number = 0
        self.hexes.hex_collection[0] = hexes.Hex_Lake()
        self.hexes.hex_collection[1] = hexes.Hex_Lake()
        self.hexes.hex_collection[2] = hexes.Hex_Lake()
        self.hexes.hex_collection[3] = hexes.Hex_Plain()
        self.hexes.hex_collection[4] = hexes.Hex_Forest()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Plain()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/start_wedge.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Start_Open(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_START_OPEN
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Mountain()
        self.hexes.hex_collection[2] = hexes.Hex_Lake()
        self.hexes.hex_collection[3] = hexes.Hex_Plain()
        self.hexes.hex_collection[4] = hexes.Hex_Forest()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Plain()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/start_open.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_1(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_1
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_1.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_2(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_2
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_2.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_3(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_3
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_3.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_4(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_4
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_4.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_5(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_5
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_5.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_6(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_6
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_6.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_7(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_7
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_7.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_8(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_8
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_8.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_9(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_9
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_9.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_10(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_10
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_10.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_11(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_11
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_11.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_12(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_12
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_12.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_13(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_13
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_13.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Green_14(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_GREEN_14
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_green_14.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_1(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_1
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_1.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_2(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_2
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_2.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_3(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_3
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_3.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_4(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_4
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_4.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_5_Green_Castle(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_5_GREEN_CASTLE
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_5_green_castle.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_6_Blue_Castle(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_6_BLUE_CASTLE
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_6_blue_castle.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_7_White_Castle(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_7_WHITE_CASTLE
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_7_white_castle.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_8_Red_Castle(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_8_RED_CASTLE
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_8_red_castle.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_9(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_9
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_9.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Tile_Brown_10(TileNonPlaceholder):
    def __init__(self):
        super().__init__()
        self.type = TILE_BROWN_10
        self.hexes.hex_collection[0] = hexes.Hex_Plain()
        self.hexes.hex_collection[1] = hexes.Hex_Plain()
        self.hexes.hex_collection[2] = hexes.Hex_Forest()
        self.hexes.hex_collection[3] = hexes.Hex_Forest()
        self.hexes.hex_collection[4] = hexes.Hex_Lake()
        self.hexes.hex_collection[5] = hexes.Hex_Plain()
        self.hexes.hex_collection[6] = hexes.Hex_Forest()
        self.image = pygame.image.load(current_folder +"/assets/images/tiles/tile_brown_10.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Tiles(object):
    tile_collection = None
    tile_group = None
    max_size_tile_collection = None
    green_deck = None
    brown_deck = None
     
    def __init__(self, board_type, mage_knight):
        self.tile_collection = []
        self.green_deck = []
        self.brown_deck = []
        self.tile_group = pygame.sprite.Group()
        self.max_size_tile_collection = board.get_num_board_zones(board_type)

        # build starting tile
        if board_type == board.BOARD_TYPE_WEDGE:
            self.tile_collection.append(Tile_Start_Wedge())
        elif board_type == board.BOARD_TYPE_OPEN:
            self.tile_collection.append(Tile_Start_Open())
            
        # fill tile collection with placeholder tiles
        for i in range(self.max_size_tile_collection):
            self.tile_collection.append(Tile())
            
        # build green deck
        green_tiles_total = []
        brown_tiles_city_total = []
        brown_tiles_non_city_total = []
        green_tiles_total.append(Tile_Green_1())
        green_tiles_total.append(Tile_Green_2())
        green_tiles_total.append(Tile_Green_3())
        green_tiles_total.append(Tile_Green_4())
        green_tiles_total.append(Tile_Green_5())
        green_tiles_total.append(Tile_Green_6())
        green_tiles_total.append(Tile_Green_7())
        green_tiles_total.append(Tile_Green_8())
        green_tiles_total.append(Tile_Green_9())
        green_tiles_total.append(Tile_Green_10())
        green_tiles_total.append(Tile_Green_11())
        green_tiles_total.append(Tile_Green_12())
        green_tiles_total.append(Tile_Green_13())
        green_tiles_total.append(Tile_Green_14())
        brown_tiles_non_city_total.append(Tile_Brown_1())
        brown_tiles_non_city_total.append(Tile_Brown_2())
        brown_tiles_non_city_total.append(Tile_Brown_3())
        brown_tiles_non_city_total.append(Tile_Brown_4())
        brown_tiles_city_total.append(Tile_Brown_5_Green_Castle())
        brown_tiles_city_total.append(Tile_Brown_6_Blue_Castle())
        brown_tiles_city_total.append(Tile_Brown_7_White_Castle())
        brown_tiles_city_total.append(Tile_Brown_8_Red_Castle())
        brown_tiles_non_city_total.append(Tile_Brown_9())
        brown_tiles_non_city_total.append(Tile_Brown_10())
        
        #shuffle all decks
        random.shuffle(green_tiles_total) 
        random.shuffle(brown_tiles_city_total)
        random.shuffle(brown_tiles_non_city_total)
        
        for i in range(mage_knight.num_green_tiles):
            self.green_deck.append(green_tiles_total.pop())
        for i in range(mage_knight.num_brown_non_city_tiles):
            self.brown_deck.append(brown_tiles_non_city_total.pop())
        for i in range(mage_knight.num_brown_city_tiles):
            self.brown_deck.append(brown_tiles_city_total.pop())
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