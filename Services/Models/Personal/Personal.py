from peewee import TextField, IntegerField

from Services.Models.Personal.PersonalBase import PersonalBase


class Personal(PersonalBase):
    TypeDocument = TextField()
    NumberDocument = IntegerField()
    Names = TextField()
    BornPlace = TextField()
    Country = TextField()
    Profession = TextField()
    Experience = TextField()
    Role = TextField()
    Dependency = TextField()
    Email = TextField()
    Phone = IntegerField()
    Salary = TextField()
