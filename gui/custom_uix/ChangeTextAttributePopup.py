from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from db.DbUtils import change_attribute


# Модальное окно для изменения текстового атрибута
class ChangeTextAttributePopup(Popup):
    button_obj = ObjectProperty()
    dict_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    # Сохранить изменение атрибута в бд
    def save_value(self):
        self.button_obj.text = self.attribute_input.text
        self.dismiss()
        data = dict([
            ('model_class', self.dict_class),
            ('id_value', self.id_value),
            ('field', self.field),
            ('value', self.attribute_input.text)
        ])
        change_attribute(data)

    def __init__(self, button_obj, dict_class, id_value, field, **kwargs):
        super(ChangeTextAttributePopup, self).__init__(**kwargs)
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False

        self.button_obj = button_obj
        self.dict_class = dict_class
        self.id_value = id_value
        self.field = field

        button_layout = BoxLayout(orientation='vertical')
        self.attribute_input = TextInput(multiline=False, text=str(button_obj.text))
        button_layout.add_widget(self.attribute_input)
        save = Button(size_hint=[1, 0.2], text='Сохранить')
        button_layout.add_widget(save)
        save.on_press = self.save_value
        cancel = Button(size_hint=[1, 0.2], text='Отмена')
        button_layout.add_widget(cancel)
        cancel.bind(on_press=self.dismiss)
        self.add_widget(button_layout)
