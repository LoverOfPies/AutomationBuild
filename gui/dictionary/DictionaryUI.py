from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from gui.custom_uix.OpenScreenButton import OpenScreenButton


def provider_screen(sm):
    screen_name = 'provider_screen'
    parent_screen = 'dictionary_screen'

    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
    al.add_widget(bl)
    bl.add_widget(OpenScreenButton(text='Назад', screenname=parent_screen, screenmanager=sm))

    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)
