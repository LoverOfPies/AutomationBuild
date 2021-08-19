from peewee import CharField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.material.MaterialGroup import MaterialGroup


# Подгруппа
class MaterialSubgroup(BaseModel):
    name = CharField(unique=True)
    material_group = ForeignKeyField(MaterialGroup, backref='material_subgroups')

    class Meta:
        db_table = "ab_material_subgroup"
