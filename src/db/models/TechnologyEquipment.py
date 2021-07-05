from peewee import ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.Equipment import Equipment
from src.db.models.WorkTechnology import WorkTechnology


# ManyToMany Технологии для данной комплектации
class TechnologyEquipment(BaseModel):
    technology = ForeignKeyField(WorkTechnology)
    equipment = ForeignKeyField(Equipment)

    class Meta:
        db_table = "ab_technologyequipment"
