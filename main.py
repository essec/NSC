from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.popup import Popup

Window.fullscreen = True

class MainScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class GameApp(App):
    title = 'Python Game'
    def build(self):
        return

if __name__ == '__main__':
    GameApp().run()
