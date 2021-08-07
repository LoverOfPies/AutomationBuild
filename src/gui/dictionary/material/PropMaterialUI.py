from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from src.db.models.Material import Material
from src.db.models.Product import Product
from src.db.models.Prop import Prop
from src.db.models.PropMaterial import PropMaterial
from src.db.models.Provider import Provider
from src.db.models.Unit import Unit
from src.gui.add_dictionary.AddRowProductPopup import AddRowProductPopup
from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ChangeTextAttributePopup import ChangeTextAttributePopup
from src.gui.custom_uix.DeleteRowButton import DeleteRowButton
from src.gui.custom_uix.OpenScreenButton import OpenScreenButton
from src.gui.custom_uix.SelectableButton import SelectableButton
from src.gui.custom_uix.SelectableModalButton import SelectableModalButton
from src.gui.modal.ModalPopup import ModalPopup


class PropMaterialUI:
    screen_name = 'propmaterial_screen'
    parent_screen = 'material_screen'
    model_class = PropMaterial
    screen = Screen(name=screen_name)
    filter_name = ''

    def __init__(self, screen_manager, filter_name):
        self.sm = screen_manager
        self.filter_name = filter_name
        self.update_screen()
        if screen_manager.has_screen('propmaterial_screen'):
            screen_manager.remove_widget(screen_manager.get_screen('propmaterial_screen'))
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
        cols: 5
        height: self.minimum_height
        row_default_height: 50
        row_force_default: True''')
        data_layout.add_widget(Label(text='Количество', height=dp(30)))
        data_layout.add_widget(Label(text='Свойство', height=dp(30)))
        data_layout.add_widget(Label(text='Единица измерения', height=dp(30)))
        data_layout.add_widget(Label(text='', height=dp(30)))
        material = Material.select().where(Material.name == self.filter_name)
        propMaterials = PropMaterial.select().where(PropMaterial.material == material)
        for propMaterial in propMaterials:
            data_layout.add_widget(SelectableButton(text=str(propMaterial.amount), size_hint_y=None, height=dp(30),
                                                    popup_title="Изменить количество",
                                                    class_popup=ChangeTextAttributePopup,
                                                    dict_class=self.model_class,
                                                    id_value=str(propMaterial.id),
                                                    field='amount', is_double=False
                                                    ))
            data_layout.add_widget(SelectableModalButton(text=str(propMaterial.prop.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Prop,
                                                         id_value=str(propMaterial.id),
                                                         field='prop', modal_title='Свойства'
                                                         ))
            data_layout.add_widget(SelectableModalButton(text=str(propMaterial.unit.name), height=dp(30),
                                                         modal_popup=ModalPopup, change_flag=True,
                                                         dict_class=self.model_class, owner_class=Unit,
                                                         id_value=str(propMaterial.id),
                                                         field='unit', modal_title='Единицы измерения'
                                                         ))
            data_layout.add_widget(DeleteRowButton(text='Удалить', height=dp(30),
                                                   id_value=str(propMaterial.id), ui=self))
        data_scroll.add_widget(data_layout)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', size_hint=[1, .4], padding=[0, 30])
        # button_layout.add_widget(AddRowButton(text='Добавить', ui=self, popup=AddRowProductPopup,
        #                                       popup_title='Добавление записи "Свойство материала"'))

        back_layout = BoxLayout(size_hint=[1, .2], padding=[0, 5])
        back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=self.parent_screen, screen_manager=self.sm))

        bl.add_widget(back_layout)
        bl.add_widget(data_scroll)
        bl.add_widget(button_layout)

        return main_anchor
