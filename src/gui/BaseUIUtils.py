from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from src.gui.custom_uix.AddRowButton import AddRowButton
from src.gui.custom_uix.ExportImportButton import ExportImportButton
from src.gui.custom_uix.ImportButton import ImportButton

from src.gui.custom_uix.OpenScreenButton import OpenScreenButton


# Кнопки управления
def init_control_buttons(ui):
    button_layout = BoxLayout(orientation='horizontal', padding=[0, 30], size_hint = [1, None], height=100)
    button_layout.add_widget(AddRowButton(text='Добавить',
                                          ui=ui,
                                          popup=ui.add_popup,
                                          popup_title=f'Добавление записи "{ui.table_name}"'))
    # old_import = ImportButton(text='Импорт данных',
    #                           ui=ui,
    #                           popup_title=f'Импорт данных таблицы "{ui.table_name}"')
    new_import = ExportImportButton(text='Импорт данных',
                                    ui=ui,
                                    is_import=True)
    button_layout.add_widget(new_import)
    button_layout.add_widget(ExportImportButton(text='Экспорт данных',
                                                ui=ui,
                                                is_import=False))
    return button_layout


# Заголовок формы
def init_title_layout(ui):
    title_layout = BoxLayout(orientation='horizontal', size_hint=[1, None], padding=[0, 30], height=100)
    title_label = Label(text=ui.table_name, font_size='20sp')
    title_layout.add_widget(title_label)
    return title_layout


# Кнопка назад
def init_back_button(ui):
    back_layout = BoxLayout(size_hint=[1, None], padding=[0, 5], height=50)
    back_layout.add_widget(OpenScreenButton(text='Назад', screen_name=ui.parent_screen, screen_manager=ui.sm))
    return back_layout
