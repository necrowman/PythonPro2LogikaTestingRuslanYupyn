from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.splitter import Splitter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    def __init__(self, name, screen_manager):
        super().__init__(name=name)
        self.sm = screen_manager
        vbox = BoxLayout(orientation = "vertical", padding = 24, spacing = 16)

        spliter = Splitter(size_hint=(1, 0.3))
        vbox.add_widget(spliter)

        title_lbl = Label(text = '''Це тестова програма для перевірки викладачів школи Logika
                          Виконав викладач Руслан Юпин
                          Сподіваюся ця апка зарахується ))''', size_hint = (1, 0.2))
        vbox.add_widget(title_lbl)

        hbox1 = BoxLayout(spacing = 16, size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5})
        next_button1 = Button(text="Перейти на наступний екран праворуч")
        next_button2 = Button(text="Перейти на наступний екран ліворуч")
        hbox1.add_widget(next_button1)
        hbox1.add_widget(next_button2)
        
        spliter2 = Splitter()
        vbox.add_widget(spliter2)

        vbox.add_widget(hbox1)

        hbox2 = BoxLayout(spacing = 16, size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5})
        next_button3 = Button(text="Показати наступний екран знизу")
        next_button4 = Button(text="Показати наступний екран зверху")
        hbox2.add_widget(next_button3)
        hbox2.add_widget(next_button4)

        vbox.add_widget(hbox2)

        self.add_widget(vbox)

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = "menu", screen_manager = sm))
        return sm

app = TestApp()
app.run()