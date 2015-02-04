import cards

class AdvancedAction(cards.DeedCard):
    def __init__(self):
        super().__init__()
        
class AdvancedActions(object):
    advanced_actions_collection = None
    
    def __init__(self):
        self.advanced_actions_collection = []