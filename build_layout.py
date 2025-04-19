import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from number_guessing import GuessGame
from menu_screen import MainMenuScreen

#my app inhertis from kivy.app.App which is special class from kivy (base class for all kivy apps)
#Starting the app, Creating the window, Managing the app lifecycle (startup, close, etc.)
class GuessApp(App):
        #when the app starts, what shouldi  show on the screen
    def build(self): 
        Builder.load_file("menu.kv")   # Load the menu screen layout
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name = "menu"))
        sm.add_widget(GuessGame(name = "game"))
        sm.current = "menu"
        
        return sm # return the main class i have


    #restart button, if it has been click, this function clear the widget and reset the game.
    def restart_game(self):
        self.root.clear_widgets()
        # game_screen = self.root.get_screen("menu")
        self.root.add_widget(MainMenuScreen(name = "menu"))
        self.root.add_widget(GuessGame(name = "game"))
        self.root.current = "menu"
        
        

#only run this code if this file is being run directly -- not imported by another file
#It protects your app from running accidentally when you import it somewhere e
if __name__ == "__main__":
    GuessApp().run()