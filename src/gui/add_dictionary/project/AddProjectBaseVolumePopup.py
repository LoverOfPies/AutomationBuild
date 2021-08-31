from operator import mod
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from src.db.DbUtils import add_row
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.project.Project import Project
from src.gui.custom_uix.DoubleInput import DoubleInput
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class AddProjectBaseVolumePopup(Popup):
    button_obj = ObjectProperty()
    change_flag = BooleanProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()
    ui_class = ObjectProperty()

    def add_value(self, obj):
        self.dismiss()
        base_unit = BaseUnit.select().where(BaseUnit.name == self.base_unit_input.text)
        project = Project.select().where(Project.name == self.ui_class.filter_name)
        model_obj = [
            {
                'amount': str(self.amount_input.text),
                'base_unit': base_unit,
                'project': project
            }
        ]
        data = dict([
            ('model_class', self.ui_class.model_class),
            ('value', model_obj),
        ])
        add_row(data)
        self.ui_class.update_screen()

    def __init__(self, button_obj, change_flag, dict_class, owner_class, id_value, field, modal_title, ui, **kwargs):
        super().__init__(**kwargs)
        self.size = [600, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.title = modal_title
        self.owner_class = owner_class
        self.dict_class = dict_class
        self.ui_class = ui

        self.amount_input = DoubleInput(multiline=False)
        self.base_unit_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                     modal_popup=ModalPopup, modal_title='Базовые единицы',
                                                     owner_class=BaseUnit, ui=self)

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

        data_layout.add_widget(
            Label(text='Количество', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.amount_input)
        data_layout.add_widget(
            Label(text='Базовая единица', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.base_unit_input)

        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.fbind('on_press', self.add_value)
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
