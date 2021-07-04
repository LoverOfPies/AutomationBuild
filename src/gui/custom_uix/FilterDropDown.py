from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class FilterDropDown(DropDown):
    dict_class = ObjectProperty()
    main_button = ObjectProperty()

    def change_attribute(self, button):
        self.main_button.text = button.text
        self.ui

    def __init__(self, dict_class, **kwargs):
        super().__init__(**kwargs)
        all_attribute = Button(text='Все', size_hint_y=None, height=44)
        all_attribute.bind(on_press=self.change_attribute)
        self.add_widget(all_attribute)
        attributes = dict_class.select()
        for attribute in attributes:
            attribute_button = Button(text=str(attribute.name), size_hint_y=None, height=44)
            attribute_button.bind(on_press=self.change_attribute)
            self.add_widget(attribute_button)
