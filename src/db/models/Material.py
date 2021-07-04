from peewee import CharField, ForeignKeyField


from src.db.models.BaseModel import BaseModel
from src.db.models.Group import Group
from src.db.models.Unit import Unit


# Материал
class Material(BaseModel):
    name = CharField(unique=True)                           # наименование
    articul = CharField()                                   # артикул
    unit = ForeignKeyField(Unit, backref='materials')       # единицы измерения (шт, кубы и т.д.)
    subgroup = ForeignKeyField(Group, backref='materials')  # подгруппа

    class Meta:
        db_table = "ab_material"
