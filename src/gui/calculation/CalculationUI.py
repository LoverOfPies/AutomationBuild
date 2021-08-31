from kivy.metrics import dp
from kivy.lang import Builder

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

from src.gui.BaseUIUtils import init_title_layout, init_back_button
from src.gui.modal.CityPicker import CityPicker


class CalculationUI:
    screen_name = 'calculation_screen'
    parent_screen = 'main_screen'
    table_name = 'Расчет'
    screen = Screen(name=screen_name)

    def __init__(self, screen_manager):
        self.sm = screen_manager
        self.name_input = TextInput(size_hint_x=2)
        self.city_picker = CityPicker(height=dp(30), text='Город')
        self.update_screen()
        self.sm.add_widget(self.screen)

    def update_screen(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.main_layout())

    def main_layout(self):
        main_anchor = AnchorLayout()
        box_layout = BoxLayout(orientation='vertical', size_hint=[.7, .9])
        main_anchor.add_widget(box_layout)

        data_layout = Builder.load_string('''GridLayout:
                size:(root.width, root.height)
                size_hint_x: 1
                size_hint_y: None
                cols: 2
                height: self.minimum_height
                row_default_height: 50
                row_force_default: True''')

        data_layout.add_widget(
            Label(text='Фио:', height=dp(30)))
        data_layout.add_widget(self.name_input)

        data_layout.add_widget(
            Label(text='Город:', height=dp(30)))
        data_layout.add_widget(self.city_picker)

        data_layout.add_widget(
            Label(text='Проект:', height=dp(30)))
        data_layout.add_widget(Button(text="Заглушка"))

        data_layout.add_widget(
            Label(text='База', height=dp(30)))
        data_layout.add_widget(CheckBox())

        title_layout = init_title_layout(self)
        back_layout = init_back_button(self)

        box_layout.add_widget(title_layout)
        box_layout.add_widget(back_layout)
        box_layout.add_widget(data_layout)

        return main_anchor
