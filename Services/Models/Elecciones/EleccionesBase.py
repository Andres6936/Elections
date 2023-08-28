from peewee import SqliteDatabase, Model

db = SqliteDatabase('./Data/Elecciones.sqlite')


class EleccionesBase(Model):
    class Meta:
        database = db
