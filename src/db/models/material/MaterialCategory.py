from peewee import CharField

from src.db.models.BaseModel import BaseModel


# Категория
class MaterialCategory(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_material_category"
