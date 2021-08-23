from uuid import uuid4
from peewee import PostgresqlDatabase, Model, PrimaryKeyField, UUIDField

psql_db = PostgresqlDatabase('automation_build', user='sysdba', host='127.0.0.1',
                             password='masterkey')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True, null=False)
    uuid = UUIDField(default=uuid4)

    class Meta:
        database = psql_db
        order_by = 'id'
