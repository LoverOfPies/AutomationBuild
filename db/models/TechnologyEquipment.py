from peewee import ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.Equipment import Equipment
from db.models.Technology import Technology


# ManyToMany Технологии для данной комплектации
class TechnologyEquipment(BaseModel):
    technology = ForeignKeyField(Technology)
    equipment = ForeignKeyField(Equipment)

    class Meta:
        db_table = "ab_technologyequipment"
