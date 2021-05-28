from peewee import CharField

from db.models.BaseModel import BaseModel


# Единица измерения (метры, сантиметры, шт., кубы и т.д.)
class Unit(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_unit"
