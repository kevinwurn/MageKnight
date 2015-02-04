import os
import pygame
import main
import board
import cards


current_folder = os.path.dirname(os.path.abspath(__file__))
PLAYER_PANEL_COLOR = (160, 160, 160)
PLAYER_PANEL_WIDTH = 500
PLAYER_PANEL_HEIGHT = 200


class PlayerPanel(pygame.sprite.Sprite):
    screen = None
    game_engine = None
    game_board = None
    location_x = None
    location_y = None
    player_card = None
    draw_pile = None
    discard_pile = None
    panel_compoents = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self.screen = game_screen
        self.game_engine = new_game_engine
        self.game_board = new_game_board

        #build panel
        self.image = pygame.Surface([PLAYER_PANEL_WIDTH, PLAYER_PANEL_HEIGHT])
        self.image.fill(PLAYER_PANEL_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self.location_x = main.GAME_SCREEN_WIDTH - PLAYER_PANEL_WIDTH
        if self.game_board.board_type == board.BOARD_TYPE_WEDGE:
            self.location_y = 0
        elif self.game_board.board_type == board.BOARD_TYPE_OPEN:
            self.location_y = main.GAME_SCREEN_HEIGHT - PLAYER_PANEL_HEIGHT
        else:
            self.location_y = 0
        self.rect.x = self.location_x
        self.rect.y = self.location_y

        #panel_compoenents sprite group        
        self.panel_compoents = pygame.sprite.Group()
        #build player card
        self.player_card = cards.Card_Player()
        self.player_card.rect.x = self.location_x + 20 
        self.player_card.rect.y = self.location_y + 10
        self.panel_compoents.add(self.player_card)
        
        #build draw pile
        self.draw_pile = cards.Card_Back()
        self.draw_pile.rect.x = self.location_x + 20 
        self.draw_pile.rect.y = self.location_y + 100
        self.panel_compoents.add(self.draw_pile)
        
        #build discard pile
        self.discard_pile = pygame.sprite.Sprite()
        self.discard_pile.image = pygame.Surface([50, 75])
        self.discard_pile.image.fill((0,0,0))
        self.discard_pile.rect = self.discard_pile.image.get_rect()
        self.discard_pile.rect.x = self.location_x + 90 
        self.discard_pile.rect.y = self.location_y + 100
        self.panel_compoents.add(self.discard_pile)
        
    
    def paint(self):
        pygame.draw.rect(self.screen, PLAYER_PANEL_COLOR, self.rect)
        self.panel_compoents.draw(self.screen)