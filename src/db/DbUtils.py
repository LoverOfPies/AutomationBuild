# Изменить запись в бд
import inspect
import sys

from peewee import IntegrityError, Model

from src.db.models.BaseModel import BaseModel
from src.gui.custom_uix.ErrorPopup import ErrorPopup


def get_models():
    def get_submodules(module):
        submodules = [obj for name, obj in inspect.getmembers(module) if inspect.ismodule(obj)]
        result_tables = []
        for submodule in submodules:
            if has_submodules(submodule):
                result_tables = result_tables + get_submodules(submodule)
            else:
                result_tables.append(submodule)
        return result_tables

    def has_submodules(module):
        return True if len([obj for name, obj in inspect.getmembers(module) if inspect.ismodule(obj)]) > 0 else False

    def get_model_classes(module):
        return [obj for name, obj in inspect.getmembers(module)
                if inspect.isclass(obj)
                and obj is not BaseModel
                and obj is not Model
                and isinstance(obj, type(BaseModel))]

    models_module = sys.modules['src.db.models']
    modules = get_submodules(models_module)
    models = []
    for model_class in modules:
        models = models + get_model_classes(model_class)
    return set(models)


def create_table_with_backref(table):
    backref_tables = table._meta.model_backrefs
    for ref in table._meta.refs:
        if not ref.rel_model.table_exists():
            create_table_with_backref(ref.rel_model)
    table.create_table()
    for backref_table in backref_tables:
        create_table_with_backref(backref_table)


# Создать таблицы в БД
def init_tables():
    first_models = [model for model in get_models() if len(model._meta.refs) < 1]
    for model in first_models:
        create_table_with_backref(model)


# Изменить значение атрибута в таблице
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
                        ErrorPopup(message=f'На объект есть ссылки {link_quantity}').open()
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


# Проверки при добавлении записи
def check_value(value, model_class):
    # Проверка на заполненность полей
    fields = [key for key in model_class._meta.fields]
    fields.remove('id')
    fields.remove('uuid')
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
