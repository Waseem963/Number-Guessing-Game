
from kivy.uix.screenmanager import ScreenManager, Screen
from number_guessing import GuessGame


class MainMenuScreen(Screen): 
   
     
   def level_easy(self):
        game_screen = self.manager.get_screen("game")  # get the actual screen shown
        game_screen.level = "easy"                     # set its level
        game_screen.setup_game()                       # tell it to prepare the random number
        self.manager.current = "game"
                                                         # now switch to game screen
   def level_medium(self):
        game_screen = self.manager.get_screen("game")  # get the actual screen shown
        game_screen.level = "medium"                     # set its level
        game_screen.setup_game()                       # tell it to prepare the random number
        self.manager.current = "game"
                        # now switch to game screen
   def level_hard(self):
        game_screen = self.manager.get_screen("game")  # get the actual screen shown
        game_screen.level = "hard"                     # set its level
        game_screen.setup_game()                       # tell it to prepare the random number
        self.manager.current = "game"                  # now switch to game screen



    