from peewee import CharField

from src.db.models.BaseModel import BaseModel


# Проект
class Project(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_project"
