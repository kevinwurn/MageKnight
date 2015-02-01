import math
import pygame
import main
import tiles
import hexes

BOARD_TYPE_WEDGE = 1
BOARD_TYPE_OPEN = 2
BOARD_HEX_WIDTH = 23
BOARD_MAX_LEVEL = 5

class Board(object):
    board_screen = None
    board_type = None
    board_hex_width = None
    board_hex_border_width = None
    board_color = None
    board_tile_border_color = None
    board_hex_border_color = None
    num_board_zones = None
    board_zones_collection = None 
    tile_collection = None

    def __init__(self, screen, new_board_type):
        self.board_screen = screen
        self.board_type = new_board_type
        self.hex_border_width = 2
        self.board_color = (0, 30, 100) #blue
#        self.tile_border_color = (0, 0, 0) #black
        self.hex_border_color = (100, 100, 100) #grey

        self.tile_collection = tiles.Tiles(self.board_type)

        if self.board_type == BOARD_TYPE_WEDGE:
            self.num_board_zones = int((math.pow(BOARD_MAX_LEVEL + 1, 2) + BOARD_MAX_LEVEL + 1) / 2)
        elif self.board_type == BOARD_TYPE_OPEN:
            self.num_board_zones = int(math.pow(BOARD_MAX_LEVEL, 2))
        self.board_zones_collection = []
        for i in range(self.num_board_zones):
            self.board_zones_collection.append(hexes.Hexes())
            self.board_zones_collection[i].number = i

    def check_board_zone(self, coordinates):
        click_x, click_y = coordinates
        for i in range(self.num_board_zones):
            for j in range(7):
                if self.point_inside_polygon(click_x, click_y, self.board_zones_collection[i].hex_collection[j].polygon):
                    print("Board Zone #: " +str(i)+ " | Hex #: " +str(j))
                    return

    def return_hex_coordinates(self, location_x, location_y):
        pl = [(location_x - BOARD_HEX_WIDTH, location_y),
              (location_x - BOARD_HEX_WIDTH/2, location_y - BOARD_HEX_WIDTH),
              (location_x + BOARD_HEX_WIDTH/2, location_y - BOARD_HEX_WIDTH),
              (location_x + BOARD_HEX_WIDTH, location_y),
              (location_x + BOARD_HEX_WIDTH/2, location_y + BOARD_HEX_WIDTH),
              (location_x - BOARD_HEX_WIDTH/2, location_y + BOARD_HEX_WIDTH)]
        return pl
    
    # determine if a point is inside a given polygon or not
    # Polygon is a list of (x,y) pairs.
    # http://www.ariel.com.au/a/python-point-int-poly.html
    def point_inside_polygon(self, x,y,poly):
        n = len(poly)
        inside =False

        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside

    def build_tile_holder(self, zone_num, color, location_x, location_y):
        hex1x = location_x
        hex1y = location_y
        hex2x = location_x + 1.5*BOARD_HEX_WIDTH
        hex2y = location_y - BOARD_HEX_WIDTH
        hex3x = hex2x + 1.5*BOARD_HEX_WIDTH
        hex3y = location_y
        hex4x = hex3x
        hex4y = hex3y + 2*BOARD_HEX_WIDTH
        hex5x = hex2x
        hex5y = hex2y + 4*BOARD_HEX_WIDTH
        hex6x = hex1x
        hex6y = hex2y + 3*BOARD_HEX_WIDTH
        hex7x = hex2x
        hex7y = hex2y + 2*BOARD_HEX_WIDTH
        for i in range(1, 8):
            exec("pl" + str(i) + " = self.return_hex_coordinates(hex" + str(i) + "x, hex" + str(i) + "y)")
            self.board_zones_collection[zone_num].hex_collection[i-1].polygon = eval('pl' + str(i))
            pygame.draw.polygon(self.board_screen, color, eval('pl' + str(i)))
            pygame.draw.polygon(self.board_screen, self.hex_border_color, eval('pl' + str(i)), self.hex_border_width)

    def build(self):
        h = (math.sin(math.radians(30))*BOARD_HEX_WIDTH)

        if self.board_type == BOARD_TYPE_WEDGE:
            #level 0
            x0 = BOARD_HEX_WIDTH
            y0 = 2*BOARD_HEX_WIDTH
            self.build_tile_holder(0, self.board_color, x0, y0)

            board_zone_num = 0
            first_time_num_for_current_level = 0
            first_board_zone_num_on_previous_level = 0
            for level in range(1, BOARD_MAX_LEVEL+1):
                for board_zone_num_for_level in range(level+1):
                    board_zone_num += 1
                    # if drawing the last tile for the level
                    if board_zone_num_for_level == level:
                        exec("x" +str(board_zone_num)+ " = 3*h+3*BOARD_HEX_WIDTH+x" +str(board_zone_num-level-1))
                        exec("y" +str(board_zone_num)+ " = BOARD_HEX_WIDTH+y" +str(board_zone_num-level-1))
                    # if drawing the first tile for the level
                    elif board_zone_num_for_level == 0:
                        exec("x" +str(board_zone_num)+ " = h+BOARD_HEX_WIDTH+x" +str(first_board_zone_num_on_previous_level+board_zone_num_for_level))
                        exec("y" +str(board_zone_num)+ " = 5*BOARD_HEX_WIDTH+y" +str(first_board_zone_num_on_previous_level+board_zone_num_for_level))
                        first_time_num_for_current_level = first_board_zone_num_on_previous_level 
                        first_board_zone_num_on_previous_level = board_zone_num
                    # if drawing all other tiles
                    else:
                        exec("x" +str(board_zone_num)+ " = h+BOARD_HEX_WIDTH+x" +str(first_time_num_for_current_level+board_zone_num_for_level))
                        exec("y" +str(board_zone_num)+ " = 5*BOARD_HEX_WIDTH+y" +str(first_time_num_for_current_level+board_zone_num_for_level))
                    self.build_tile_holder(board_zone_num, eval("[i + 20 * " +str(level)+ " for i in self.board_color]"), eval("x" +str(board_zone_num)), eval("y" +str(board_zone_num)))

        elif self.board_type == BOARD_TYPE_OPEN:
            #level 0
            x0 = main.SCREEN_WIDTH/2 + h + BOARD_HEX_WIDTH
            y0 = 2*BOARD_HEX_WIDTH
            self.build_tile_holder(0, self.board_color, x0, y0)
            
            board_zone_num = 0
            first_time_num_for_current_level = 0
            first_board_zone_num_on_previous_level = 0
            max_board_zone_num_increment=0
            for level in range(1, BOARD_MAX_LEVEL+1):
                for board_zone_num_for_level in range(level+max_board_zone_num_increment+2):
                    board_zone_num += 1
                    # if drawing the last tile for the level
                    if board_zone_num_for_level == level+max_board_zone_num_increment+1:
                        exec("x" +str(board_zone_num)+ " = 2*h+2*BOARD_HEX_WIDTH+x" +str(board_zone_num-level-max_board_zone_num_increment-2))
                        exec("y" +str(board_zone_num)+ " = 4*BOARD_HEX_WIDTH+y" +str(board_zone_num-level-max_board_zone_num_increment-2))
                        max_board_zone_num_increment += 1
                    # if drawing the first tile for the level
                    elif board_zone_num_for_level == 0:
                        exec("x" +str(board_zone_num)+ " = -3*h-3*BOARD_HEX_WIDTH+x" +str(first_board_zone_num_on_previous_level+board_zone_num_for_level))
                        exec("y" +str(board_zone_num)+ " = BOARD_HEX_WIDTH+y" +str(first_board_zone_num_on_previous_level+board_zone_num_for_level))
                        first_time_num_for_current_level = first_board_zone_num_on_previous_level 
                        first_board_zone_num_on_previous_level = board_zone_num
                    # if drawing the second tile for the level
                    elif board_zone_num_for_level == 1:
                        exec("x" +str(board_zone_num)+ " = -h-BOARD_HEX_WIDTH+x" +str(first_time_num_for_current_level))
                        exec("y" +str(board_zone_num)+ " = 5*BOARD_HEX_WIDTH+y" +str(first_time_num_for_current_level))
                    # if drawing all other tiles
                    else:
                        exec("x" +str(board_zone_num)+ " = -h-BOARD_HEX_WIDTH+x" +str(first_time_num_for_current_level+board_zone_num_for_level-1))
                        exec("y" +str(board_zone_num)+ " = 5*BOARD_HEX_WIDTH+y" +str(first_time_num_for_current_level+board_zone_num_for_level-1))
                    self.build_tile_holder(board_zone_num, eval("[i + 20 * " +str(level)+ " for i in self.board_color]"), eval("x" +str(board_zone_num)), eval("y" +str(board_zone_num)))