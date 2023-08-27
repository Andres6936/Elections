from peewee import DoubleField, TextField, IntegerField
from pydantic import BaseModel

from Services.Models.Personal.PersonalBase import PersonalBase


class PersonalCOVI(PersonalBase):
    Serial = TextField(primary_key=True)
    Nit = DoubleField()
    Business = TextField()
    TypeBusiness = IntegerField()
    NumberDocument = TextField()
    Names = TextField()
    Profession = TextField()
    TypeVehicle = TextField()
    NumberVehicle = TextField()
    Phone = TextField()
    Address = TextField()
    Age = TextField()
    Eps = TextField()


class PersonalCOVIBody(BaseModel):
    Serial: str | None = None
    Nit: float
    Business: str
    TypeBusiness: int
    NumberDocument: str
    Names: str
    Profession: str
    TypeVehicle: str
    NumberVehicle: str
    Phone: str
    Address: str
    Age: str
    Eps: str
