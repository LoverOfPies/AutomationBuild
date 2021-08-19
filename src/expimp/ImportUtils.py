from openpyxl import load_workbook

from src.db.DbUtils import add_multirow
from src.gui.custom_uix.ErrorPopup import ErrorPopup


def import_single_row(filename, ui, list_name):
    wb = load_workbook(filename)
    try:
        sheet = wb.get_sheet_by_name(list_name)
    except KeyError:
        ErrorPopup(message='Неправильный файл').open()
        return
    values = []
    for cell in sheet['A']:
        if cell.row == 1:
            continue
        values.append([{'name': str(cell.value)}])
    data = dict([
        ('model_class', ui.model_class),
        ('value', values),
    ])
    add_multirow(data)
    ui.update_screen()
