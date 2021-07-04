from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна изменения атрибута
class SelectableButton(Button):
    class_popup = ObjectProperty()
    is_double = BooleanProperty()
    popup_title = StringProperty()

    dict_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def on_press(self):
        popup = self.class_popup(self, title=self.popup_title,
                                 dict_class=self.dict_class, id_value=self.id_value, field=self.field,
                                 is_double=self.is_double)
        popup.open()
