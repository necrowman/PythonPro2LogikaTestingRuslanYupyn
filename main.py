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
        vbox = BoxLayout(orientation="vertical", padding=24, spacing=16)

        spliter = Splitter(size_hint=(1, 0.3))
        vbox.add_widget(spliter)

        title_lbl = Label(text='''Це тестова програма для перевірки викладачів школи Logika
                          Виконав викладач Руслан Юпин
                          Сподіваюся ця апка зарахується ))''', size_hint=(1, 0.2))
        vbox.add_widget(title_lbl)

        hbox1 = BoxLayout(spacing=16, size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5})
        next_button1 = Button(text="Перейти на наступний екран праворуч")
        next_button1.bind(on_press=self.go_right)
        next_button2 = Button(text="Перейти на наступний екран ліворуч")
        next_button2.bind(on_press=self.go_left)
        hbox1.add_widget(next_button1)
        hbox1.add_widget(next_button2)

        spliter2 = Splitter()
        vbox.add_widget(spliter2)

        vbox.add_widget(hbox1)

        hbox2 = BoxLayout(spacing=16, size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5})
        next_button3 = Button(text="Показати наступний екран знизу")
        next_button3.bind(on_press=self.go_up)
        next_button4 = Button(text="Показати наступний екран зверху")
        next_button4.bind(on_press=self.go_down)
        hbox2.add_widget(next_button3)
        hbox2.add_widget(next_button4)

        vbox.add_widget(hbox2)

        self.add_widget(vbox)

    def go_left(self, instance):
        self.sm.transition.direction = "left"
        self.sm.current = "left_screen"

    def go_right(self, instance):
        self.sm.transition.direction = "right"
        self.sm.current = "right_screen"

    def go_up(self, instance):
        self.sm.transition.direction = "up"
        self.sm.current = "up_screen"

    def go_down(self, instance):
        self.sm.transition.direction = "down"
        self.sm.current = "down_screen"

class NextScreen(Screen):
    def __init__(self, name, back_direction, screen_manager):
        super().__init__(name=name)
        self.back_direction = back_direction
        self.sm = screen_manager

        vbox = BoxLayout(orientation="vertical", padding=24, spacing=16)

        spliter = Splitter(size_hint=(1, 0.4))
        vbox.add_widget(spliter)

        title_lbl = Label(text=f"Це кастомізований екран зі своєю зворотньою транзицією (переходом): \n{name}", size_hint=(1, 0.2))
        vbox.add_widget(title_lbl)

        spliter2 = Splitter()
        vbox.add_widget(spliter2)

        back_btn = Button(text="Повернутися назад", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        back_btn.bind(on_press=self.go_back)

        vbox.add_widget(back_btn)

        self.add_widget(vbox)

    def go_back(self, instance):
        self.sm.transition.direction = self.back_direction
        self.sm.current = "menu"

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu", screen_manager=sm))
        sm.add_widget(NextScreen(name="left_screen", back_direction="right", screen_manager=sm))
        sm.add_widget(NextScreen(name="right_screen", back_direction="left", screen_manager=sm))
        sm.add_widget(NextScreen(name="up_screen", back_direction="down", screen_manager=sm))
        sm.add_widget(NextScreen(name="down_screen", back_direction="up", screen_manager=sm))
        return sm

app = TestApp()
app.run()