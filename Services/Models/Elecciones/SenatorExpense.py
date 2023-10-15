from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class SenatorExpense(EleccionesBase):
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
