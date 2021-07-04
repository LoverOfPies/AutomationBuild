from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.dictionary.BaseUnitUI import BaseUnitUI
from src.gui.dictionary.CategoryUI import CategoryUI
from src.gui.dictionary.GroupUI import GroupUI
from src.gui.dictionary.MaterialUI import MaterialUI
from src.gui.dictionary.ProductUI import ProductUI
from src.gui.dictionary.ProjectUI import ProjectUI
from src.gui.dictionary.PropUI import PropUI
from src.gui.dictionary.ProviderUI import ProviderUI
from src.gui.dictionary.CityUI import CityUI
from src.gui.dictionary.SubgroupUI import SubgroupUI
from src.gui.dictionary.TechnologyUI import TechnologyUI
from src.gui.dictionary.UnitUI import UnitUI
from src.gui.dictionary.WorkMaterialUI import WorkMaterialUI
from src.gui.dictionary.WorkUI import WorkUI


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
    bl.add_widget(OpenScreenButton(text='Поставщики', screen_name=ProviderUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Базовые единицы', screen_name=BaseUnitUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Единицы измерения', screen_name=UnitUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Перечень свойств', screen_name=PropUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Категории', screen_name=CategoryUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Группы', screen_name=GroupUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Подгруппы', screen_name=SubgroupUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Материалы', screen_name=MaterialUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Товары', screen_name=ProductUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Технологии', screen_name=TechnologyUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Работы', screen_name=WorkUI.screen_name, screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Материалы для работы', screen_name=WorkMaterialUI.screen_name,
                                   screen_manager=sm))
    bl.add_widget(OpenScreenButton(text='Проекты', screen_name=ProjectUI.screen_name, screen_manager=sm))

    screen = Screen(name=screen_name)
    screen.add_widget(al)
    sm.add_widget(screen)

    # Создание экранов для справочников
    CityUI(screen_manager=sm)
    ProviderUI(screen_manager=sm)
    BaseUnitUI(screen_manager=sm)
    UnitUI(screen_manager=sm)
    PropUI(screen_manager=sm)
    CategoryUI(screen_manager=sm)
    GroupUI(screen_manager=sm)
    SubgroupUI(screen_manager=sm)
    MaterialUI(screen_manager=sm)
    ProductUI(screen_manager=sm)
    TechnologyUI(screen_manager=sm)
    WorkUI(screen_manager=sm)
    WorkMaterialUI(screen_manager=sm)
    ProjectUI(screen_manager=sm)


class MainApp(App):
    def build(self):
        self.title = 'AutomationBuild'
        sm = ScreenManager()
        main_screen(sm)
        dictionary_screen(sm)
        return sm
