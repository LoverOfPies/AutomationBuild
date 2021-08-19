from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.material.MaterialGroup import MaterialGroup
from src.db.models.material.MaterialSubgroup import MaterialSubgroup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.add_dictionary.material.AddRowMaterialSubgroupPopup import AddRowMaterialSubgroupPopup
from src.gui.modal.ModalPopup import ModalPopup


class MaterialSubgroupUI:
    screen_name = 'subgroup_screen'
    parent_screen = 'material_screen'
    model_class = MaterialSubgroup
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
        cols: 3
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Группа', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        subgroups = self.model_class.select()
        for subgroup in subgroups:
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(subgroup.name),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(subgroup.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableModalButton(height=dp(30),
                                                         text=str(subgroup.material_group.name),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=MaterialGroup,
                                                         id_value=str(subgroup.id),
                                                         field='material_group', modal_title='Группы'
                                                         ))
            data_layout.add_widget(DeleteRowButton(height=dp(30),
                                                   text='Удалить',
                                                   id_value=str(subgroup.id),
                                                   ui=self
                                                   ))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        title_label = Label(text='Подгруппы материалов', font_size='20sp')
        title_layout.add_widget(title_label)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить',
                                              ui=self,
                                              popup=AddRowMaterialSubgroupPopup,
                                              popup_title='Добавление записи "Подгруппа материалов"'))

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
