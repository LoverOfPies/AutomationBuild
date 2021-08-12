from peewee import CharField

from src.db.models.BaseModel import BaseModel


# Этап работ
class WorkStage(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_work_stage"
