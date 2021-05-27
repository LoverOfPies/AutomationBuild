from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from db.DbUtils import delete_row
from gui.custom_uix.AddRowPopup import AddRowPopup


class AddRowButton(Button):
    ui = ObjectProperty()

    def on_press(self, *args):
        popup = AddRowPopup(title='Добавление записи "Город"', ui_class=self.ui)
        popup.open()
