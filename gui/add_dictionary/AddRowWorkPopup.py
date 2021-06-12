from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from db.DbUtils import add_row
from db.models.BaseUnit import BaseUnit
from db.models.Technology import Technology
from gui.custom_uix.SelectableModalButton import SelectableModalButton
from gui.modal.BaseUnitModalPopup import BaseUnitModalPopup
from gui.modal.TechnologyModalPopup import TechnologyModalPopup


class AddRowWorkPopup(Popup):
    ui_class = ObjectProperty()

    def add_value(self, obj):
        self.dismiss()
        baseunit = BaseUnit.select().where(BaseUnit.name == self.baseunit_input.text)
        technology = Technology.select().where(Technology.name == self.technology_input.text)
        model_obj = [
            {'name': str(self.name_input.text),
             'baseunit_id': baseunit,
             'technology_id': technology}
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
        self.baseunit_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                    modal_popup=BaseUnitModalPopup)
        self.technology_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                modal_popup=TechnologyModalPopup)

        main_layout = BoxLayout(orientation='vertical')
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
                size:(root.width, root.height)
                size_hint_x: 1
                size_hint_y: None
                cols: 4
                height: self.minimum_height
                row_default_height: 50
                row_force_default: True''')

        data_layout.add_widget(Label(text='Наименование', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.name_input)
        data_layout.add_widget(Label(text='Базовая единица', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.baseunit_input)
        data_layout.add_widget(Label(text='Технология', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.technology_input)
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.fbind('on_press', self.add_value)
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
