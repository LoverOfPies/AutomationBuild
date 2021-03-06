from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.button import Button
from src.db.DbUtils import change_attribute


# Кнопка вызова модального окна изменения атрибута
from src.gui.custom_uix.ErrorPopup import ErrorPopup


class SelectRowButton(Button):
    button_obj = ObjectProperty()
    popup = ObjectProperty()
    name_row = StringProperty()
    change_flag = BooleanProperty()

    owner_class = ObjectProperty()
    dict_class = ObjectProperty()
    id_value = StringProperty()
    field = StringProperty()

    def on_press(self):
        if self.change_flag:
            owner = self.owner_class.select().where(self.owner_class.name == self.name_row)
            if not bool(owner):
                self.dismiss()
                ErrorPopup(message="Поле не может быть пустым").open()
                return
            data = dict([
                ('model_class', self.dict_class),
                ('id_value', self.id_value),
                ('field', self.field),
                ('value', owner)
            ])
            change_attribute(data)
        self.button_obj.text = self.name_row
        self.popup.dismiss()
