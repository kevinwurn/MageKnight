import cards

class Units(cards.NonDeedCard):
    def __init__(self):
        super().__init__()

class GreyUnit(Units):
    def __init__(self):
        super().__init__()
        
class GoldUnit(Units):
    def __init__(self):
        super().__init__() 


class GreyUnits(object):
    grey_units_collection = None
    
    def __init__(self):
        self.grey_units_collection = []

class GoldUnits(object):
    gold_units_collection = None
    
    def __init__(self):
        self.gold_units_collection = []