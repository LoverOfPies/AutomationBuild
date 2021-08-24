from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.material.Material import Material
from src.db.models.base.Unit import Unit
from src.gui.BaseUIUtils import init_control_buttons, init_title_layout, init_back_button
from src.gui.add_dictionary.material.AddRowMaterialPopup import AddRowMaterialPopup
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.dictionary.material.MaterialCategoryUI import MaterialCategoryUI
from src.gui.dictionary.material.MaterialGroupUI import MaterialGroupUI
from src.gui.dictionary.material.MaterialPropertyUI import MaterialPropertyUI
from src.gui.dictionary.material.MaterialSubgroupUI import MaterialSubgroupUI
from src.gui.modal.ModalPopup import ModalPopup

from src.gui.modal.ChainedFilterPopup import ChainedFilterPopup
from src.db.models.material.MaterialCategory import MaterialCategory
from src.db.models.material.MaterialGroup import MaterialGroup
from src.db.models.material.MaterialSubgroup import MaterialSubgroup


class MaterialUI:
    screen_name = 'material_screen'
    parent_screen = 'dictionary_screen'
    table_name = 'Материалы'
    model_class = Material
    screen = Screen(name=screen_name)
    add_popup = AddRowMaterialPopup

    items_list = None
    filter_flag = False
    material_category = 'Не выбранно'
    material_group = 'Не выбранно'
    subgroup = 'Не выбранно'
    selection_chain = {
        'material_category': {'id': None, 'selection': None, 'last_choice': None, 'model': MaterialCategory, 'enabled': True},
        'material_group': {'id': None, 'selection': None, 'last_choice': None, 'model': MaterialGroup, 'enabled': False},
        'subgroup': {'id': None, 'selection': None, 'last_choice': None, 'model': MaterialSubgroup, 'enabled': False}
    }
    last_selection = 'subgroup'

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

        if not self.filter_flag:
            self.items_list = self.model_class.select()

        for material in self.items_list:
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
                                                         text=str(
                                                             material.unit.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Unit,
                                                         id_value=str(
                                                             material.id),
                                                         field='unit', modal_title='Единицы измерения'
                                                         ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Свойства',
                                                          screen_manager=self.sm,
                                                          filter_ui=MaterialPropertyUI,
                                                          filter_name=str(
                                                              material.name)
                                                          ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(material.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = init_title_layout(self)

        # Кнопки управления
        button_layout = init_control_buttons(self)

        # Кнопка назад
        back_layout = init_back_button(self)

        # Категории
        category_layout = BoxLayout(orientation='horizontal', size_hint=[
                                    1, .2], padding=[0, 5])
        category_layout.add_widget(OpenScreenButton(text='Категории',
                                                    screen_name=MaterialCategoryUI.screen_name,
                                                    screen_manager=self.sm))
        category_layout.add_widget(Label(text='Категория: '))
        # Фильтр категории
        category_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                      text=self.material_category,
                                                      dict_class=MaterialGroup,
                                                      owner_class=MaterialCategory,
                                                      field='material_category',
                                                      modal_title='Фильр категории',
                                                      ui=self,
                                                      ))

        # Группа
        group_layout = BoxLayout(orientation='horizontal', size_hint=[
                                 1, .2], padding=[0, 5])
        group_layout.add_widget(OpenScreenButton(text='Группа',
                                                 screen_name=MaterialGroupUI.screen_name,
                                                 screen_manager=self.sm))
        group_layout.add_widget(Label(text='Группа: '))
        # Фильтр группы
        group_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                   text=self.material_group,
                                                   dict_class=MaterialSubgroup,
                                                   owner_class=MaterialGroup,
                                                   field='material_group',
                                                   modal_title='Фильр группы',
                                                   ui=self,
                                                   ))

        # Подгруппа
        subgroup_layout = BoxLayout(orientation='horizontal', size_hint=[
                                    1, .2], padding=[0, 5])
        subgroup_layout.add_widget(OpenScreenButton(text='Подгруппа',
                                                    screen_name=MaterialSubgroupUI.screen_name,
                                                    screen_manager=self.sm))
        subgroup_layout.add_widget(Label(text='Подгруппа: '))
        # Фильтр подгруппы
        subgroup_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                      text=self.subgroup,
                                                      dict_class=self.model_class,
                                                      owner_class=MaterialSubgroup,
                                                      field='subgroup',
                                                      modal_title='Фильр группы',
                                                      ui=self,
                                                      ))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(category_layout)
        bl.add_widget(group_layout)
        bl.add_widget(subgroup_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
