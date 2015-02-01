import math
import pygame
import hexes
import board

TILE_START_WEDGE = 0
TILE_START_OPEN = 0

class Tile(object):
    type = None
    tile_hex_collection = None
    
    def __init__(self):
        self.tile_hex_collection = hexes.Hexes()

class Tiles(object):
    tile_collection = None
    max_size_collection = None
    green_deck = None
    brown_deck = None
     
    def __init__(self, board_type):
        self.tile_collection = []
        self.green_deck = []
        self.brown_deck = []
        
        if board_type == board.BOARD_TYPE_WEDGE:
            self.max_size_collection = int((math.pow(board.BOARD_MAX_LEVEL + 1, 2) + board.BOARD_MAX_LEVEL + 1) / 2)
        elif board_type == board.BOARD_TYPE_OPEN:
            self.max_size_collection = int(math.pow(board.BOARD_MAX_LEVEL, 2))

        #build starting tile
        self.tile_collection.append(Tile())
        if board_type == board.BOARD_TYPE_WEDGE:
            self.tile_collection[0].type = TILE_START_WEDGE
        elif board_type == board.BOARD_TYPE_OPEN:
            self.tile_collection[0].type = TILE_START_OPEN
        self.tile_collection[0].tile_hex_collection.number = 0
        
#    draw from green_deck then brown_deck when green_deck empty
#    add Tile to tile_collection
#    def draw(self):
        