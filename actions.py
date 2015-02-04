import os
import random
import pygame
import cards
import game
import player

current_folder = os.path.dirname(os.path.abspath(__file__))
CARD_ARYTHREA_BATTLE_VERSATILITY = 1
CARD_ARYTHREA_RAGE = 2
CARD_ARYTHREA_DETERMINATION = 3
CARD_ARYTHREA_SWIFTNESS = 4 # x 2
CARD_ARYTHREA_MARCH = 6 # x 2
CARD_ARYTHREA_STAMINA = 8 # x 2
CARD_ARYTHREA_TRANQUILITY = 10
CARD_ARYTHREA_PROMISE = 11
CARD_ARYTHREA_THREATEN = 12
CARD_ARYTHREA_CRYSTALIZE = 13
CARD_ARYTHREA_MANA_PULL = 14
CARD_ARYTHREA_CONCENTRATION = 15
CARD_ARYTHREA_IMPROVISATION = 16


class Action(cards.DeedCard):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)    

class Actions(object):
    name = None
    actions_collection = None
    game_engine = None

    def __init__(self, new_game_engine):
        self.game_engine = new_game_engine
        self.actions_collection = []
        if self.game_engine.current_player == player.ARYTHREA:
            self.actions_collection.append(Card_Arythrea_Battle_Versatility(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Rage(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Determination(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Swiftness(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Swiftness(self.game_engine))
            self.actions_collection.append(Card_Arythrea_March(self.game_engine))
            self.actions_collection.append(Card_Arythrea_March(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Stamina(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Stamina(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Tranquility(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Promise(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Threaten(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Crystalize(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Mana_Pull(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Concentration(self.game_engine))
            self.actions_collection.append(Card_Arythrea_Improvisation(self.game_engine))
        random.shuffle(self.actions_collection)

class Card_Arythrea_Battle_Versatility(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Battle Versatility"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_battle_versatility.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_Rage(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Rage"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_rage.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
    def play(self):
        if self.game_engine.battle_phase == game.BATTLE_PHASE_BLOCK:
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_BLOCK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, game.ELEMENT_PHYSICAL, 2, game.CRYSTAL_NONE))
            return True
        elif self.game_engine.battle_phase == game.BATTLE_PHASE_ATTACK:
            self.game_engine.arythrea.attack.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, game.ELEMENT_PHYSICAL, 2, game.CRYSTAL_NONE))
            return True
        return False
    def play_advanced(self):
        if self.game_engine.arythrea.num_red_tokens > 0:
            self.game_engine.arythrea.num_red_tokens -= 1
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, game.ELEMENT_PHYSICAL, 4, game.CRYSTAL_NONE))
            return True
        elif self.game_engine.arythrea.num_red_crystals > 0:
            self.game_engine.arythrea.num_red_crystals -= 1
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, game.ELEMENT_PHYSICAL, 4, game.CRYSTAL_RED))
            return True
        return False
    def undo(self):
        for card_asset in self.game.arythrea.card_assets:
            if card_asset.source_id == self.uid:
                if card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_ADVANCED:
                    if card_asset.crystal_type == game.CRYSTAL_NONE:
                        self.game_engine.arythrea.num_red_tokens += 1
                    elif card_asset.crystal_type == game.CRYSTAL_RED:
                        self.game_engine.arythrea.num_red_crystals += 1
                    self.game_engine.arythrea.card_assets.remove(card_asset)
                    return True
                elif card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED:
                    self.game_engine.arythrea.card_assets.remove(card_asset)
                    return True
        return False

class Card_Arythrea_Determination(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Determination"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_determination.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_Swiftness(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Swiftness"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_swiftness.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_March(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "March"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_march.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Stamina(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Stamina"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_stamina.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Tranquility(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Tranquility"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_tranquility.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Promise(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Promise"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_promise.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Threaten(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Threaten"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_threaten.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Crystalize(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Crystalize"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_crystalize.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()

class Card_Arythrea_Mana_Pull(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Mana Pull"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_mana_pull.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Concentration(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Concentration"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_concentration.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()
        
class Card_Arythrea_Improvisation(Action):
    def __init__(self, new_game_engine):
        super().__init__(new_game_engine)
        self.name = "Improvisation"
        self.image = pygame.image.load(current_folder +"/assets/images/cards/players/arythrea/card_improvisation.png").convert_alpha()
        self.fit_within_board()
        self.rect = self.image.get_rect()