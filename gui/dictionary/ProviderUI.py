from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from db.models.City import City
from db.models.Provider import Provider
from gui.custom_uix.AddRowButton import AddRowButton
from gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from gui.custom_uix.DeleteRowButton import DeleteRowButton
from gui.custom_uix.OpenScreenButton import OpenScreenButton
from gui.custom_uix.SelectableButton import SelectableButton
from gui.custom_uix.SelectableModalButton import SelectableModalButton
from gui.custom_uix.add_dictionary.AddProviderPopup import AddRowProviderPopup
from gui.custom_uix.modal.CItyModalPopup import CityModalPopup
from gui.dictionary.CityUI import CityUI


class ProviderUI:
    screen_name = 'provider_screen'
    parent_screen = 'dictionary_screen'
    model_class = Provider
    screen = Screen(name=screen_name)

    def __init__(self, screen_manager):
        self.sm = screen_manager
        self.update_screen()
        self.sm.add_widget(self.screen)

    def update_screen(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.main_layout())

    def main_layout(self):
        main_anchor = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.7, .9])
        main_anchor.add_widget(bl)

        # Вывод данных
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
        size:(root.width, root.height)
        size_hint_x: 1
        size_hint_y: None
        cols: 5
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='id', height=dp(30)))
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Город', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        providers = self.model_class.select()
        for provider in providers:
            data_layout.add_widget(Label(text=str(provider.id), height=dp(30)))
            data_layout.add_widget(SelectableButton(text=str(provider.name), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(provider.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(provider.city.name), height=dp(30),
                                                         modal_popup=CityModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=City,
                                                         id_value=str(provider.id),
                                                         field='city'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(provider.id), ui=self))
            data_layout.add_widget(Label(text='Товары поставщика', height=dp(30)))
        data_scroll.add_widget(data_layout)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowProviderPopup,
                                              popup_title='Добавление записи "Поставщик"'))
        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))
        city_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        city_layout.add_widget(OpenScreenButton(text='Города', screen_name=CityUI.screen_name, screen_manager=self.sm))

        bl.add_widget(back_layout)
        bl.add_widget(city_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
