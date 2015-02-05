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
    _screen = None
    _game_engine = None
    _game_board = None
    _location_x = None
    _location_y = None
    _player_card = None
    _draw_pile = None
    _discard_pile = None
    _panel_compoents = None
    _player = None
    _x1_offset = None
    _y1_offset = None
    _x2_offset = None
    _y2_offset = None

    def __init__(self, game_screen, new_game_engine, new_game_board):
        super().__init__()
        self._screen = game_screen
        self._game_engine = new_game_engine
        self._game_board = new_game_board
        if self._game_engine.current_player == player.ARYTHREA:
            self._player = self._game_engine.arythrea

        #build panel
        self.image = pygame.Surface([PLAYER_PANEL_WIDTH, PLAYER_PANEL_HEIGHT])
        self.image.fill(PLAYER_PANEL_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self._location_x = main.GAME_SCREEN_WIDTH - PLAYER_PANEL_WIDTH
        self._location_y = 0
        self.rect.x = self._location_x
        self.rect.y = self._location_y

        #set grid up for player panel
        self._x1_offset = self._location_x + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self._y1_offset = self._location_y + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self._x2_offset = self._location_x + PLAYER_PANEL_SPACE_BETWEEN_CARDS
        self._y2_offset = self._location_y + 2*PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_HEIGHT


        #panel_compoenents sprite group        
        self._panel_compoents = pygame.sprite.Group()
        #TOP ROW
        #build player card
        self._player_card = cards.Card_Player(self._game_engine)
        self._add_card_to_top(self._player_card)

        #BOTTOM ROW
        #build discard pile
        self._discard_pile = pygame.sprite.Sprite()
        self._discard_pile.image = pygame.Surface([cards.CARD_WIDTH, cards.CARD_HEIGHT])
        self._discard_pile.image.fill((0,0,0))
        self._discard_pile.rect = self._discard_pile.image.get_rect()
        self._add_card_to_bottom(self._discard_pile)
        
        #add cards from player's hand
        for hand_card in self._player.hand:
            self._add_card_to_bottom(hand_card)

        '''
        #build draw pile
        self._draw_pile = cards.Card_Back()
        self._draw_pile.rect.x = x_offset_for_cards  
        self._draw_pile.rect.y = y_offset_for_cards 
        self.panel_compoents.add(self._draw_pile)
        '''

            
    def _add_card_to_top(self, card):
        card.rect.x = self._x1_offset
        card.rect.y = self._y1_offset
        self._panel_compoents.add(card)
        self._game_engine.sprite_collection.append(card)
        self._x1_offset += PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
        
    def _add_card_to_bottom(self, card):
        card.rect.x = self._x2_offset
        card.rect.y = self._y2_offset
        self._panel_compoents.add(card)
        self._game_engine.sprite_collection.append(card)
        self._x2_offset += PLAYER_PANEL_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
    
    def paint(self):
        pygame.draw.rect(self._screen, PLAYER_PANEL_COLOR, self.rect)
        self._panel_compoents.draw(self._screen)