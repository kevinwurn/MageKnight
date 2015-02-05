import main
import board
import pygame

OTHER_PANEL_COLOR = (160, 160, 160)
OTHER_PANEL_WIDTH = 350
OTHER_PANEL_HEIGHT = 250
OTHER_PANEL_LOCATION_Y_FOR_WEDGE = 220

class OtherPanel(pygame.sprite.Sprite):
    _screen = None
    _game_engine = None
    _game_board = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self._screen = game_screen
        self._game_engine = new_game_engine
        self._game_board = new_game_board

        #build panel
        self.image = pygame.Surface([OTHER_PANEL_WIDTH, OTHER_PANEL_HEIGHT])
        self.image.fill(OTHER_PANEL_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self.rect.x = main.GAME_SCREEN_WIDTH - OTHER_PANEL_WIDTH
        self.rect.y = OTHER_PANEL_LOCATION_Y_FOR_WEDGE

    def paint(self):
        pygame.draw.rect(self._screen, OTHER_PANEL_COLOR, self.rect)