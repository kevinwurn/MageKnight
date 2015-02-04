import cards

class Spell(cards.DeedCard):
    def __init__(self):
        super().__init__()
        
class Spells(object):
    spells_collection = None
    
    def __init__(self):
        self.spells_collection = []