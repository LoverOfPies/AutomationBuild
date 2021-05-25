from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from gui.custom_uix.AddRowPopup import AddRowPopup
from gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from gui.custom_uix.DeleteButton import DeleteButton
from gui.custom_uix.OpenScreenButton import OpenScreenButton
from gui.custom_uix.SelectableButton import SelectableButton
from db.models.City import City


def add_city(instance):
    popup = AddRowPopup(title='Добавление записи "Город"', dict_class=City)
    popup.open()


class CityUI:
    screen_name = 'city_screen'
    parent_screen = 'dictionary_screen'
    dict_class = City

    def __init__(self, screen_manager):
        self.sm = screen_manager

    def city_screen(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.7, .9])
        al.add_widget(bl)

        # Фильтр
        search_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 15])
        search_layout.add_widget(Label(text='Фильтр'))
        id_input = TextInput(hint_text='id', multiline=False)
        name_input = TextInput(hint_text='Наименование', multiline=False)
        search_button = Button(text='Поиск')
        search_layout.add_widget(id_input)
        search_layout.add_widget(name_input)
        search_layout.add_widget(search_button)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        button_layout.add_widget(Button(text='Добавить', on_press=add_city))

        # Вывод данных
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
        size:(root.width, root.height)
        size_hint_x: 1
        size_hint_y: None
        cols: 3
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='id', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(Label(text='Наименование', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(Label(text='', size_hint_y=None, height=dp(30)))
        cities = self.dict_class.select()
        for city in cities:
            data_layout.add_widget(Label(text=str(city.id), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectableButton(text=str(city.name), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=City,
                                                    id_value=str(city.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(DeleteButton(text='Удалить', height=dp(30),
                                                model_class=City, id_value=str(city.id), ui=self))
        data_scroll.add_widget(data_layout)

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screenname=self.parent_screen, screenmanager=self.sm))

        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(search_layout)
        bl.add_widget(button_layout)

        screen = Screen(name=self.screen_name)
        screen.add_widget(al)
        self.sm.add_widget(screen)
