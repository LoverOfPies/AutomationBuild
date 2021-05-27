from kivy.properties import ObjectProperty
from kivy.uix.button import Button


# Кнопка переключения между экранами
class OpenScreenButton(Button):
    screen_manager = ObjectProperty()
    screen_name = ObjectProperty()

    def on_press(self, *args):
        super(OpenScreenButton, self).on_press()
        self.screen_manager.current = self.screen_name
