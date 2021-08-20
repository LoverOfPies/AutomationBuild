from peewee import PostgresqlDatabase, Model, PrimaryKeyField

psql_db = PostgresqlDatabase('automation_build', user='sysdba', host='127.0.0.1',
                             password='uwotmate')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True, null=False)

    class Meta:
        database = psql_db
        order_by = 'id'
