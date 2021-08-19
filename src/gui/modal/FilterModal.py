from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

# кнопка выбора
class SelectRowButton(Button):
    ui_class = ObjectProperty()
    button_obj = ObjectProperty()
    popup = ObjectProperty()
    name_row = StringProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = StringProperty()

    def on_press(self):
        city = self.owner_class.select().where(self.owner_class.name == self.name_row)
        providers = self.dict_class.select().where(self.dict_class.city == city)
        self.ui_class.providers = providers
        self.ui_class.filter_flag = True
        self.ui_class.filter_btn_text = self.name_row
        self.popup.dismiss()
        self.ui_class.update_screen()

# модальное окно фильтра
class ModalPopup(Popup):
    ui_class = ObjectProperty()
    button_obj = ObjectProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = StringProperty()

    def __init__(self, button_obj, ui_class, dict_class, owner_class, field, modal_title, **kwargs):
        super(ModalPopup, self).__init__(**kwargs)

        self.title = modal_title
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.ui_class = ui_class

        main_layout = BoxLayout(orientation='vertical')
        data_scroll = ScrollView(do_scroll_y=True, do_scroll_x=False)
        data_layout = Builder.load_string('''GridLayout:
                size:(root.width, root.height)
                size_hint_x: 1
                size_hint_y: None
                cols: 2
                height: self.minimum_height
                row_default_height: 50
                row_force_default: True''')
        data_layout.add_widget(Label(text='Наименование', size_hint_y=None, height=dp(30)))
        data_layout.add_widget(Label(text='', size_hint_y=None, height=dp(30)))
        rows = owner_class.select()
        for row in rows:
            data_layout.add_widget(Label(text=str(row.name), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectRowButton(text='Выбрать', height=dp(30), popup=self,
                                                   name_row=row.name, button_obj=button_obj, ui_class=ui_class,
                                                   dict_class=dict_class, owner_class=owner_class,
                                                   field=field))
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        cancel = Button(size_hint=[1, 0.2], text='Сбросить')
        main_layout.add_widget(cancel)

        cancel.bind(on_press=self.reset_filter)

        self.add_widget(main_layout)
    
    def reset_filter(modal, self):
        modal.ui_class.filter_flag = False
        modal.ui_class.filter_btn_text = 'Не выбранно'
        modal.ui_class.update_screen()
        modal.dismiss()
            

# Кнопка вызова фильтра
class FilterModal(Button):
    ui = ObjectProperty()
    modal_title = StringProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = StringProperty()
    modal_popup = ModalPopup

    def on_press(self):
        popup = self.modal_popup(self, self.ui, self.dict_class, self.owner_class, self.field, self.modal_title)
        popup.open()

