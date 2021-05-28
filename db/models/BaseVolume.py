from peewee import CharField, ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.BaseUnit import BaseUnit
from db.models.Project import Project


# Базовый объём
class BaseVolume(BaseModel):
    name = CharField(unique=True)
    project = ForeignKeyField(Project, backref='base_volumes')
    base_unit = ForeignKeyField(BaseUnit, backref='base_volumes')

    class Meta:
        db_table = "ab_basevolume"
