from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна добавления записи
class AddRowButton(Button):
    ui = ObjectProperty()
    popup = ObjectProperty()
    popup_title = StringProperty()

    def on_press(self, *args):
        popup = self.popup(title=self.popup_title, ui_class=self.ui)
        popup.open()
