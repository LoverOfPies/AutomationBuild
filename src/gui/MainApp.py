from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.dictionary.BaseUnitUI import BaseUnitUI
from src.gui.dictionary.material.MaterialUI import MaterialUI
from src.gui.dictionary.PropUI import PropUI
from src.gui.dictionary.provider.ProviderUI import ProviderUI
from src.gui.dictionary.provider.CityUI import CityUI
from src.gui.dictionary.UnitUI import UnitUI


def main_screen(sm):
    # Начальный экран
    screen_name = 'main_screen'
    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
    al.add_widget(bl)
    title_screen = Label(text='Система расчёта строительства', font_size='20sp')
    bl.add_widget(title_screen)
    bl.add_widget(OpenScreenButton(text='Справочники', screen_name='dictionary_screen', screen_manager=sm))
    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)


def dictionary_screen(sm):
    # Экран выбора справочников
    screen_name = 'dictionary_screen'
    parent_screen = 'main_screen'

    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .5])
    al.add_widget(bl)
    title_screen = Label(text='Справочники', font_size='20sp')
    bl.add_widget(title_screen)
    bl.add_widget(OpenScreenButton(text='Назад', screen_name=parent_screen, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Базовые единицы', screen_name=BaseUnitUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Единицы измерения', screen_name=UnitUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Свойства', screen_name=PropUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Поставщики', screen_name=ProviderUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Материалы', screen_name=MaterialUI.screen_name, screen_manager=sm))
    # bl.add_widget(OpenScreenButton(text='Работы', screen_name=WorkUI.screen_name, screen_manager=sm))

    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)

    # Создание экранов для справочников
    BaseUnitUI(screen_manager=sm)
    UnitUI(screen_manager=sm)
    PropUI(screen_manager=sm)

    CityUI(screen_manager=sm)
    ProviderUI(screen_manager=sm)

    MaterialUI(screen_manager=sm)


class MainApp(App):
    def build(self):
        self.title = 'AutomationBuild'
        sm = ScreenManager()
        main_screen(sm)
        dictionary_screen(sm)
        return sm
