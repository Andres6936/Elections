from peewee import TextField

from Services.Models.Elecciones.BaseModelPeewee import BaseModelPeewee


class ElectionsNational(BaseModelPeewee):
    Department = TextField()
    Municipality = TextField()
    Stand = TextField()
    VotingTable = TextField()
    Votes = TextField()
    Candidate = TextField()
