from peewee import DoubleField, ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.Material import Material
from db.models.Prop import Prop
from db.models.Unit import Unit


# Свойство и параметры для конкретного материала
class PropMaterial(BaseModel):
    amount = DoubleField(default=0)                                     # число для свойства данного материала
    material = ForeignKeyField(Material, backref='property_materials')  # материал
    prop = ForeignKeyField(Prop, backref='property_materials')          # свойство
    unit = ForeignKeyField(Unit, backref='property_materials')          # единицы измерения

    class Meta:
        db_table = "ab_propmaterial"
