from peewee import CharField, ForeignKeyField

from db.models.BaseModel import BaseModel
from db.models.City import City


# Поставщик
class Provider(BaseModel):
    name = CharField(unique=True)
    city = ForeignKeyField(City, backref='providers')

    class Meta:
        db_table = "ab_provider"
