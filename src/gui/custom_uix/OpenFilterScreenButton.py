from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button


# Кнопка переключения между экранами
from src.gui.dictionary.ProductUI import ProductUI


class OpenFilterScreenButton(Button):
    screen_manager = ObjectProperty()
    screen_name = ObjectProperty()
    filter_name = StringProperty()

    def on_press(self, *args):
        ProductUI(screen_manager=self.screen_manager, filter_name=self.filter_name)
        super(OpenFilterScreenButton, self).on_press()
        self.screen_manager.current = self.screen_name
