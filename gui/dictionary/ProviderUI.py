from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from db.models.Provider import Provider
from gui.custom_uix.OpenScreenButton import OpenScreenButton


class ProviderUI:
    screen_name = 'provider_screen'
    parent_screen = 'dictionary_screen'
    model_class = Provider
    screen = Screen(name=screen_name)

    def __init__(self, screen_manager):
        self.sm = screen_manager
        self.screen.add_widget(self.provider_screen())
        self.sm.add_widget(self.screen)

    def update_screen(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.provider_screen())

    def provider_screen(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
        al.add_widget(bl)
        bl.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        return al
