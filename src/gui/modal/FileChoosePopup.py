from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.base.Prop import Prop
from src.db.models.base.Unit import Unit
from src.db.models.material.Material import Material
from src.db.models.work.Work import Work
from src.expimp.ImportUtils import import_single_row, import_material, import_work

Builder.load_string("""
<FileChoosePopup>:
    id: fileChoosePopup
    BoxLayout:
        GridLayout:
            size:(root.width, root.height)
            cols: 1
            height: self.minimum_height
            row_default_height: 50
            Button:
                text: "Открыть"
                size_hint: [1, 0.2]
                on_release: fileChoosePopup.select_file(filechooser.selection)
            FileChooserListView:
                id: filechooser
            Button:
                text: 'Отмена'
                size_hint: [1, 0.2]
                on_release: root.dismiss()
""")


class FileChoosePopup(Popup):
    ui = ObjectProperty()

    def select_file(self, filename):
        if self.ui.model_class == BaseUnit:
            import_single_row(filename[0], self.ui, 'БазовыеЕдиницы')
        if self.ui.model_class == Prop:
            import_single_row(filename[0], self.ui, 'СвойстваМатериалов')
        if self.ui.model_class == Unit:
            import_single_row(filename[0], self.ui, 'ЕдиницыИзмерения')
        if self.ui.model_class == Material:
            import_material(filename[0], self.ui, 'Материалы')
        if self.ui.model_class == Work:
            import_work(filename[0], self.ui, 'Работы')
        self.dismiss()

    def __init__(self, **kwargs):
        super(FileChoosePopup, self).__init__(**kwargs)
        self.size = [800, 600]
        self.size_hint = [None, None]
        self.auto_dismiss = False
