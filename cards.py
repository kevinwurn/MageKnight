import uuid
import pygame

class Cards(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class DeedCards(Cards):
    mage_knight = None
    uid = None
    
    def __init__(self, mage_knight_game):
        super().__init__()
        self.mage_knight = mage_knight_game
        self.uid = uuid.uuid4()
    
    def discard(self):
        print("discard")

class NonDeedCards(Cards):
    def __init__(self):
        super().__init__()