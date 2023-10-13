from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class Senator(EleccionesBase):
    Serial = TextField(primary_key=True)
    Name = TextField()
    Identification = TextField()
    TypeIdentification = TextField()
