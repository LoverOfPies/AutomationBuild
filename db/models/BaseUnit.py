from peewee import CharField

from db.models.BaseModel import BaseModel


# Базовая единица
class BaseUnit(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_baseunit"
