from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.City import City
from src.db.models.Provider import Provider
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.FilterDropDown import FilterDropDown
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.add_dictionary.AddProviderPopup import AddRowProviderPopup
from src.gui.dictionary.CityUI import CityUI
from src.gui.dictionary.ProductUI import ProductUI
from src.gui.modal.ModalPopup import ModalPopup


class ProviderUI:
    screen_name = 'provider_screen'
    parent_screen = 'dictionary_screen'
    model_class = Provider
    screen = Screen(name=screen_name)
    citydrop_button = Button(text='Все')

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
        cols: 4
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Город', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        # city = City.select().where(City.name == 'Рыбинск')
        # providers = self.model_class.select().where(Provider.city == city)
        providers = self.model_class.select()
        for provider in providers:
            data_layout.add_widget(SelectableButton(text=str(provider.name), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(provider.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(provider.city.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=City,
                                                         id_value=str(provider.id),
                                                         field='city', modal_title='Города'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(provider.id), ui=self))
            data_layout.add_widget(OpenFilterScreenButton(text='Товары', screen_name=ProductUI.screen_name,
                                                    screen_manager=self.sm, height=dp(30), filter_name=str(provider.name)))
        data_scroll.add_widget(data_layout)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowProviderPopup,
                                              popup_title='Добавление записи "Поставщик"'))

        # Кнопка "Назад"
        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        # Фильтр с выпадающим списком
        # dropdown = FilterDropDown(dict_class=City, main_button=self.citydrop_button)
        # self.citydrop_button.bind(on_release=dropdown.open)
        # dropdown_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        # dropdown_layout.add_widget(Label(text='Город: '))
        # dropdown_layout.add_widget(self.citydrop_button)

        # Справочник городов
        city_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        city_layout.add_widget(OpenScreenButton(text='Города', screen_name=CityUI.screen_name, screen_manager=self.sm))

        bl.add_widget(back_layout)
        # bl.add_widget(dropdown_layout)
        bl.add_widget(city_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor