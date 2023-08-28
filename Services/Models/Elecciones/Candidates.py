from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class Candidates(EleccionesBase):
    Serial = TextField(primary_key=True)
    Candidate = TextField()
    PoliticalParty = TextField()
