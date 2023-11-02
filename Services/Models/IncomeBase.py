from ormar import Text

from Services.Models.BaseModel import BaseModel


class IncomeBase(BaseModel):
    Serial: str = Text(primary_key=True)
    CandidateIdentification: str = Text()
    Consul: str = Text()
    TypeCandidate: str = Text()
    Department: str = Text()
    Municipality: str = Text()
    Location: str = Text()
    PoliticalParty: str = Text()
    Candidate: str = Text()
    TypeContributor: str = Text()
    ContributorName: str = Text()
    ContributionValue: str = Text()
    TypeIdentificationContribute: str = Text()
    ContributeIdentification: str = Text()
    Acta: str = Text()
    TypeContribution: str = Text()
    Coalition: str = Text()
    VoucherDate: str = Text()
    Voucher: str = Text()
    Concept: str = Text()

    class Meta:
        tablename = "IncomeBase"
