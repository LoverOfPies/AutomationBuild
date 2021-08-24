from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from src.gui.custom_uix.ExportButton import ExportButton
from src.gui.custom_uix.ImportButton import ImportButton


def init_control_buttons(button_layout, ui):
    button_layout.add_widget(ImportButton(text='Импорт данных',
                                          ui=ui,
                                          popup_title=f'Импорт данных таблицы \"{ui.table_name}\"'))
    button_layout.add_widget(ExportButton(text='Экспорт данных',
                                          model=ui.model_class))


def init_title_layout(ui):
    title_layout = BoxLayout(orientation='horizontal', size_hint=[1, .3], padding=[0, 30])
    title_label = Label(text=ui.table_name, font_size='20sp')
    title_layout.add_widget(title_label)
    return title_layout
