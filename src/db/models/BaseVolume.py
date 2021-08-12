from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.Project import Project


# Базовый объём
class BaseVolume(BaseModel):
    name = CharField(unique=True)
    project = ForeignKeyField(Project, backref='base_volumes')
    base_unit = ForeignKeyField(BaseUnit, backref='base_volumes')

    class Meta:
        db_table = "ab_base_volume"
