from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class IncomeBase(EleccionesBase):
    CandidateIdentification = TextField()
    Consul = TextField()
    TypeCandidate = TextField()
    Department = TextField()
    Municipality = TextField()
    Location = TextField()
    PoliticalParty = TextField()
    Candidate = TextField()
    TypeContributor = TextField()
    ContributorName = TextField()
    ContributionValue = TextField()
    TypeIdentificationContribute = TextField()
    ContributeIdentification = TextField()
    Acta = TextField()
    TypeContribution = TextField()
    Coalition = TextField()
    VoucherDate = TextField()
    Voucher = TextField()
    Concept = TextField()
