from peewee import CharField

from db.models.BaseModel import BaseModel


# Свойства для материалов (длина, ширина и т.д.)
class Prop(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_prop"
