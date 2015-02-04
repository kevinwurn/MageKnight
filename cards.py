import os
import uuid
import pygame

current_folder = os.path.dirname(os.path.abspath(__file__))
CARD_WIDTH = 50
CARD_HEIGHT = 75

class Card(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    #run after image has loaded
    def fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (CARD_WIDTH, CARD_HEIGHT))
class DeedCard(Card):
    game_engine = None
    uid = None
    
    def __init__(self, game_engine_game):
        super().__init__()
        self.game_engine = game_engine_game
        self.uid = uuid.uuid4()
    def discard(self):
        print("discard")
class NonDeedCard(Card):
    def __init__(self):
        super().__init__()


class Wound_Card(DeedCard):
    def __init__(self):
        super().__init__()
        print("Wound Card")
class Card_Back(Card):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(current_folder +"/assets/images/cards/card_back.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()