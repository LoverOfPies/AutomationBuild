from kivy.properties import ObjectProperty
from kivy.uix.button import Button


class AddRowButton(Button):
    ui = ObjectProperty()
    popup = ObjectProperty()

    def on_press(self, *args):
        popup = self.popup(title='Добавление записи "Город"', ui_class=self.ui)
        popup.open()
