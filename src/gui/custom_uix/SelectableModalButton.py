from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна изменения атрибута
class SelectableModalButton(Button):
    modal_popup = ObjectProperty()
    change_flag = BooleanProperty()
    modal_title = StringProperty()
    ui = ObjectProperty()

    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def on_press(self):
        if not self.change_flag:
            self.dict_class = None
            self.id_value = ''
            self.field = ''
        popup = self.modal_popup(self, self.change_flag, self.dict_class, self.owner_class, self.id_value, self.field,
                                 self.modal_title, self.ui)
        popup.open()
