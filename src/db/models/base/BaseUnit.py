from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.base.Unit import Unit


# Базовая единица
class BaseUnit(BaseModel):
    name = CharField(unique=True)
    # unit = ForeignKeyField(Unit, backref='units')

    class Meta:
        db_table = "ab_base_unit"
