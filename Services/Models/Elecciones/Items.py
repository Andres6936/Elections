from peewee import TextField

from Services.Models.Elecciones.BaseModelPeewee import BaseModelPeewee


class Items(BaseModelPeewee):
    Serial = TextField()
    Line = TextField()
    Item = TextField()
    Price = TextField()
    Amount = TextField()
    UoM = TextField()
    Total = TextField()
    CDP = TextField()
