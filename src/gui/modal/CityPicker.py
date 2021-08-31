from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.label import Label

from src.db.models.provider.City import City


class SelectCityButton(Button):
    popup = ObjectProperty()
    button_obj = ObjectProperty()
    name_row = StringProperty()
    owner_class = ObjectProperty()

    def on_press(self):
        self.button_obj.text = self.name_row
        self.popup.dismiss()


class CityPickerPopup(Popup):
    button_obj = ObjectProperty()

    def __init__(self, button_obj, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Выбор города'
        self.owner_class = City
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
        rows = self.owner_class.select()
        for row in rows:
            data_layout.add_widget(Label(text=str(row.name), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectCityButton(text='Выбрать', height=dp(30), popup=self,
                                                   name_row=row.name, button_obj=button_obj,
                                                   owner_class=self.owner_class))
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        main_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)

        self.add_widget(main_layout)

class CityPicker(Button):

    def on_press(self):
        popup = CityPickerPopup(self)
        popup.open()
