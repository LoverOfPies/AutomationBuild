from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.material.MaterialCategory import MaterialCategory


# Группа
class MaterialGroup(BaseModel):
    name = CharField(unique=True)
    material_category = ForeignKeyField(MaterialCategory, backref='material_groups')

    class Meta:
        db_table = "ab_material_group"
