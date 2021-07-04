from peewee import CharField

from src.db.models.BaseModel import BaseModel


# Город
class City(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_city"
