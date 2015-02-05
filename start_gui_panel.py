from pgu import gui
import player

class StartGUIPanel(object):
    _screen = None
    _app = None
    _table = None
    _select = None

    player = None

    def __init__(self, game_screen):
        self._screen = game_screen
        
        self._app = gui.Desktop()
        self._app.connect(gui.QUIT, self._app.quit, None)
        
        self._table = gui.Table()
        self._table.tr()
        self._table.td(gui.Label("Select Player"))
        self._select = gui.Select()
        self._select.add("Arythrea", player.ARYTHREA)
        self._table.tr()
        self._table.td(self._select)
        self._table.tr()
        button = gui.Button("Start Solo Game")
        self._table.td(button)
        button.connect(gui.CLICK, self._commit_values)
    
    def _commit_values(self):
        if self._select.value:
            self.player = self._select.value
            self._app.quit()
    
    def launch(self):
        self._app.run(self._table, self._screen)