from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class ElectionsNative(EleccionesBase):
    Department = TextField()
    Municipality = TextField()
    Stand = TextField()
    VotingTable = TextField()
    Votes = TextField()
    Candidate = TextField()
