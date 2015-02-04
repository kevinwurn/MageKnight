import main
import board
import pygame

OTHER_PANEL_COLOR = (160, 160, 160)
OTHER_PANEL_WIDTH = 350
OTHER_PANEL_HEIGHT = 250
OTHER_PANEL_LOCATION_Y_FOR_WEDGE = 220

class OtherPanel(pygame.sprite.Sprite):
    screen = None
    game_engine = None
    game_board = None
    location_x = None
    location_y = None
    player_card = None
    panel_compoents = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self.screen = game_screen
        self.game_engine = new_game_engine
        self.game_board = new_game_board

        #build panel
        self.image = pygame.Surface([OTHER_PANEL_WIDTH, OTHER_PANEL_HEIGHT])
        self.image.fill(OTHER_PANEL_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self.location_x = main.GAME_SCREEN_WIDTH - OTHER_PANEL_WIDTH
        if self.game_board.board_type == board.BOARD_TYPE_WEDGE:
            self.location_y = OTHER_PANEL_LOCATION_Y_FOR_WEDGE
        elif self.game_board.board_type == board.BOARD_TYPE_OPEN:
            self.location_y = 0
        else:
            self.location_y = 0
        self.rect.x = self.location_x
        self.rect.y = self.location_y

    def paint(self):
        pygame.draw.rect(self.screen, OTHER_PANEL_COLOR, self.rect)