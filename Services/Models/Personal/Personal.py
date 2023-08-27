from peewee import TextField, IntegerField
from pydantic import BaseModel

from Services.Models.Personal.PersonalBase import PersonalBase


class Personal(PersonalBase):
    Serial = TextField(primary_key=True)
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


class PersonalBody(BaseModel):
    Serial: str | None = None
    TypeDocument: str
    NumberDocument: int
    Names: str
    BornPlace: str
    Country: str
    Profession: str
    Experience: str
    Role: str
    Dependency: str
    Email: str
    Phone: int
    Salary: str
