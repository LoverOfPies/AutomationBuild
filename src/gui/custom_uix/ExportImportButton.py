from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.button import Button

from src.expimp.ExportUtils import export_table
from src.expimp.ImportUtils import import_table


# Кнопка вызова экспорта данных
class ExportImportButton(Button):
    ui = ObjectProperty()
    is_import = BooleanProperty()

    def on_press(self, *args):
        if self.is_import:
            import_table(self.ui)
        else:
            export_table(self.ui.model_class)
