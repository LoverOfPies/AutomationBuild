from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка переключения между экранами
class OpenFilterScreenButton(Button):
    screen_manager = ObjectProperty()
    filter_ui = ObjectProperty()
    filter_name = StringProperty()

    def on_press(self, *args):
        self.filter_ui(screen_manager=self.screen_manager, filter_name=self.filter_name)
        super(OpenFilterScreenButton, self).on_press()
        self.screen_manager.current = self.filter_ui.screen_name
