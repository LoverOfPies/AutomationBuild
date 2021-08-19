from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class ErrorPopup(Popup):

    def __init__(self, message, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        self.size = [400, 400]
        self.size_hint = [None, None]
        self.auto_dismiss = False
        self.title = "Ошибка"

        main_layout = BoxLayout(orientation='vertical')
        label_error = Label(text=message)
        main_layout.add_widget(label_error)

        ok = Button(size_hint=[1, 0.2], text='ОК')
        main_layout.add_widget(ok)
        ok.bind(on_press=self.dismiss)

        self.add_widget(main_layout)
