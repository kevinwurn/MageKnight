import cards

class Artifact(cards.DeedCard):
    def __init__(self):
        super().__init__()
        

class Artifacts(object):
    artifacts_collection = None
    
    def __init__(self):
        self.artifacts_collection = []