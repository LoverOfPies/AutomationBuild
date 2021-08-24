from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from src.expimp.ExportUtils import export_table
from src.gui.modal.FileChoosePopup import FileChoosePopup


# Кнопка вызова экспорта данных
class ExportButton(Button):
    model = ObjectProperty()

    def on_press(self, *args):
        export_table(self.model)
