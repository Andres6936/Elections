from ormar import Text

from Services.Models.BaseModel import BaseModel


class IncomeBase(BaseModel):
    CandidateIdentification = Text()
    Consul = Text()
    TypeCandidate = Text()
    Department = Text()
    Municipality = Text()
    Location = Text()
    PoliticalParty = Text()
    Candidate = Text()
    TypeContributor = Text()
    ContributorName = Text()
    ContributionValue = Text()
    TypeIdentificationContribute = Text()
    ContributeIdentification = Text()
    Acta = Text()
    TypeContribution = Text()
    Coalition = Text()
    VoucherDate = Text()
    Voucher = Text()
    Concept = Text()

    class Meta:
        tablename = "IncomeBase"
