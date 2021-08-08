from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.Material import Material
from src.db.models.Subgroup import Subgroup
from src.db.models.Unit import Unit
from src.gui.add_dictionary.AddRowMaterialPopup import AddRowMaterialPopup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.dictionary.material.CategoryUI import CategoryUI
from src.gui.dictionary.material.GroupUI import GroupUI
from src.gui.dictionary.material.PropMaterialUI import PropMaterialUI
from src.gui.dictionary.material.SubgroupUI import SubgroupUI
from src.gui.dictionary.provider.ProductUI import ProductUI
from src.gui.modal.ModalPopup import ModalPopup


class MaterialUI:
    screen_name = 'material_screen'
    parent_screen = 'dictionary_screen'
    model_class = Material
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
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Артикул', height=dp(30)))
        data_layout.add_widget(Label(text='Единицы измерения', height=dp(30)))
        data_layout.add_widget(Label(text='Свойства материала', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        materials = self.model_class.select()
        for material in materials:
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(material.name),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(material.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(material.articul),
                                                    popup_title="Изменить артикул",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(material.id),
                                                    field='articul'
                                                    ))
            data_layout.add_widget(SelectableModalButton(height=dp(30),
                                                         text=str(material.unit.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Unit,
                                                         id_value=str(material.id),
                                                         field='unit', modal_title='Единицы измерения'
                                                         ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Свойства',
                                                          screen_manager=self.sm,
                                                          filter_ui=PropMaterialUI,
                                                          filter_name=str(material.name)
                                                          ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(material.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        title_label = Label(text='Материалы', font_size='20sp')
        title_layout.add_widget(title_label)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить',
                                              ui=self,
                                              popup=AddRowMaterialPopup,
                                              popup_title='Добавление записи "Материал"'))
        button_layout.add_widget(Button(text='Импорт данных'))

        # Кнопка "Назад"
        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        # Категории
        category_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        category_layout.add_widget(OpenScreenButton(text='Категории',
                                                    screen_name=CategoryUI.screen_name,
                                                    screen_manager=self.sm))
        category_layout.add_widget(Label(text='Категория: '))
        category_layout.add_widget(Button(text='Заглушка'))

        # Группа
        group_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        group_layout.add_widget(OpenScreenButton(text='Группа',
                                                 screen_name=GroupUI.screen_name,
                                                 screen_manager=self.sm))
        group_layout.add_widget(Label(text='Группа: '))
        group_layout.add_widget(Button(text='Заглушка'))

        # Подгруппа
        subgroup_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        subgroup_layout.add_widget(OpenScreenButton(text='Подгруппа',
                                                    screen_name=SubgroupUI.screen_name,
                                                    screen_manager=self.sm))
        subgroup_layout.add_widget(Label(text='Подгруппа: '))
        subgroup_layout.add_widget(Button(text='Заглушка'))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(category_layout)
        bl.add_widget(group_layout)
        bl.add_widget(subgroup_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
