from peewee import TextField

from Services.Models.Elecciones.BaseModelPeewee import BaseModelPeewee


class ElectionsNative(BaseModelPeewee):
    Department = TextField()
    Municipality = TextField()
    Stand = TextField()
    VotingTable = TextField()
    Votes = TextField()
    Candidate = TextField()
