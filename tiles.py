import math
import os
import pygame
import hexes
import board

current_folder = os.path.dirname(os.path.abspath(__file__))
#COLOR_INVISIBLE = (255, 255, 255)
TILE_START_WEDGE = 'A'
TILE_START_OPEN = 'B'
MAX_SIZE_GREEN_DECK = 7
MAX_SIZE_BROWN_DECK = 4
NUM_CITIES = 2

# Placeholder tile
class Tile(pygame.sprite.Sprite):
    type = None
    hexes = None
    location_collection = None
    token_collection = None
    def __init__(self):
        super().__init__()
        self.hexes = hexes.Hexes()    

# normal tile is scanned at 320x335 resize image (37%x40%) to 118.4x134 - need to stretch image to be a little taller
class TileNonPlaceholder(Tile):
    def __init__(self):
        super().__init__()
        self.location_collection = []
        self.token_collection = []
    def fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (118,134))
    def set_location(self, x, y):
        h = (math.sin(math.radians(30))*board.BOARD_HEX_WIDTH)
        self.rect.x = x - board.BOARD_HEX_WIDTH
        self.rect.y = y - 2*board.BOARD_HEX_WIDTH + h/2-3 

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
        self.hexes.number = 0
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

class Tiles(object):
    tile_collection = None
    tile_group = None
    max_size_tile_collection = None
    green_deck = None
    max_size_green_deck = None
    brown_deck = None
    max_size_brown_deck = None
     
    def __init__(self, board_type):
        self.tile_collection = []
        self.green_deck = []
        self.brown_deck = []
        self.tile_group = pygame.sprite.Group()
        self.max_size_green_deck = MAX_SIZE_GREEN_DECK
        self.max_size_brown_deck = MAX_SIZE_BROWN_DECK
        self.max_size_tile_collection = board.get_num_board_zones(board_type)

        # build starting tile
        if board_type == board.BOARD_TYPE_WEDGE:
            self.tile_collection.append(Tile_Start_Wedge())
        elif board_type == board.BOARD_TYPE_OPEN:
            self.tile_collection.append(Tile_Start_Open())
        self.tile_group.add(self.tile_collection[0])
            
        # fill tile collection with placeholder tiles
        for i in range(self.max_size_tile_collection):
            self.tile_collection.append(Tile())
        
#    draw from green_deck then brown_deck when green_deck empty
#    add Tile to tile_collection
#    def draw(self):
        