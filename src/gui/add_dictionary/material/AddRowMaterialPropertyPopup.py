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
from src.db.models.base.Prop import Prop
from src.db.models.base.Unit import Unit
from src.gui.custom_uix.DoubleInput import DoubleInput
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class AddRowMaterialPropertyPopup(Popup):
    ui_class = ObjectProperty()

    def add_value(self, obj):
        self.dismiss()
        material = Material.select().where(Material.name == self.ui_class.filter_name)
        prop = Prop.select().where(Prop.name == self.prop_input.text)
        unit = Unit.select().where(Unit.name == self.unit_input.text)
        model_obj = [
            {'amount': str(self.amount_input.text),
             'material': material,
             'prop': prop,
             'unit': unit}
        ]
        data = dict([
            ('model_class', self.ui_class.model_class),
            ('value', model_obj),
        ])
        add_row(data)
        self.ui_class.update_screen()

    def __init__(self, ui_class, **kwargs):
        super(AddRowMaterialPropertyPopup, self).__init__(**kwargs)
        self.size = [600, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.ui_class = ui_class

        self.amount_input = DoubleInput()
        self.prop_input = SelectableModalButton(size_hint_y=None, height=dp(30),
                                                text='',
                                                change_flag=False,
                                                modal_popup=ModalPopup,
                                                modal_title='Свойства',
                                                owner_class=Prop)
        self.unit_input = SelectableModalButton(size_hint_y=None, height=dp(30),
                                                text='',
                                                change_flag=False,
                                                modal_popup=ModalPopup,
                                                modal_title='Единицы измерения',
                                                owner_class=Unit)

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

        data_layout.add_widget(Label(text='Количество', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.amount_input)
        data_layout.add_widget(Label(text='Свойство', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.prop_input)
        data_layout.add_widget(Label(text='Единица измерения', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(self.unit_input)
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.fbind('on_press', self.add_value)
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
