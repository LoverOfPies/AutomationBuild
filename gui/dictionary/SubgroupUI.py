from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from db.models.Group import Group
from db.models.Subgroup import Subgroup
from gui.custom_uix.AddRowButton import AddRowButton
from gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from gui.custom_uix.DeleteRowButton import DeleteRowButton
from gui.custom_uix.OpenScreenButton import OpenScreenButton
from gui.custom_uix.SelectableButton import SelectableButton
from gui.custom_uix.SelectableModalButton import SelectableModalButton
from gui.add_dictionary.AddRowSubgroupPopup import AddRowSubgroupPopup
from gui.modal.GroupModalPopup import GroupModalPopup


class SubgroupUI:
    screen_name = 'subgroup_screen'
    parent_screen = 'dictionary_screen'
    model_class = Subgroup
    screen = Screen(name=screen_name)

    def __init__(self, screen_manager):
        self.sm = screen_manager
        self.update_screen()
        self.sm.add_widget(self.screen)

    def update_screen(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.main_layout())

    def main_layout(self):
        main_anchor = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[.7, .9])
        main_anchor.add_widget(bl)

        # Вывод данных
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
        size:(root.width, root.height)
        size_hint_x: 1
        size_hint_y: None
        cols: 4
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='id', height=dp(30)))
        data_layout.add_widget(Label(text='Наименование', height=dp(30)))
        data_layout.add_widget(Label(text='Группа', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        subgroups = self.model_class.select()
        for subgroup in subgroups:
            data_layout.add_widget(Label(text=str(subgroup.id), height=dp(30)))
            data_layout.add_widget(SelectableButton(text=str(subgroup.name), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить наименование",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(subgroup.id),
                                                    field='name'
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(subgroup.group.name), height=dp(30),
                                                         modal_popup=GroupModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Group,
                                                         id_value=str(subgroup.id),
                                                         field='group'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(subgroup.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowSubgroupPopup,
                                              popup_title='Добавление записи "Подгруппа"'))

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
