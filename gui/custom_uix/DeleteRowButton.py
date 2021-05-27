from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from db.DbUtils import delete_row


class DeleteRowButton(Button):
    ui = ObjectProperty()
    id_value = StringProperty()

    def on_press(self, *args):
        super(DeleteRowButton, self).on_press()
        data = dict([
            ('model_class', self.ui.model_class),
            ('id_value', self.id_value),
        ])
        delete_row(data)
        self.ui.update_screen()
