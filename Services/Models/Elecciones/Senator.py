from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class Senator(EleccionesBase):
    Serial = TextField()
    Name = TextField()
    Identification = TextField(primary_key=True)
    TypeIdentification = TextField()
