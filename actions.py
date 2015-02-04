import cards
import game
import player

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


class Actions(cards.DeedCard):
    name = None

    def __init__(self):
        super().__init__()

class Card_Arythrea_Battle_Versatility(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Battle Versatility"

class Card_Arythrea_Rage(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Rage"
    def play(self):
        if self.game_engine.battle_phase == game.BATTLE_PHASE_BLOCK:
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_BLOCK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, player.ELEMENT_PHYSICAL, 2, player.CRYSTAL_NONE))
            return True
        elif self.game_engine.battle_phase == game.BATTLE_PHASE_ATTACK:
            self.game_engine.arythrea.attack.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED, player.ELEMENT_PHYSICAL, 2, player.CRYSTAL_NONE))
            return True
        return False
    def play_advanced(self):
        if self.game_engine.arythrea.num_red_tokens > 0:
            self.game_engine.arythrea.num_red_tokens -= 1
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, player.ELEMENT_PHYSICAL, 4, player.CRYSTAL_NONE))
            return True
        elif self.game_engine.arythrea.num_red_crystals > 0:
            self.game_engine.arythrea.num_red_crystals -= 1
            self.game_engine.arythrea.battle_assets.append(player.CardAsset(self.uid, player.CARD_ASSET_TYPE_ATTACK, player.CARD_ASSET_ACTION_TYPE_ADVANCED, player.ELEMENT_PHYSICAL, 4, player.CRYSTAL_RED))
            return True
        return False
    def undo(self):
        for card_asset in self.game.arythrea.card_assets:
            if card_asset.source_id == self.uid:
                if card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_ADVANCED:
                    if card_asset.crystal_type == player.CRYSTAL_NONE:
                        self.game_engine.arythrea.num_red_tokens += 1
                    elif card_asset.crystal_type == player.CRYSTAL_RED:
                        self.game_engine.arythrea.num_red_crystals += 1
                    self.game_engine.arythrea.card_assets.remove(card_asset)
                    return True
                elif card_asset.action_type == player.CARD_ASSET_ACTION_TYPE_NON_ADVANCED:
                    self.game_engine.arythrea.card_assets.remove(card_asset)
                    return True
        return False

class Card_Arythrea_Determination(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Determination"

class Card_Arythrea_Swiftness(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Swiftness"

class Card_Arythrea_March(Actions):
    def __init__(self):
        super().__init__()
        self.name = "March"
        
class Card_Arythrea_Stamina(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Stamina"
        
class Card_Arythrea_Tranquility(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Tranquility"
        
class Card_Arythrea_Promise(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Promise"
        
class Card_Arythrea_Threaten(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Threaten"
        
class Card_Arythrea_Crystalize(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Crystalize"

class Card_Arythrea_Mana_Pull(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Mana Pull"
        
class Card_Arythrea_Concentration(Actions):
    def __init__(self):
        super().__init__()
        self.name = "Concentration"
        
class Card_Arythrea_Improvisation(Actions):
    def __init__(self):
        super().__