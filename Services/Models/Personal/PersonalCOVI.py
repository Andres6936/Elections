from peewee import DoubleField, TextField, IntegerField

from Services.Models.Personal.PersonalBase import PersonalBase


class PersonalCOVI(PersonalBase):
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
