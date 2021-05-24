from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from gui.custom_uix.OpenScreenButton import OpenScreenButton
from gui.dictionary.CityUI import CityUI
from gui.dictionary.DictionaryUI import provider_screen


def main_screen(sm):
    screen_name = 'main_screen'
    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
    al.add_widget(bl)
    bl.add_widget(OpenScreenButton(text='Справочники', screenname='dictionary_screen', screenmanager=sm))
    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)


def dictionary_screen(sm):
    screen_name = 'dictionary_screen'
    parent_screen = 'main_screen'

    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
    al.add_widget(bl)
    bl.add_widget(OpenScreenButton(text='Назад', screenname=parent_screen, screenmanager=sm))
    bl.add_widget(OpenScreenButton(text='Города', screenname='city_screen', screenmanager=sm))
    bl.add_widget(OpenScreenButton(text='Поставщики', screenname='provider_screen', screenmanager=sm))

    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)
    CityUI(screen_manager=sm).city_screen()
    provider_screen(sm)


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sc2 = Screen(name='dictionary_screen')
        sc2.add_widget(Label(text='another screen'))

        main_screen(sm)
        dictionary_screen(sm)
        return sm
