import main
import pygame

PANEL_OTHER_COLOR = (160, 160, 160)
PANEL_OTHER_WIDTH = 350
PANEL_OTHER_HEIGHT = 250
PANEL_OTHER_LOCATION_Y_FOR_WEDGE = 220

class PanelOther(pygame.sprite.Sprite):
    _screen = None
    _game_engine = None
    _game_board = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self._screen = game_screen
        self._game_engine = new_game_engine
        self._game_board = new_game_board

        #build panel
        self.image = pygame.Surface([PANEL_OTHER_WIDTH, PANEL_OTHER_HEIGHT])
        self.image.fill(PANEL_OTHER_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self.rect.x = main.GAME_SCREEN_WIDTH - PANEL_OTHER_WIDTH
        self.rect.y = PANEL_OTHER_LOCATION_Y_FOR_WEDGE

    def paint(self):
        pygame.draw.rect(self._screen, PANEL_OTHER_COLOR, self.rect)