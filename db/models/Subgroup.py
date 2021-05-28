from peewee import CharField, ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.Group import Group


# Подгруппа
class Subgroup(BaseModel):
    name = CharField(unique=True)
    group = ForeignKeyField(Group, backref='subgroups')

    class Meta:
        db_table = "ab_subgroup"
