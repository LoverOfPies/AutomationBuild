from peewee import ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.project.Equipment import Equipment
from src.db.models.work.WorkGroup import WorkGroup


# ManyToMany Группы работ для данной комплектации
class WorkGroupEquipment(BaseModel):
    work_group = ForeignKeyField(WorkGroup, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='work_groups')

    class Meta:
        db_table = "ab_technology_equipment"
