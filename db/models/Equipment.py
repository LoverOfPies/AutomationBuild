from peewee import CharField

from db.models.BaseModel import BaseModel


# Комплектация
class Equipment(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_equipment"
