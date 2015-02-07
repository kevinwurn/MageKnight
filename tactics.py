import pygame
import cards

class Tactic(cards.NonDeedCard):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
class Tactics_Day_1_Early_Bird(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Early Bird"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_1_early_bird.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Day_2_Rethink(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Rethink"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_2_rethink.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Day_3_Mana_Steal(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Mana Steal"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_3_mana_steal.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Day_4_Planning(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Planning"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_4_planning.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Day_5_Great_Start(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Great Start"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_5_great_start.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Day_6_The_Right_Moment(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "The Right Moment"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_day_6_the_right_moment.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_1_From_The_Dusk(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "From The Dusk"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_1_from_the_dusk.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_2_Long_Night(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Long Night"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_2_long_night.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_3_Mana_Search(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Mana Search"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_3_mana_search.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_4_Midnight_Meditation(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Midnight Meditation"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_4_midnight_meditation.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_5_Preparation(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Preparation"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_5_preparation.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()
class Tactics_Night_6_Sparing_Power(Tactic):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Sparing Power"
    def load(self):
        self.relative_path_filename = "assets/images/cards/tactics/tactics_night_6_sparing_power.png"
        self.image = pygame.image.load(self.relative_path_filename).convert_alpha()
        self._fit_within_board()
        self.rect = self.image.get_rect()

class Tactics(object):
    tactics_collection = None
    
    def __init__(self):
        self.tactics_collection = []