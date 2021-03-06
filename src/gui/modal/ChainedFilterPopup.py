from functools import partial
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty # pylint: disable=no-name-in-module
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

def get_next_field_of_dict(dictionary, field, direction=1):
    temp = list(dictionary)
    try:
        next_field = temp[temp.index(field) + direction]
    except (ValueError, IndexError):
        next_field = None

    if temp.index(field) + direction < 0:
            next_field = None

    return next_field

# кнопка выбора
# да я ебанутый (dxr)
class SelectRowButton(Button):
    ui_class = ObjectProperty()
    button_obj = ObjectProperty()
    popup = ObjectProperty()
    name_row = StringProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = StringProperty()

    def set_filter_selection(self) -> list:
        self.ui_class.selection_chain[self.field]['id'] = getattr(self.dict_class, self.field)
        self.ui_class.selection_chain[self.field]['last_choice'] = self.name_row
        items = self.owner_class.select().where(self.owner_class.name == self.name_row)

        filtered_list = []
        final_list = []
        for chain_member in self.ui_class.selection_chain.items():
            if chain_member[1]['id'] is not None and chain_member[0] == self.field:
                self.ui_class.selection_chain[self.field]['selection'] = [item for item in self.dict_class.select().where(chain_member[1]['id'] == items)]
                next_field = get_next_field_of_dict(self.ui_class.selection_chain, self.field)
                if next_field is not None:
                    self.ui_class.selection_chain[next_field]['enabled'] = True

        for chain_member in self.ui_class.selection_chain.items():
            if chain_member[1]['selection'] is not None and chain_member[0] == self.field:
                for item in chain_member[1]['selection']:
                    filtered_list.append(item)

        
        def recursion_select(flist, field):

            next_field = get_next_field_of_dict(self.ui_class.selection_chain, field)
            next_next_field = get_next_field_of_dict(self.ui_class.selection_chain, field, 2)

            fl = []

            if next_next_field is not None:
                for item in flist:
                    selection = self.ui_class.selection_chain[next_next_field]['model'].select().where(getattr(self.ui_class.selection_chain[next_next_field]['model'], next_field) == item)
                    for s in selection:
                        fl.append(s)

            if next_next_field is not None:
                recursion_select(fl, next_field)
            else:
                if next_field is not None:
                    for item in flist:
                        selection = self.ui_class.model_class.select().where(getattr(self.ui_class.model_class, next_field) == item)
                        for s in selection:
                            final_list.append(s)
                else:
                    final_list.extend(filtered_list)

        recursion_select(filtered_list, self.field)

        return final_list

    def on_press(self):

        if not self.ui_class.last_selection == self.field:
            self.popup.reset_filter(self.popup, reset_items=False)

        final_list = self.set_filter_selection()

        self.ui_class.items_list = final_list
        self.ui_class.filter_flag = True


        setattr(self.ui_class, self.field, self.name_row)
        self.popup.dismiss()
        self.ui_class.update_screen()

# модальное окно фильтра
class ModalPopup(Popup):
    ui_class = ObjectProperty()
    button_obj = ObjectProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = ObjectProperty()
    modal_title = StringProperty()

    def __init__(self, button_obj, ui_class, dict_class, owner_class, field, modal_title, **kwargs):
        super(ModalPopup, self).__init__(**kwargs)

        self.title = modal_title
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.ui_class = ui_class
        self.dict_class = dict_class
        self.owner_class = owner_class
        self.field = field

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
        rows = []
        all_rows = owner_class.select()
        for chain_member in self.ui_class.selection_chain.items():
            if chain_member[1]['selection'] is not None:
                for row in all_rows:
                    if row in chain_member[1]['selection']:
                        rows.append(row)
        if len(rows) == 0:
            rows = owner_class.select()
        for row in rows:
            data_layout.add_widget(Label(text=str(row.name), size_hint_y=None, height=dp(30)))
            data_layout.add_widget(SelectRowButton(text='Выбрать', height=dp(30), popup=self,
                                                   name_row=row.name, button_obj=button_obj, ui_class=ui_class,
                                                   dict_class=dict_class, owner_class=owner_class, field=field))
        data_scroll.add_widget(data_layout)
        main_layout.add_widget(data_scroll)

        cancel = Button(size_hint=[1, 0.2], text='Сбросить')
        main_layout.add_widget(cancel)

        buttoncallback = partial(self.reset_filter, reset_items=True)
        cancel.bind(on_press=buttoncallback) # pylint: disable=no-member

        self.add_widget(main_layout)
    
    def reset_filter(modal, _self, reset_items=False): # pylint: disable=no-self-argument
        if reset_items:
            prev_field = get_next_field_of_dict(modal.ui_class.selection_chain, modal.field, -1)
            if prev_field is not None:
                last_name = modal.ui_class.selection_chain[prev_field]['last_choice']
                owner_class = modal.ui_class.selection_chain[prev_field]['model']
                dict_class = modal.owner_class

                sel = SelectRowButton(text='Выбрать', height=dp(30), popup=modal, name_row=last_name, button_obj=None, ui_class=modal.ui_class,
                                                    dict_class=dict_class, owner_class=owner_class, field=prev_field)
                final_list = sel.set_filter_selection()
                modal.ui_class.items_list = final_list
            else:
                modal.ui_class.filter_flag = False

        for key, value in reversed(modal.ui_class.selection_chain.items()):
            setattr(modal.ui_class, key, 'Не выбранно')
            if key == modal.field:
                break
            value['enabled'] = False
            value['id'] = None
            value['selection'] = None

        modal.ui_class.update_screen()
        modal.dismiss()

# Кнопка вызова фильтра
class ChainedFilterPopup(Button):
    ui = ObjectProperty()
    modal_title = StringProperty()
    dict_class = ObjectProperty()
    owner_class = ObjectProperty()
    field = StringProperty()

    modal_popup = ModalPopup

    enabled = BooleanProperty(False)

    def __init__(self, ui, modal_title, dict_class, owner_class, field, **kwargs):
        super(ChainedFilterPopup, self).__init__(**kwargs)

        self.ui = ui
        self.modal_title = modal_title
        self.dict_class = dict_class
        self.owner_class = owner_class
        self.field = field

        if self.ui.selection_chain[self.field]['enabled']:
            self.background_color = [1,1,1,1]
            self.color = [1,1,1,1]
            self.enabled = True
        else:
            self.background_color = [1,1,1,.3]
            self.color = [1,1,1,.5]
            self.enabled = False

    def on_press(self):
        if self.enabled:
            popup = self.modal_popup(self, self.ui, self.dict_class, self.owner_class, self.field, self.modal_title)
            popup.open()