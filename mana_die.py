import random
import pygame

DIE_GOLD = 0
DIE_RED = 1
DIE_BLUE = 2
DIE_GREEN = 3
DIE_WHITE = 4
DIE_BLACK = 5

DIE_WIDTH = 15

class ManaDie(pygame.sprite.Sprite):
    relative_path_filename = None
    face = None
    
    def __init__(self):
        super().__init__()
        
    def _load(self):
        if self.face == DIE_GOLD:
            self.relative_path_filename = "assets/images/mana die/gold.png"
        elif self.face == DIE_RED:
            self.relative_path_filename = "assets/images/mana die/red.png"
        elif self.face == DIE_BLUE:
            self.relative_path_filename = "assets/images/mana die/blue.png"
        elif self.face == DIE_GREEN:
            self.relative_path_filename = "assets/images/mana die/green.png"
        elif self.face == DIE_WHITE:
            self.relative_path_filename = "assets/images/mana die/white.png"
        elif self.face == DIE_BLACK:
            self.relative_path_filename = "assets/images/mana die/black.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()

    def _fit_within_board(self):
        self.image = pygame.transform.smoothscale(self.image, (DIE_WIDTH, DIE_WIDTH))
    
    def roll(self):
        self.face = random.randint(0, 5)
        self._load()