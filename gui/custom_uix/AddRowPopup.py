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


class AddRowPopup(Popup):
    dict_class = ObjectProperty()
    ui_class = ObjectProperty()
    name = TextInput()

    def add_value(self):
        self.dismiss()
        data = dict([
            ('model_class', self.ui_class.model_class),
            ('value', self.name.text),
        ])
        add_row(data)
        self.ui_class.update_screen()

    def __init__(self, ui_class, **kwargs):
        super(AddRowPopup, self).__init__(**kwargs)
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False

        self.ui_class = ui_class

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
        fields = ui_class.model_class._meta.fields.keys()
        for key in fields:
            if key != 'id':
                data_layout.add_widget(Label(text=str(key), size_hint_y=None, height=dp(30)))
                data_layout.add_widget(self.name)
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        save = Button(size_hint=[1, 0.2], text='Сохранить')
        main_layout.add_widget(save)
        save.on_press = self.add_value
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
