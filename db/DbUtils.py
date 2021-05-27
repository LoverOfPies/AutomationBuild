# Изменить запись в бд
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
    city = [
        {'name': value}]
    model_class.insert(city).execute()
