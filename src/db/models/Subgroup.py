from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.Group import Group


# Подгруппа
class Subgroup(BaseModel):
    name = CharField(unique=True)
    group = ForeignKeyField(Group, backref='subgroups')

    class Meta:
        db_table = "ab_subgroup"
