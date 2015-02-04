import os
import pygame
import main
import board
import cards
import player


current_folder = os.path.dirname(os.path.abspath(__file__))
PLAYER_PANEL_COLOR = (160, 160, 160)
PLAYER_PANEL_WIDTH = 600
PLAYER_PANEL_HEIGHT = 200
PLAYER_PANEL_SPACE_BETWEEN_CARDS = 15


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
    player = None
    x1_offset = None
    y1_offset = None
    x2_offset = None
    y2_offset = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self.screen = game_screen
        self.game_engine = new_game_engine
        self.game_board = new_game_board
        if self.game_engine.current_player == player.ARYTHREA:
            self.player = self.game_engine.arythrea

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

        #set grid up for player panel
        self.x1_offset = self.location_x + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self.y1_offset = self.location_y + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self.x2_offset = self.location_x + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self.y2_offset = self.location_y + 2*PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_HEIGHT


        #panel_compoenents sprite group        
        self.panel_compoents = pygame.sprite.Group()
        #TOP ROW
        #build player card
        self.player_card = cards.Card_Player()
        self.add_card_to_top(self.player_card)

        #BOTTOM ROW
        #build discard pile
        self.discard_pile = pygame.sprite.Sprite()
        self.discard_pile.image = pygame.Surface([cards.CARD_WIDTH, cards.CARD_HEIGHT])
        self.discard_pile.image.fill((0,0,0))
        self.discard_pile.rect = self.discard_pile.image.get_rect()
        self.add_card_to_bottom(self.discard_pile)
        
        #add cards from player's hand
        for hand_card in self.player.hand:
            self.add_card_to_bottom(hand_card)

        '''
        #build draw pile
        self.draw_pile = cards.Card_Back()
        self.draw_pile.rect.x = x_offset_for_cards  
        self.draw_pile.rect.y = y_offset_for_cards 
        self.panel_compoents.add(self.draw_pile)
        '''

            
    def add_card_to_top(self, card):
        card.rect.x = self.x1_offset
        card.rect.y = self.y1_offset
        self.panel_compoents.add(card)
        self.x1_offset += PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
        
    def add_card_to_bottom(self, card):
        card.rect.x = self.x2_offset
        card.rect.y = self.y2_offset
        self.panel_compoents.add(card)
        self.x2_offset += PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
    
    def paint(self):
        pygame.draw.rect(self.screen, PLAYER_PANEL_COLOR, self.rect)
        self.panel_compoents.draw(self.screen)