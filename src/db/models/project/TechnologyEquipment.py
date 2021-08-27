from peewee import ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.project.Equipment import Equipment
from src.db.models.work.WorkTechnology import WorkTechnology


# ManyToMany Технологии для данной комплектации
class TechnologyEquipment(BaseModel):
    technology = ForeignKeyField(WorkTechnology, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='technologies')

    class Meta:
        db_table = "ab_technology_equipment"
