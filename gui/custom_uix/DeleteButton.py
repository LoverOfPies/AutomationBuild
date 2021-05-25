from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from db.DbUtils import delete_row


class DeleteButton(Button):
    model_class = ObjectProperty()
    ui = ObjectProperty()
    id_value = StringProperty()

    def on_press(self, *args):
        super(DeleteButton, self).on_press()
        data = dict([
            ('model_class', self.model_class),
            ('id_value', self.id_value),
        ])
        self.ui.city_screen()
        delete_row(data)
