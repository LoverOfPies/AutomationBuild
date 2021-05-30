from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна изменения атрибута
class SelectRowButton(Button):
    button_obj = ObjectProperty()
    popup = ObjectProperty()
    name_row = StringProperty()

    def on_press(self):
        self.button_obj.text = self.name_row
        self.popup.dismiss()
