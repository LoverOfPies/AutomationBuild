from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from src.db.DbUtils import add_row
from src.db.models.material.Material import Material
from src.db.models.work.Work import Work
from src.gui.custom_uix.DoubleInput import DoubleInput
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class AddRowWorkMaterialPopup(Popup):
    ui_class = ObjectProperty()

    def add_value(self, obj):
        self.dismiss()
        material = Material.select().where(Material.name == self.material_input.text)
        work = Work.select().where(Work.name == self.ui_class.filter_name)
        model_obj = [
            {'amount': str(self.amount_input.text),
             'material': material,
             'work': work}
        ]
        data = dict([
            ('model_class', self.ui_class.model_class),
            ('value', model_obj),
        ])
        add_row(data)
        self.ui_class.update_screen()

    def __init__(self, ui_class, **kwargs):
        super(AddRowWorkMaterialPopup, self).__init__(**kwargs)
        self.size = [600, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.ui_class = ui_class

        self.amount_input = DoubleInput()
        self.material_input = SelectableModalButton(text='', size_hint_y=None, height=dp(30), change_flag=False,
                                                    modal_popup=ModalPopup, modal_title='Материалы',
                                                    owner_class=Material)

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

        data_layout.add_widget(Label(text='Количество материала', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.amount_input)
        data_layout.add_widget(Label(text='Материал', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.material_input)
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.fbind('on_press', self.add_value)
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
