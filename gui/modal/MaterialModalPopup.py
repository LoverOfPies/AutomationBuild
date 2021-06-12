from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from db.models.Material import Material
from gui.custom_uix.SelectRowButton import SelectRowButton


class MaterialModalPopup(Popup):
    button_obj = ObjectProperty()
    change_flag = BooleanProperty()

    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def __init__(self, button_obj, change_flag, dict_class, owner_class, id_value, field, **kwargs):
        super(MaterialModalPopup, self).__init__(**kwargs)
        self.title = 'Материалы'
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False

        main_layout = BoxLayout(orientation='vertical')
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
                size:(root.width, root.height)
                size_hint_x: 1
                size_hint_y: None
                cols: 3
                height: self.minimum_height
                row_default_height: 50
                row_force_default: True''')
        data_layout.add_widget(Label(text='id', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(Label(text='Наименование', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(Label(text='', size_hint_y=None, height=dp(30)))
        materials = Material.select()
        for material in materials:
            data_layout.add_widget(Label(text=str(material.id), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(Label(text=str(material.name), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectRowButton(text='Выбрать', height=dp(30), popup=self,
                                                   name_row=material.name, button_obj=button_obj,
                                                   change_flag=change_flag,
                                                   dict_class=dict_class, owner_class=owner_class,
                                                   id_value=id_value,
                                                   field=field))
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)