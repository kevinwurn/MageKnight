import main
import pygame
import game
import mana_die

PANEL_OTHER_COLOR = (160, 160, 160)
PANEL_OTHER_WIDTH = 420
PANEL_OTHER_HEIGHT = 250
PANEL_OTHER_LOCATION_Y = 220
PANEL_OTHER_SPACER_WIDTH = 10

class PanelOther(pygame.sprite.Sprite):
    _screen = None
    _game_engine = None
    _game_board = None
    _panel_components = None
    _dice_components = None
    _location_x = None
    _location_y = None
    _board_day_night = None
    _board_fame_reputation = None

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
        self._location_x = main.GAME_SCREEN_WIDTH - PANEL_OTHER_WIDTH
        self._location_y = PANEL_OTHER_LOCATION_Y 
        self.rect.x = self._location_x 
        self.rect.y = self._location_y 
        
        self._panel_components = pygame.sprite.Group()
        self._dice_components = pygame.sprite.Group()
        
        #place day / night board
        self._board_day_night = pygame.sprite.Sprite()
        if self._game_engine.time_of_day == game.TIME_DAY:
            self._board_day_night.image = pygame.image.load("assets/images/boards/day_board.png")
        elif self._game_engine.time_of_day == game.TIME_NIGHT:
            self._board_day_night.image = pygame.image.load("assets/images/boards/night_board.png")
        self._board_day_night.image = pygame.transform.smoothscale(self._board_day_night.image, (208, 105))
        self._board_day_night.rect = self._board_day_night.image.get_rect()
        self._board_day_night.rect.x = self._location_x + PANEL_OTHER_SPACER_WIDTH
        self._board_day_night.rect.y = self._location_y + PANEL_OTHER_SPACER_WIDTH
        self._panel_components.add(self._board_day_night)
        
        #place fame / reputation board
        '''
        self._board_fame_reputation = pygame.sprite.Sprite() 
        self._board_fame_reputation.image = pygame.image.load("assets/images/boards/fame_reputation_tracker.png")
        self._board_fame_reputation.image = pygame.transform.smoothscale(self._board_fame_reputation.image, (325, 252))
        self._board_fame_reputation.rect = self._board_fame_reputation.image.get_rect()
        self._board_fame_reputation.rect.x = self._location_x + 2*PANEL_OTHER_SPACER_WIDTH + self._board_day_night.rect.width
        self._board_fame_reputation.rect.y = self._location_y + PANEL_OTHER_SPACER_WIDTH
        self._panel_components.add(self._board_fame_reputation)
        '''
        #place mana die
        self._place_die() 
        
    def _place_die(self):
        for i in range(self._game_engine.num_die):
            self._game_engine.mana_dice[i].rect.x = self._location_x + self._board_day_night.rect.width/2 + (i)*(PANEL_OTHER_SPACER_WIDTH + mana_die.DIE_WIDTH)
            self._game_engine.mana_dice[i].rect.y = self._location_y + self._board_day_night.rect.height/2
            self._dice_components.add(self._game_engine.mana_dice[i])
            self._game_engine.magnify_collection.append(self._game_engine.mana_dice[i])
            self._game_engine.dice_group.add(self._game_engine.mana_dice[i])

    def paint(self):
        pygame.draw.rect(self._screen, PANEL_OTHER_COLOR, self.rect)
        self._panel_components.draw(self._screen)
        self._dice_components.draw(self._screen)