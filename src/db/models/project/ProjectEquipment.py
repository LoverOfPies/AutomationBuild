from peewee import ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.project.Equipment import Equipment
from src.db.models.project.Project import Project


# ManyToMany Комплектации для проекта
class ProjectEquipment(BaseModel):
    project = ForeignKeyField(Project, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='projects')

    class Meta:
        db_table = "ab_project_equipment"
