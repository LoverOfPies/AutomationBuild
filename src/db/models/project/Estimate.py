from peewee import ForeignKeyField, CharField, IntegerField

from src.db.models.BaseModel import BaseModel
from src.db.models.project.Project import Project
from src.db.models.provider.City import City


# Расчёт
class Estimate(BaseModel):
    number = IntegerField(unique=True)
    client_fio = CharField(unique=True)
    city = ForeignKeyField(City, backref='estimates')
    project = ForeignKeyField(Project, backref='estimates')

    class Meta:
        db_table = "ab_estimate"
