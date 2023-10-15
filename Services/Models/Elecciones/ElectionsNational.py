from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class ElectionsNational(EleccionesBase):
    Department = TextField()
    Municipality = TextField()
    Stand = TextField()
    VotingTable = TextField()
    Votes = TextField()
    Candidate = TextField()
