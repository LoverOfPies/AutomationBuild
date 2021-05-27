from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна изменения атрибута
class SelectableButton(Button):
    class_popup = ObjectProperty()
    popup_title = StringProperty()

    dict_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def on_press(self):
        popup = self.class_popup(self, title=self.popup_title,
                                 dict_class=self.dict_class, id_value=self.id_value, field=self.field)
        popup.open()
