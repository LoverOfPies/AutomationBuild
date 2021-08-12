from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.work.WorkTechnology import WorkTechnology


# Группа работ
class WorkGroup(BaseModel):
    name = CharField(unique=True)
    work_technology = ForeignKeyField(WorkTechnology, backref='work_groups')   # технология

    class Meta:
        db_table = "ab_work_group"
