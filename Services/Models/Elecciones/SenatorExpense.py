from peewee import TextField

from Services.Models.Elecciones.BaseModelPeewee import BaseModelPeewee


class SenatorExpense(BaseModelPeewee):
    Serial = TextField(primary_key=True)
    Consul = TextField()
    District = TextField()
    Department = TextField()
    PoliticalParty = TextField()
    Concept = TextField()
    Name = TextField()
    TypePerson = TextField()
    Value = TextField()
    DescriptionConcept = TextField()
    TypePropaganda = TextField()
    Senator = TextField()
