from peewee import SqliteDatabase, Model

db = SqliteDatabase('./Data/Personal.sqlite')


class PersonalBase(Model):
    class Meta:
        database = db
