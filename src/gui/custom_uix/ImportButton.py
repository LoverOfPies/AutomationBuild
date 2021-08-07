from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from src.gui.modal.FileChoosePopup import FileChoosePopup


# Кнопка вызова модального окна импорта данных
class ImportButton(Button):
    ui = ObjectProperty()
    popup_title = StringProperty()

    def on_press(self, *args):
        popup = FileChoosePopup(title=self.popup_title, ui=self.ui)
        popup.open()
