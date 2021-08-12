from peewee import CharField, ForeignKeyField


from src.db.models.BaseModel import BaseModel
from src.db.models.material.MaterialSubgroup import Subgroup
from src.db.models.base.Unit import Unit


# Материал
class Material(BaseModel):
    name = CharField(unique=True)                           # наименование
    articul = CharField()                                   # артикул
    unit = ForeignKeyField(Unit, backref='materials')       # единицы измерения (шт, кубы и т.д.)
    subgroup = ForeignKeyField(Subgroup, backref='materials')  # подгруппа

    class Meta:
        db_table = "ab_material"
