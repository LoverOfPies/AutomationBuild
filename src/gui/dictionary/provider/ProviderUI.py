from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.provider.City import City
from src.db.models.provider.Provider import Provider
from src.gui.BaseUIUtils import init_title_layout, init_control_buttons, init_back_button
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.add_dictionary.provider.AddProviderPopup import AddRowProviderPopup
from src.gui.dictionary.provider.CityUI import CityUI
from src.gui.dictionary.provider.ProductUI import ProductUI
from src.gui.modal.ModalPopup import ModalPopup
from src.gui.modal.FilterPopup import FilterPopup


class ProviderUI:
    screen_name = 'provider_screen'
    parent_screen = 'dictionary_screen'
    table_name = 'Поставщики'
    model_class = Provider
    screen = Screen(name=screen_name)
    add_popup = AddRowProviderPopup
    providers = None
    filter_flag = False
    filter_btn_text = 'Не выбранно'

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
        data_layout = Builder.load_string(
            '''GridLayout:
            size:(root.width, root.height)
            size_hint_x: 1
            size_hint_y: None
            cols: 4
            height: self.minimum_height
            row_default_height: 50
            row_force_default: True'''
        )
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Город', height=dp(30)))
        data_layout.add_widget(Label(text='Товары поставщика', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))

        if not self.filter_flag:
            self.providers = self.model_class.select()

        for provider in self.providers:
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(provider.name),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(provider.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableModalButton(height=dp(30),
                                                         text=str(
                                                             provider.city.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=City,
                                                         id_value=str(
                                                             provider.id),
                                                         field='city', modal_title='Города'
                                                         ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Товары ' + provider.name,
                                                          screen_manager=self.sm,
                                                          filter_ui=ProductUI,
                                                          filter_name=str(
                                                              provider.name)
                                                          ))
            data_layout.add_widget(DeleteRowButton(height=dp(30),
                                                   text='Удалить',
                                                   id_value=str(provider.id),
                                                   ui=self
                                                   ))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = init_title_layout(self)

        # Кнопки управления
        button_layout = init_control_buttons(self)

        # Кнопка назад
        back_layout = init_back_button(self)

        # Справочник городов
        city_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        city_layout.add_widget(OpenScreenButton(
            text='Города', screen_name=CityUI.screen_name, screen_manager=self.sm))
        city_layout.add_widget(Label(text='Город: '))

        # Фильтр города
        city_layout.add_widget(FilterPopup(height=dp(30),
                                           text=self.filter_btn_text,
                                           dict_class=self.model_class,
                                           owner_class=City,
                                           modal_title='Фильр города',
                                           ui=self,
                                           ))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(city_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
