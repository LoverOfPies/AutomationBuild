from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка вызова модального окна изменения атрибута
class SelectableModalButton(Button):
    modal_popup = ObjectProperty()

    def on_press(self):
        popup = self.modal_popup(self)
        popup.open()
