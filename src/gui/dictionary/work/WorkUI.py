from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.work.Work import Work
from src.gui.add_dictionary.work.AddRowWorkPopup import AddRowWorkPopup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenFilterScreenButton import OpenFilterScreenButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.dictionary.work.WorkGroupUI import WorkGroupUI
from src.gui.dictionary.work.WorkMaterialUI import WorkMaterialUI
from src.gui.dictionary.work.WorkStageUI import WorkStageUI
from src.gui.dictionary.work.WorkTechnologyUI import WorkTechnologyUI
from src.gui.modal.ModalPopup import ModalPopup

from src.gui.modal.ChainedFilterPopup import ChainedFilterPopup
from src.db.models.work.WorkStage import WorkStage
from src.db.models.work.WorkTechnology import WorkTechnology
from src.db.models.work.WorkGroup import WorkGroup


class WorkUI:
    screen_name = 'work_screen'
    parent_screen = 'dictionary_screen'
    model_class = Work
    screen = Screen(name=screen_name)

    items_list = None
    filter_flag = False
    work_stage = 'Не выбранно'
    work_technology = 'Не выбранно'
    group_work = 'Не выбранно'
    selection_chain = {
        'work_stage': {'id': None, 'selection': None, 'last_choice': None, 'model': WorkStage, 'enabled': True},
        'work_technology': {'id': None, 'selection': None, 'last_choice': None, 'model': WorkTechnology, 'enabled': False},
        'group_work': {'id': None, 'selection': None, 'last_choice': None, 'model': WorkGroup, 'enabled': False},
    }
    last_selection = 'group_work'

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
        data_layout.add_widget(Label(text='Коэффицент', height=dp(30)))
        data_layout.add_widget(Label(text='Тариф клиента', height=dp(30)))
        data_layout.add_widget(Label(text='Тариф себестоимости', height=dp(30)))
        data_layout.add_widget(Label(text='Базовая единица', height=dp(30)))
        data_layout.add_widget(Label(text='Группа', height=dp(30)))
        data_layout.add_widget(Label(text='Материалы для работы', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))

        if not self.filter_flag:
            self.items_list = self.model_class.select()

        for work in self.items_list:
            data_layout.add_widget(SelectableButton(text=str(work.name), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(work.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableButton(text=str(work.work_coefficient), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить коэффицент",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(work.id),
                                                    field='work_coefficient', is_double=False
                                                    ))
            data_layout.add_widget(SelectableButton(text=str(work.client_price), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить тариф клиента",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(work.id),
                                                    field='client_price', is_double=False
                                                    ))
            data_layout.add_widget(SelectableButton(text=str(work.work_price), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить тариф себестоимости",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(work.id),
                                                    field='work_price', is_double=False
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(work.base_unit.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=BaseUnit,
                                                         id_value=str(work.id),
                                                         field='base_unit', modal_title='Базовые единицы'
                                                         ))
            data_layout.add_widget(SelectableModalButton(text=str(work.group_work.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=BaseUnit,
                                                         id_value=str(work.id),
                                                         field='group_work', modal_title='Группы работ'
                                                         ))
            data_layout.add_widget(OpenFilterScreenButton(height=dp(30),
                                                          text='Материалы для работы',
                                                          screen_manager=self.sm,
                                                          filter_ui=WorkMaterialUI,
                                                          filter_name=str(work.name)
                                                          ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(work.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Заголовок формы
        title_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
        title_label = Label(text='Работы', font_size='20sp')
        title_layout.add_widget(title_label)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить',
                                              ui=self,
                                              popup=AddRowWorkPopup,
                                              popup_title='Добавление записи "Работа"'))
        button_layout.add_widget(Button(text='Импорт данных'))

        # Кнопка "Назад"
        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        # Стадии работ
        work_stage_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        work_stage_layout.add_widget(OpenScreenButton(text='Стадия',
                                                      screen_name=WorkStageUI.screen_name,
                                                      screen_manager=self.sm))
        work_stage_layout.add_widget(Label(text='Стадия: '))
        # Фильтр стадий
        work_stage_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                      text=self.work_stage,
                                                      dict_class=WorkTechnology,
                                                      owner_class=WorkStage,
                                                      field='work_stage',
                                                      modal_title='Фильр стадий',
                                                      ui=self,
                                                      ))

        # Технологии работ
        work_technology_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        work_technology_layout.add_widget(OpenScreenButton(text='Технология',
                                                           screen_name=WorkTechnologyUI.screen_name,
                                                           screen_manager=self.sm))
        work_technology_layout.add_widget(Label(text='Технология: '))
        # Фильтр технологий
        work_technology_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                      text=self.work_technology,
                                                      dict_class=WorkGroup,
                                                      owner_class=WorkTechnology,
                                                      field='work_technology',
                                                      modal_title='Фильр технологий',
                                                      ui=self,
                                                      ))

        # Группы работ
        work_group_layout = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=[0, 5])
        work_group_layout.add_widget(OpenScreenButton(text='Группа',
                                                      screen_name=WorkGroupUI.screen_name,
                                                      screen_manager=self.sm))
        work_group_layout.add_widget(Label(text='Группа: '))
        # Фильтр групп
        work_group_layout.add_widget(ChainedFilterPopup(height=dp(30),
                                                      text=self.group_work,
                                                      dict_class=self.model_class,
                                                      owner_class=WorkGroup,
                                                      field='group_work',
                                                      modal_title='Фильр групп',
                                                      ui=self,
                                                      ))

        bl.add_widget(title_layout)
        bl.add_widget(back_layout)
        bl.add_widget(work_stage_layout)
        bl.add_widget(work_technology_layout)
        bl.add_widget(work_group_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
