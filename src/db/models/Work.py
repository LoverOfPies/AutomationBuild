from peewee import CharField, ForeignKeyField, DoubleField

from src.db.models.BaseModel import BaseModel
from src.db.models.BaseUnit import BaseUnit
from src.db.models.WorkGroup import WorkGroup


# Работа
class Work(BaseModel):
    name = CharField(unique=True)
    # base_amount = DoubleField(default=0)                        # базовое количество
    client_price = DoubleField(default=0)                       # тариф клиента
    work_price = DoubleField(default=0)                         # тариф себестоимости
    baseunit = ForeignKeyField(BaseUnit, backref='works')       # базовая единица
    groupwork = ForeignKeyField(WorkGroup, backref='works')     # технология

    class Meta:
        db_table = "ab_work"
