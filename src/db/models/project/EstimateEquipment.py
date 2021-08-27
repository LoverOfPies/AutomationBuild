from peewee import ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.project.Equipment import Equipment
from src.db.models.project.Estimate import Estimate


# ManyToMany Комплектации для расчёта
class EstimateEquipment(BaseModel):
    estimate = ForeignKeyField(Estimate, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='estimates')

    class Meta:
        db_table = "ab_estimate_equipment"
