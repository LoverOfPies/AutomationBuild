from peewee import DoubleField, ForeignKeyField

from src.db.models.BaseModel import BaseModel
from src.db.models.material.Material import Material
from src.db.models.base.Prop import Prop
from src.db.models.base.Unit import Unit


# Свойство и параметры для конкретного материала
class MaterialProperty(BaseModel):
    amount = DoubleField(default=0)                                      # число для свойства данного материала
    material = ForeignKeyField(Material, backref='material_properties')  # материал
    prop = ForeignKeyField(Prop, backref='material_properties')  # свойство
    unit = ForeignKeyField(Unit, backref='material_properties')          # единицы измерения

    class Meta:
        db_table = "ab_material_property"
