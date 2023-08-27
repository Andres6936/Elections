import uuid

from peewee import TextField, IntegerField
from pydantic import BaseModel

from Services.Models.Personal.PersonalBase import PersonalBase


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

    @staticmethod
    def From(body: PersonalBody):
        return Personal.create(
            Serial=uuid.uuid4(),
            TypeDocument=body.TypeDocument,
            NumberDocument=body.NumberDocument,
            Names=body.Names.upper(),
            BornPlace=body.BornPlace.upper(),
            Country=body.Country.upper(),
            Profession=body.Profession.upper(),
            Experience=body.Experience,
            Role=body.Role.upper(),
            Dependency=body.Dependency,
            Email=body.Email,
            Phone=body.Phone,
            Salary=body.Salary,
        )
