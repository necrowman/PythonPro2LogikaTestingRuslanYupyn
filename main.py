from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    def __init__(self, name, screen_manager):
        super().__init__(name=name)
        self.sm = screen_manager
        vbox = BoxLayout(orientation = "vertical", padding = 24, spacing = 16)
        title_lbl = Label(text = '''Це тестова програма для перевірки викладачів школи Logika
                          Виконав викладач Руслан Юпин
                          Сподіваюся ця апка зарахується ))''')


class TestApp(App):
    pass

app = TestApp()
app.run()