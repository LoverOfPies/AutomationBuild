from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from src.db.DbUtils import add_row
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.work.WorkGroup import WorkGroup
from src.gui.custom_uix.DoubleInput import DoubleInput
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class AddRowWorkPopup(Popup):
    ui_class = ObjectProperty()

    def add_value(self, obj):
        self.dismiss()
        base_unit = BaseUnit.select().where(BaseUnit.name == self.base_unit_input.text)
        work_group = WorkGroup.select().where(WorkGroup.name == self.work_group_input.text)
        model_obj = [
            {'name': str(self.name_input.text),
             'work_coefficient': str(self.work_coefficient_input.text),
             'client_price': str(self.client_price_input.text),
             'work_price': str(self.work_price_input.text),
             'base_unit': base_unit,
             'work_group': work_group}
        ]
        data = dict([
            ('model_class', self.ui_class.model_class),
            ('value', model_obj),
        ])
        add_row(data)
        self.ui_class.update_screen()

    def __init__(self, ui_class, **kwargs):
        super(AddRowWorkPopup, self).__init__(**kwargs)
        self.size = [600, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.ui_class = ui_class

        self.name_input = TextInput()
        self.work_coefficient_input = DoubleInput(multiline=False)
        self.client_price_input = DoubleInput(multiline=False)
        self.work_price_input = DoubleInput(multiline=False)
        self.base_unit_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                     modal_popup=ModalPopup, modal_title='Базовые единицы',
                                                     owner_class=BaseUnit)
        self.work_group_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                      modal_popup=ModalPopup, modal_title='Группы работ',
                                                      owner_class=WorkGroup)

        main_layout = BoxLayout(orientation='vertical')
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
                size:(root.width, root.height)
                size_hint_x: 1
                size_hint_y: None
                cols: 2
                height: self.minimum_height
                row_default_height: 50
                row_force_default: True''')

        data_layout.add_widget(Label(text='Наименование', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.name_input)
        data_layout.add_widget(Label(text='Коэффицент работы', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.work_coefficient_input)
        data_layout.add_widget(Label(text='Тариф клиента', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.client_price_input)
        data_layout.add_widget(Label(text='Тариф себестоимости', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.work_price_input)
        data_layout.add_widget(Label(text='Базовая единица', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.base_unit_input)
        data_layout.add_widget(Label(text='Группа работ', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.work_group_input)
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.fbind('on_press', self.add_value)
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
