from peewee import CharField, ForeignKeyField


from db.models.BaseModel import BaseModel
from db.models.Group import Group
from db.models.Unit import Unit


# Материал
class Material(BaseModel):
    name = CharField(unique=True)                           # наименование
    articul = CharField()                                   # артикул
    unit = ForeignKeyField(Unit, backref='materials')       # единицы измерения (шт, кубы и т.д.)
    subgroup = ForeignKeyField(Group, backref='materials')  # подгруппа

    class Meta:
        db_table = "ab_material"
