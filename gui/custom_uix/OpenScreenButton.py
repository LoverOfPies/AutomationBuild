from kivy.properties import ObjectProperty
from kivy.uix.button import Button


class OpenScreenButton(Button):
    screenmanager = ObjectProperty()
    screenname = ObjectProperty()

    def on_press(self, *args):
        super(OpenScreenButton, self).on_press()
        self.screenmanager.current = self.screenname
