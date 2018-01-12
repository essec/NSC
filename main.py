from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = 'main_screen'

class PlayScreen(Screen):
    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)
        self.name = 'play_screen'

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super(HelpScreen, self).__init__(**kwargs)
        self.name = 'help_screen'

class RunButton(Button):
    def __init__(self, **kwargs):
        super(RunButton, self).__init__(**kwargs)

class HintButton(Button):
    def __init__(self, **kwargs):
        super(HintButton, self).__init__(**kwargs)



class BlockButton(Button):
    def __init__(self, **kwargs):
        super(BlockButton, self).__init__(**kwargs)

class ImportButton(Button):
    def __init__(self, **kwargs):
        super(ImportButton, self).__init__(**kwargs)


class ScreenManagement(ScreenManager):
    pass

class GameWidget(Widget):
    pass

class GameApp(App):
    title = 'Python Game'
    def build(self):
        return

if __name__ == '__main__':
    GameApp().run()
