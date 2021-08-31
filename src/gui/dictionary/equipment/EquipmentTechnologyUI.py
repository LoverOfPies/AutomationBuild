from operator import eq
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.Equipment import Equipment
from src.db.models.TechnologyEquipment import TechnologyEquipment

from src.gui.BaseUIUtils import init_control_buttons, init_title_layout, init_back_button
from src.gui.add_dictionary.equipment.AddEquipmentTechnologyPopup import AddEquipmentTechnologyPopup

class EquipmentTechnologyUI:
    screen_name = 'equipment_technology_screen'
    parent_screen = 'equipment_screen'
    table_name = 'Группы работ комплектации'
    model_class = TechnologyEquipment
    items_list = None
    screen = Screen(name=screen_name)
    add_popup = AddEquipmentTechnologyPopup

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
        cols: 2
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))

        querry = (
            Equipment.select(Equipment.name, fn.Count(TechnologyEquipment.id).alias('count'))
            .join()
            )
        self.items_list = querry

        for tech in self.items_list:
            print(tech)

        # Заголовок формы
        title_layout = init_title_layout(self)

        # Кнопки управления
        button_layout = init_control_buttons(self)

        # Кнопка назад
        back_layout = init_back_button(self)

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(button_layout)

        return main_anchor