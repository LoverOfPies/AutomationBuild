from peewee import DoubleField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.material.Material import Material
from src.db.models.work.Work import Work


# Материал для работы
class WorkMaterial(BaseModel):
    # logistic_price = DoubleField(default=0)                             # цена за логистику
    amount = DoubleField(default=0)                                     # количество материала
    material = ForeignKeyField(Material, backref='work_materials')      # материал
    work = ForeignKeyField(Work, backref='work_materials')              # работа

    class Meta:
        db_table = "ab_work_material"
