from re import I
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

from src.db.models.project.Project import Project

from src.gui.dictionary.project.ProjectEquipmentUI import ProjectEquipmentUI
from src.gui.dictionary.project.ProjectBaseVolumeUI import ProjectBaseVolumeUI
from src.gui.BaseUIUtils import init_control_buttons, init_title_layout, init_back_button
from src.gui.add_dictionary.AddRowSimplePopup import AddRowSimplePopup
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton


class ProjectUI:
    screen_name = 'project_screen'
    parent_screen = 'dictionary_screen'
    table_name = 'Проекты'
    model_class = Project
    items_list = None
    screen = Screen(name=screen_name)
    add_popup = AddRowSimplePopup

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
        data_layout.add_widget(Label(text='Комплектации', height=dp(30)))
        data_layout.add_widget(Label(text='Базовые объемы', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))

        self.items_list = self.model_class.select()
        for project in self.items_list:
            data_layout.add_widget(SelectableButton(height=dp(30),
                                                    text=str(project.name),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(project.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Комплектации',
                                                          screen_manager=self.sm,
                                                          filter_ui=ProjectEquipmentUI,
                                                          filter_name=str(project.name)
                                                          ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Базовые объемы',
                                                          screen_manager=self.sm,
                                                          filter_ui=ProjectBaseVolumeUI,
                                                          filter_name=str(project.name)
                                                          ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(project.id), ui=self))
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
