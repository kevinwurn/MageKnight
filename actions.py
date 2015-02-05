import os
import random
import pygame
import cards
import game
import player

current_folder = os.path.dirname(os.path.abspath(__file__))

class Action(cards.DeedCard):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)    

class Actions(object):
    name = None
    actions_collection = None
    _game_engine = None

    def __init__(self, new_game_engine):
        self._game_engine = new_game_engine
        self.actions_collection = []
        if self._game_engine.current_player == player.ARYTHREA:
            self.actions_collection.append(Card_Arythrea_Battle_Versatility(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Rage(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Determination(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Swiftness(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Swiftness(self._game_engine))
            self.actions_collection.append(Card_Arythrea_March(self._game_engine))
            self.actions_collection.append(Card_Arythrea_March(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Stamina(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Stamina(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Tranquility(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Promise(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Threaten(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Crystalize(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Mana_Pull(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Concentration(self._game_engine))
            self.actions_collection.append(Card_Arythrea_Improvisation(self._game_engine))
        random.shuffle(self.actions_collection)

class Card_Arythrea_Battle_Versatility(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Battle Versatility"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_battle_versatility.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()


class Card_Arythrea_Rage(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Rage"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_rage.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
    def play(self):
        if self._game_engine.battle_phase == game.BATTLE_PHASE_BLOCK:
            self._game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_BLOCK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, game.ELEMENT_PHYSICAL, 2, game.CRYSTAL_NONE))
            return True
        elif self._game_engine.battle_phase == game.BATTLE_PHASE_ATTACK:
            self._game_engine.arythrea.attack.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, game.ELEMENT_PHYSICAL, 2, game.CRYSTAL_NONE))
            return True
        return False
    def play_advanced(self):
        if self._game_engine.arythrea.num_red_tokens > 0:
            self._game_engine.arythrea.num_red_tokens -= 1
            self._game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, game.ELEMENT_PHYSICAL, 4, game.CRYSTAL_NONE))
            return True
        elif self._game_engine.arythrea.num_red_crystals > 0:
            self._game_engine.arythrea.num_red_crystals -= 1
            self._game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, game.ELEMENT_PHYSICAL, 4, game.CRYSTAL_RED))
            return True
        return False
    def undo(self):
        for card_asset in self.game.arythrea.card_assets:
            if card_asset.source_id == self.uid:
                if card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_ADVANCED:
                    if card_asset.crystal_type == game.CRYSTAL_NONE:
                        self._game_engine.arythrea.num_red_tokens += 1
                    elif card_asset.crystal_type == game.CRYSTAL_RED:
                        self._game_engine.arythrea.num_red_crystals += 1
                    self._game_engine.arythrea.card_assets.remove(card_asset)
                    return True
                elif card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED:
                    self._game_engine.arythrea.card_assets.remove(card_asset)
                    return True
        return False

class Card_Arythrea_Determination(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Determination"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_determination.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_Swiftness(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Swiftness"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_swiftness.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_March(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "March"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_march.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Stamina(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Stamina"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_stamina.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Tranquility(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Tranquility"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_tranquility.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Promise(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Promise"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_promise.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Threaten(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Threaten"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_threaten.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Crystalize(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Crystalize"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_crystalize.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_Mana_Pull(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Mana Pull"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_mana_pull.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Concentration(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Concentration"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_concentration.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Improvisation(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Improvisation"
    def load(self):
        self.relative_path_filename = "/assets/images/cards/players/arythrea/card_improvisation.png"
        self.image = pygame.image.load(current_folder + self.relative_path_filename).convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()