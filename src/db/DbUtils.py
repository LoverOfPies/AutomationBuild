# Изменить запись в бд
from peewee import IntegrityError

from src.gui.custom_uix.ErrorPopup import ErrorPopup


def change_attribute(data):
    model_class = data.get('model_class')
    id_value = data.get('id_value')
    field = data.get('field')
    value = data.get('value')
    obj = model_class.get((model_class.id == id_value))
    field_data = dict(obj.__data__)
    field_data[field] = value
    query = model_class.update(**field_data).where(
        model_class.id == obj.id)
    if query.execute() == 0:
        raise Exception()


# Удалить запись в бд
def delete_row(data):
    model_class = data.get('model_class')
    id_value = data.get('id_value')
    obj = model_class.get((model_class.id == id_value))
    try:
        foreign_tables = [table for table in obj._meta.model_backrefs]
        for foreign_table in foreign_tables:
            foreign_keys = [key for key in foreign_table._meta.refs]
            for foreign_key in foreign_keys:
                if foreign_key.rel_model == model_class:
                    link_quantity = len(foreign_table.select().where(foreign_key == obj))
                    if link_quantity > 0:
                        ErrorPopup(message="На объект есть ссылки " + str(link_quantity)).open()
                        return False
        obj.delete_instance()
    except IntegrityError:
        return False


# Добавить запись в бд
def add_row(data):
    model_class = data.get('model_class')
    value = data.get('value')
    if check_value(value, model_class):
        model_class.insert(value).execute()


# Добавить несколько записей в бд
def add_multirow(data):
    model_class = data.get('model_class')
    values = data.get('value')
    for value in values:
        if check_value(value, model_class):
            model_class.insert(value).execute()


def check_value(value, model_class):
    # Проверка на заполненность полей
    fields = [key for key in model_class._meta.fields]
    fields.remove('id')
    for field in fields:
        if bool(value[0].get(field)):
            continue
        else:
            ErrorPopup(message="Не заполнены все поля").open()
            return False

    # Проверка уникальности наименования
    try:
        result = model_class.get_or_none(name=value[0].get('name'))
    except AttributeError:
        return True
    return True if result is None else False
