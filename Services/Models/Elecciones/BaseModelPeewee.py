from peewee import SqliteDatabase, Model

db = SqliteDatabase('./Data/Elecciones.sqlite')


class BaseModelPeewee(Model):
    class Meta:
        database = db
