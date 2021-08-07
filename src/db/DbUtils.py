# Изменить запись в бд
from src.db.models.PropMaterial import PropMaterial


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
    else:
        return True


# Удалить запись в бд
def delete_row(data):
    model_class = data.get('model_class')
    id_value = data.get('id_value')
    obj = model_class.get((model_class.id == id_value))
    obj.delete_instance()


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
    try:
        result = model_class.get_or_none(name=value[0].get('name'))
    except:
        return True
    return True if result is None else False
