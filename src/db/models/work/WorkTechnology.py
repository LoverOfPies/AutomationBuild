from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.work.WorkStage import WorkStage


# Технология работ
class WorkTechnology(BaseModel):
    name = CharField(unique=True)
    work_stage = ForeignKeyField(WorkStage, backref='work_technologies')  # этап работ

    class Meta:
        db_table = "ab_work_technology"
