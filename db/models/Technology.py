from peewee import CharField

from db.models.BaseModel import BaseModel


# Технология
class Technology(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_technology"
