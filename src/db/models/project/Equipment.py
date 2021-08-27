from peewee import CharField

from src.db.models.BaseModel import BaseModel


# Комплектация
class Equipment(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_equipment"
