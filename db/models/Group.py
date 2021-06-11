from peewee import CharField, ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.Category import Category


# Группа
class Group(BaseModel):
    name = CharField(unique=True)
    category = ForeignKeyField(Category, backref='groups')

    class Meta:
        db_table = "ab_group"
