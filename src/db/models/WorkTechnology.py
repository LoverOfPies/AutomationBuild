from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.WorkStage import WorkStage


# Технология работ
class WorkTechnology(BaseModel):
    name = CharField(unique=True)
    workstage = ForeignKeyField(WorkStage, backref='groupworks')  # этап работ

    class Meta:
        db_table = "ab_technology"
