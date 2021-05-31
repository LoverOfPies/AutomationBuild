from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from gui.custom_uix.OpenScreenButton import OpenScreenButton
from gui.dictionary.BaseUnitUI import BaseUnitUI
from gui.dictionary.CategoryUI import CategoryUI
from gui.dictionary.ProjectUI import ProjectUI
from gui.dictionary.ProviderUI import ProviderUI
from gui.dictionary.CityUI import CityUI


def main_screen(sm):
    # Начальный экран
    screen_name = 'main_screen'
    al = AnchorLayout()
    bl = BoxLayout(orientation='vertical', size_hint=[.7, .2])
    al.add_widget(bl)
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
    bl.add_widget(OpenScreenButton(text='Назад', screen_name=parent_screen, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Города', screen_name=CityUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Поставщики', screen_name=ProviderUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Базовые единицы', screen_name=BaseUnitUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Категории', screen_name=CategoryUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Проекты', screen_name=ProjectUI.screen_name, screen_manager=sm))

    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)

    # Создание экранов для справочников
    CityUI(screen_manager=sm)
    ProviderUI(screen_manager=sm)
    BaseUnitUI(screen_manager=sm)
    CategoryUI(screen_manager=sm)
    ProjectUI(screen_manager=sm)


class MainApp(App):
    def build(self):
        self.title = 'AutomationBuild'
        sm = ScreenManager()
        main_screen(sm)
        dictionary_screen(sm)
        return sm
