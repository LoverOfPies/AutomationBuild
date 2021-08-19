from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.material.Material import Material
from src.db.models.provider.Product import Product
from src.db.models.provider.Provider import Provider
from src.gui.add_dictionary.provider.AddRowProductPopup import AddRowProductPopup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class ProductUI:
    screen_name = 'product_screen'
    parent_screen = 'provider_screen'
    model_class = Product
    screen = Screen(name=screen_name)
    filter_name = ''

    def __init__(self, screen_manager, filter_name):
        self.sm = screen_manager
        self.filter_name = filter_name
        self.update_screen()
        if screen_manager.has_screen('product_screen'):
            screen_manager.remove_widget(screen_manager.get_screen('product_screen'))
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
        data_layout.add_widget(Label(text='Цена', height=dp(30)))
        data_layout.add_widget(Label(text='Материала за 1 шт', height=dp(30)))
        data_layout.add_widget(Label(text='Поставщик', height=dp(30)))
        data_layout.add_widget(Label(text='Материал', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        provider = Provider.select().where(Provider.name == self.filter_name)
        products = Product.select().where(Product.provider == provider)
        for product in products:
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(product.price),
                                                    popup_title="Изменить цену",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(product.id),
                                                    field='price', is_double=False
                                                    ))
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(product.amount_for_one),
                                                    popup_title="Изменить количество за 1 шт",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(product.id),
                                                    field='amount_for_one', is_double=False
                                                    ))
            data_layout.add_widget(SelectableModalButton(height=dp(30),
                                                         text=str(product.provider.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Provider,
                                                         id_value=str(product.id),
                                                         field='provider', modal_title='Поставщики'
                                                         ))
            data_layout.add_widget(SelectableModalButton(height=dp(30),
                                                         text=str(product.material.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Material,
                                                         id_value=str(product.id),
                                                         field='material', modal_title='Материалы'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(product.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        title_label = Label(text='Товары ' + self.filter_name, font_size='20sp')
        title_layout.add_widget(title_label)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowProductPopup,
                                              popup_title='Добавление записи "Товар"'))

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
