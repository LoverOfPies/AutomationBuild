from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.WorkTechnology import WorkTechnology


# Группа работ
class WorkGroup(BaseModel):
    name = CharField(unique=True)
    worktechnology = ForeignKeyField(WorkTechnology, backref='groupworks')   # технология

    class Meta:
        db_table = "ab_work"
