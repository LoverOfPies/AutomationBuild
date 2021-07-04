from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.BaseUnit import BaseUnit
from src.db.models.Technology import Technology


# Работа
class Work(BaseModel):
    name = CharField(unique=True)
    # base_amount = DoubleField(default=0)                        # базовое количество
    # full_price = DoubleField(default=0)                         # полная стоимость
    # work_price = DoubleField(default=0)                         # стоимость работ
    baseunit = ForeignKeyField(BaseUnit, backref='works')       # базовая единица
    technology = ForeignKeyField(Technology, backref='works')   # технология

    class Meta:
        db_table = "ab_work"
