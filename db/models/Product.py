from peewee import ForeignKeyField, DoubleField

from db.models.BaseModel import BaseModel
from db.models.Material import Material
from db.models.Provider import Provider


# Товар
class Product(BaseModel):
    price = DoubleField(default=0)                              # цена
    amount_for_one = DoubleField(default=0)                     # количество материала за 1 шт
    provider = ForeignKeyField(Provider, backref='products')    # поставщик
    material = ForeignKeyField(Material, backref='products')    # материал

    class Meta:
        db_table = "ab_product"
