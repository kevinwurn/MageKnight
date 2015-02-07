import pygame
import main
import cards
import player
import gui_choose_tactics


PANEL_PLAYER_COLOR = (160, 160, 160)
PANEL_PLAYER_WIDTH = 600
PANEL_PLAYER_HEIGHT = 200
PANEL_PLAYER_SPACE_BETWEEN_CARDS = 15


class PanelPlayer(pygame.sprite.Sprite):
    _screen = None
    _game_engine = None
    _game_board = None
    _location_x = None
    _location_y = None
    _player_card = None
    _draw_pile = None
    _btn_start_round = None
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
        if self._game_engine.chosen_player == player.ARYTHREA:
            self._player = self._game_engine.arythrea

        #build panel
        self.image = pygame.Surface([PANEL_PLAYER_WIDTH, PANEL_PLAYER_HEIGHT])
        self.image.fill(PANEL_PLAYER_COLOR)
        self.rect = self.image.get_rect()
        
        #set x, y location of panel
        self._location_x = main.GAME_SCREEN_WIDTH - PANEL_PLAYER_WIDTH
        self._location_y = 0
        self.rect.x = self._location_x
        self.rect.y = self._location_y

        #set grid up for player panel
        self._x1_offset = self._location_x + PANEL_PLAYER_SPACE_BETWEEN_CARDS
        self._y1_offset = self._location_y + PANEL_PLAYER_SPACE_BETWEEN_CARDS
        self._x2_offset = self._location_x + PANEL_PLAYER_SPACE_BETWEEN_CARDS
        self._y2_offset = self._location_y + 2*PANEL_PLAYER_SPACE_BETWEEN_CARDS + cards.CARD_HEIGHT


        #panel_compoenents sprite group        
        self._panel_compoents = pygame.sprite.Group()
        #TOP ROW
        #build player card
        self._player_card = cards.Card_Player(self._game_engine)
        self._player_card.load()
        self._add_card_to_top(self._player_card)

        #BOTTOM ROW
        self._btn_start_round = pygame.sprite.Sprite()
        self._btn_start_round.image = pygame.Surface([cards.CARD_WIDTH, cards.CARD_HEIGHT])
        self._btn_start_round.image.fill((0,0,0))
        self._btn_start_round.rect = self._btn_start_round.image.get_rect()
        start_round_font = pygame.font.Font("fonts/arial.ttf", 12)
        start_round_text_top = start_round_font.render("Start", 1, (255, 255, 255))
        start_round_text_bottom = start_round_font.render("Round", 1, (255, 255, 255))
        start_round_textpos_top = start_round_text_top.get_rect()
        start_round_textpos_bottom = start_round_text_bottom.get_rect()
        start_round_textpos_top.centerx = self._btn_start_round.rect.centerx
        start_round_textpos_top.centery = self._btn_start_round.rect.centery - start_round_text_top.get_rect().size[1]
        start_round_textpos_bottom.centerx = self._btn_start_round.rect.centerx
        start_round_textpos_bottom.centery = self._btn_start_round.rect.centery
        self._add_card_to_bottom(self._btn_start_round)
        self._btn_start_round.image.blit(start_round_text_top, start_round_textpos_top)
        self._btn_start_round.image.blit(start_round_text_bottom, start_round_textpos_bottom)
        
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
        self._game_engine.card_group.add(card)
        self._x1_offset += PANEL_PLAYER_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
        
    def _add_card_to_bottom(self, card):
        card.rect.x = self._x2_offset
        card.rect.y = self._y2_offset
        self._panel_compoents.add(card)
        self._game_engine.sprite_collection.append(card)
        self._game_engine.card_group.add(card)
        self._x2_offset += PANEL_PLAYER_SPACE_BETWEEN_CARDS + cards.CARD_WIDTH
    
    def paint(self):
        pygame.draw.rect(self._screen, PANEL_PLAYER_COLOR, self.rect)
        self._panel_compoents.draw(self._screen)
    
    def check_btn_start_round_clicked(self, mousedown_coordinates):
        if self._btn_start_round.alive():
            if self._btn_start_round.rect.collidepoint(mousedown_coordinates):
                tactics_panel = gui_choose_tactics.GUIChooseTactics(self._screen, self._game_engine)
                tactics_panel.launch()
                if self._game_engine.chosen_player == player.ARYTHREA:
                    self._game_engine.arythrea.tactic = tactics_panel.tactic
                    self._game_engine.arythrea.tactic.load()
                    self._game_engine.arythrea.tactic.rect.x = self._btn_start_round.rect.x
                    self._game_engine.arythrea.tactic.rect.y = self._btn_start_round.rect.y
                    self._game_engine.sprite_collection.append(self._game_engine.arythrea.tactic)
                    self._game_engine.card_group.add(self._game_engine.arythrea.tactic)
                    self._panel_compoents.add(self._game_engine.arythrea.tactic)
                self._btn_start_round.kill()
                self._game_engine.sprite_collection.remove(self._btn_start_round)
        