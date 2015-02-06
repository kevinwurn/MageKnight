import uuid
import pygame

CARD_WIDTH = 50
CARD_HEIGHT = 75

class Card(pygame.sprite.Sprite):
    _game_engine = None
    relative_path_filename = None
    
    def __init__(self, new_game_engine):
        super().__init__()
        self._game_engine = new_game_engine
    #run after image has loaded
    def fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (CARD_WIDTH, CARD_HEIGHT))
class DeedCard(Card):
    uid = None
    
    def __init__(self, new_engine_game):
        super().__init__(new_engine_game)
        self.uid = uuid.uuid4()
    def discard(self):
        print("discard")
class NonDeedCard(Card):
    def __init__(self, new_engine_game):
        super().__init__(new_engine_game)


class Wound_Card(DeedCard):
    def __init__(self, new_engine_game):
        super().__init__(new_engine_game)
        print("Wound Card")
class Card_Back(Card):
    def __init__(self, new_engine_game):
        super().__init__(new_engine_game)
    def load(self):
        self.relative_path_filename = "assets/images/cards/card_back.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
class Card_Player(Card):
    # for now default to arythrea.  currently many ways to do this.  not sure the best way yet.
    def __init__(self, new_engine_game):
        super().__init__(new_engine_game)
    def load(self):
        self.relative_path_filename = "assets/images/cards/players/arythrea/card_arythrea.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()    