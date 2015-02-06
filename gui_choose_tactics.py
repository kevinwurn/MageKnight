from pgu import gui
import tactics
import game

TACTIC_CARD_WIDTH = 100
TACTIC_CARD_HEIGHT = 150

class GUIChooseTactics(object):
    _screen = None
    _engine = None
    _app = None
    _table = None
    _radio = None
    _images = None

    tactic = None

    def __init__(self, game_screen, game_engine):
        self._screen = game_screen
        self._engine = game_engine
        self._images = []
        
        self._app = gui.Desktop()
        self._app.connect(gui.QUIT, self._app.quit, None)
        
        self._table = gui.Table()
        #first row
        self._table.tr()
        if self._engine.time_of_day == game.TIME_DAY:
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_1_early_bird.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_2_rethink.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_3_mana_steal.png"))
        elif self._engine.time_of_day == game.TIME_NIGHT:
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_1_from_the_dusk.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_2_long_night.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_3_mana_search.png"))
        for img in self._images:
            self._table.td(img)
        #second row 
        self._table.tr()
        self._radio = gui.Group()
        self._table.td(gui.Radio(self._radio,value=1))
        self._table.td(gui.Radio(self._radio,value=2))
        self._table.td(gui.Radio(self._radio,value=3))
        #third row      
        self._table.tr()
        if self._engine.time_of_day == game.TIME_DAY:
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_4_planning.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_5_great_start.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_day_6_the_right_moment.png"))
        elif self._engine.time_of_day == game.TIME_NIGHT:
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_4_midnight_meditation.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_5_preparation.png"))
            self._images.append(gui.Image("assets/images/cards/tactics/gui_tactics_night_6_sparing_power.png"))
        for i in range(3, 6):
            self._table.td(self._images[i])
        #fourth row
        self._table.tr()       
        self._table.td(gui.Radio(self._radio,value=4))
        self._table.td(gui.Radio(self._radio,value=5))
        self._table.td(gui.Radio(self._radio,value=6))
        #fifth row
        self._table.tr()
        button = gui.Button("Select Tactics")
        self._table.td(button, colspan=3)
        button.connect(gui.CLICK, self._commit_values)
    
    def _commit_values(self):
        if self._radio.value:
            if self._engine.time_of_day == game.TIME_DAY:
                if self._radio.value == 1:
                    self.tactic = tactics.Tactics_Day_1_Early_Bird(self._engine)
                elif self._radio.value == 2:
                    self.tactic = tactics.Tactics_Day_2_Rethink(self._engine)
                elif self._radio.value == 3:
                    self.tactic = tactics.Tactics_Day_3_Mana_Steal(self._engine) 
                elif self._radio.value == 4:
                    self.tactic = tactics.Tactics_Day_4_Planning(self._engine)
                elif self._radio.value == 5:
                    self.tactic = tactics.Tactics_Day_5_Great_Start(self._engine) 
                elif self._radio.value == 6:
                    self.tactic = tactics.Tactics_Day_6_The_Right_Moment(self._engine)
                else:
                    return  
            elif self._engine.time_of_day == game.TIME_NIGHT: 
                if self._radio.value == 1:
                    self.tactic = tactics.Tactics_Night_1_From_The_Dusk(self._engine)
                elif self._radio.value == 2:
                    self.tactic = tactics.Tactics_Night_2_Long_Night(self._engine)
                elif self._radio.value == 3:
                    self.tactic = tactics.Tactics_Night_3_Mana_Search(self._engine)  
                elif self._radio.value == 4:
                    self.tactic = tactics.Tactics_Night_4_Midnight_Meditation(self._engine) 
                elif self._radio.value == 5:
                    self.tactic = tactics.Tactics_Night_5_Preparation(self._engine)
                elif self._radio.value == 6:
                    self.tactic = tactics.Tactics_Night_6_Sparing_Power(self._engine)
                else:
                    return
            else:
                return
            self._app.quit() 
    
    def launch(self):
        self._app.run(self._table, self._screen)