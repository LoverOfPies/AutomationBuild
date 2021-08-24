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
from src.gui.BaseUIUtils import init_title_layout, init_control_buttons, init_back_button
from src.gui.add_dictionary.work.AddRowWorkMaterialPopup import AddRowWorkMaterialPopup
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class WorkMaterialUI:
    screen_name = 'work_material_screen'
    parent_screen = 'work_screen'
    table_name = 'Материалы для работ'
    model_class = WorkMaterial
    screen = Screen(name=screen_name)
    add_popup = AddRowWorkMaterialPopup
    filter_name = ''

    def __init__(self, screen_manager, filter_name):
        self.sm = screen_manager
        self.filter_name = filter_name
        self.update_screen()
        if screen_manager.has_screen(self.screen_name):
            screen_manager.remove_widget(screen_manager.get_screen(self.screen_name))
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
        data_layout.add_widget(Label(text='Количество материала', height=dp(30)))
        data_layout.add_widget(Label(text='Материалы', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        work = Work.select().where(Work.name == self.filter_name)
        work_materials = self.model_class.select().where(self.model_class.work == work)
        for work_material in work_materials:
            data_layout.add_widget(SelectableButton(text=str(work_material.amount), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить количество",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(work_material.id),
                                                    field='amount', is_double=False
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(work_material.material.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Material,
                                                         id_value=str(work_material.id),
                                                         field='material', modal_title='Материалы'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(work_material.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = init_title_layout(self)

        # Кнопки управления
        button_layout = init_control_buttons(self)

        # Кнопка назад
        back_layout = init_back_button(self)

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
