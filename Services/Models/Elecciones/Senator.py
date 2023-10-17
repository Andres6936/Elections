from peewee import TextField

from Services.Models.Elecciones.BaseModelPeewee import BaseModelPeewee


class Senator(BaseModelPeewee):
    Serial = TextField(primary_key=True)
    Name = TextField()
    Identification = TextField()
    TypeIdentification = TextField()
