from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class Items(EleccionesBase):
    Serial = TextField()
    Line = TextField()
    Item = TextField()
    Price = TextField()
    Amount = TextField()
    UoM = TextField()
    Total = TextField()
    CDP = TextField()
