import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home_screen'
        self.add_widget(HomeLayout())


class GameScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'game_screen'


class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen())
        self.add_widget(GameScreen())


class Title(Label):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Python Coding Game Lesson'
        self.font_size = 50


class BeginButton(Button):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Begin'

    def on_release(self):
        sm.current = 'game_screen'


class HelpButton(Button):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Help'


class ExitButton(Button):

    def __init__(self, **kwargs):
        super().__init(**kwargs)
        self.text = 'Exit'

class HomeLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 8
        self.add_widget(Title())
        self.add_widget(SubHome())


class SubHome(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 50
        self.padding = 30
        self.size_hint_y = None
        self.height = 100
        self.size_hint = 1, .2
        self.add_widget(BeginButton())
        self.add_widget(HelpButton())

sm = ScreenManagement()

class GameApp(App):
    title = 'Python Coding Game Lesson'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        return sm 


if __name__ == '__main__':
    GameApp().run()
