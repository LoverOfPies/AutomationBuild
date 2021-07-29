from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from src.expimp.ImportUtils import import_base_unit

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
        import_base_unit(filename[0], self.ui)
        self.dismiss()

    def __init__(self, **kwargs):
        super(FileChoosePopup, self).__init__(**kwargs)
        self.size = [800, 600]
        self.size_hint = [None, None]
        self.auto_dismiss = False
