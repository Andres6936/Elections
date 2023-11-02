from databases import Database
from ormar import Model
from sqlalchemy import MetaData

database = Database('sqlite:///Data/Elecciones.sqlite')
metadata = MetaData()


class BaseModel(Model):
    class Meta:
        abstract = True
        database = database
        metadata = metadata
