from peewee import CharField

from db.models.BaseModel import BaseModel


# Категория
class Category(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_category"
