from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.material.Material import Material
from src.db.models.work.Work import Work
from src.db.models.work.WorkMaterial import WorkMaterial
from src.gui.add_dictionary.AddRowWorkMaterialPopup import AddRowWorkMaterialPopup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class WorkMaterialUI:
    screen_name = 'workmaterial_screen'
    parent_screen = 'dictionary_screen'
    model_class = WorkMaterial
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
        cols: 4
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='Количество материала', height=dp(30)))
        data_layout.add_widget(Label(text='Базовая единица', height=dp(30)))
        data_layout.add_widget(Label(text='Технология', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        workmaterials = self.model_class.select()
        for workmaterial in workmaterials:
            data_layout.add_widget(SelectableButton(text=str(workmaterial.amount), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(workmaterial.id),
                                                    field='amount', is_double=False
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(workmaterial.material.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Material,
                                                         id_value=str(workmaterial.id),
                                                         field='material', modal_title='Материалы'
                                                         ))
            data_layout.add_widget(SelectableModalButton(text=str(workmaterial.work.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Work,
                                                         id_value=str(workmaterial.id),
                                                         field='work', modal_title='Работы'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(workmaterial.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowWorkMaterialPopup,
                                              popup_title='Добавление записи "Материал для работы"'))

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
