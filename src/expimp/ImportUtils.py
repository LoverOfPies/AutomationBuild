from openpyxl import load_workbook

from src.db.DbUtils import add_multirow


def import_single_row(filename, ui):
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name('Лист1')
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
