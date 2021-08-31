from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from src.db.DbUtils import add_row

from src.db.models.project.WorkGroupEquipment import WorkGroupEquipment


class SelectRowButton(Button):
    button_obj = ObjectProperty()
    popup = ObjectProperty()
    name_row = StringProperty()
    ui_class = ObjectProperty()

    owner_class = ObjectProperty()
    dict_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def on_press(self):
        work_group = self.owner_class.select().where(self.owner_class.name == self.name_row)
        equipment = self.dict_class.select().where(self.dict_class.name == self.ui_class.filter_name)
        model_obj = [
            {'work_group': work_group,
             'equipment': equipment
            }
        ]
        data = dict([
            ('model_class', WorkGroupEquipment),
            ('value', model_obj)
        ])
        add_row(data)
        self.ui_class.update_screen()
        self.popup.dismiss()


class AddEquipmentWorkgroupPopup(Popup):
    button_obj = ObjectProperty()
    change_flag = BooleanProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()
    ui_class = ObjectProperty()

    def __init__(self, button_obj, change_flag, dict_class, owner_class, id_value, field, modal_title, ui_class, **kwargs):
        super().__init__(**kwargs)
        self.title = modal_title
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False

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
        data_layout.add_widget(Label(text='', size_hint_y=None, height=dp(30)))
        rows = owner_class.select()
        for row in rows:
            data_layout.add_widget(Label(text=str(row.name), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectRowButton(text='Выбрать', height=dp(30), popup=self,
                                                   name_row=row.name, button_obj=button_obj,
                                                   dict_class=dict_class, owner_class=owner_class,
                                                   id_value=id_value,
                                                   field=field, ui_class=ui_class))
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
